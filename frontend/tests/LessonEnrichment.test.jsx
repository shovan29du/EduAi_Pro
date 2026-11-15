import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, within } from '@testing-library/react';
import LessonEnrichment from '../src/components/LessonEnrichment.jsx';

const ok = (body) => Promise.resolve({ ok: true, json: () => Promise.resolve(body) });
const fail = () => Promise.resolve({ ok: false, status: 500, json: () => Promise.resolve({}) });
const COMMONS = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/BS.png/320px-BS.png';

const ENRICHMENT = {
  lesson_id: 'finance-m1-l1', subject: 'Finance', query: 'Option Pricing', wiki_title: 'Black–Scholes model',
  topic: {
    formulas: [{ label: 'Put–call parity', expr: 'C − P = S − K e^(−rT)', note: 'Links call and put prices' }],
    tables: [{ title: 'Greeks', headers: ['Greek', 'Measures'], rows: [['Delta', 'Price sensitivity']] }],
    cases: [{ title: 'Black–Scholes and the CBOE', when: '1973', summary: 'The formula appeared as options trading opened.', takeaway: 'A formula created a market.', wiki: 'Black–Scholes model' }],
  },
  subject_pack: {
    formulas: [{ label: 'NPV', expr: 'NPV = Σ CF/(1+r)^t', note: '' }],
    tables: [{ title: 'Common financial ratios', headers: ['Ratio', 'Reads as'], rows: [['Current ratio', 'Liquidity']] }],
    cases: [{ title: 'Long-Term Capital Management', when: '1998', summary: 'A hedge fund failed.', takeaway: 'Leverage multiplies damage.', wiki: 'Long-Term Capital Management' }],
  },
};
const ARTICLE = { available: true, title: 'Black–Scholes model', description: 'Mathematical model', extract: 'It estimates the price of options.', thumbnail_url: COMMONS, page_url: 'https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model' };

function install({ enrichment = () => ok(ENRICHMENT), article = () => ok(ARTICLE) } = {}) {
  global.fetch = vi.fn((url) => {
    const u = String(url);
    if (u.startsWith('/api/lesson-enrichment/wiki')) return article(u);
    if (u.startsWith('/api/lesson-enrichment/')) return enrichment(u);
    if (u.startsWith('/api/museum/thumbnail')) return ok({ thumbnail_url: COMMONS });
    if (u.startsWith('/api/museum/credit')) return ok({ known: true, line: 'A. Photographer · CC BY-SA 4.0', artist: 'A. Photographer', license: 'CC BY-SA 4.0', license_url: 'https://example.org/l', source_url: 'https://example.org/s' });
    return fail();
  });
}

beforeEach(() => install());

describe('LessonEnrichment', () => {
  it('shows the related picture, formulas, tables and case studies for a Master\'s lesson', async () => {
    render(<LessonEnrichment lessonId="finance-m1-l1" levelId="M1" />);
    expect(await screen.findByText('It estimates the price of options.')).toBeInTheDocument();
    expect(screen.getByRole('img', { name: 'Black–Scholes model' })).toHaveAttribute('src', COMMONS);
    expect(screen.getByRole('link', { name: /Read the full article/ })).toHaveAttribute('href', ARTICLE.page_url);
    expect(screen.getByText(/Text under CC BY-SA/)).toBeInTheDocument();

    expect(screen.getByText('C − P = S − K e^(−rT)')).toBeInTheDocument();
    expect(screen.getByRole('table', { name: 'Greeks' })).toBeInTheDocument();
    expect(screen.getByText(/The formula appeared as options trading opened/)).toBeInTheDocument();
    expect(screen.getByText(/A formula created a market./)).toBeInTheDocument();

    const sheet = screen.getByText(/Finance reference sheet/).closest('details');
    expect(within(sheet).getByText('NPV = Σ CF/(1+r)^t')).toBeInTheDocument();
    expect(within(sheet).getByRole('table', { name: 'Common financial ratios' })).toBeInTheDocument();
    expect(await within(sheet).findByRole('img', { name: 'Long-Term Capital Management' })).toBeInTheDocument();
  });

  it('asks Wikipedia for the exact article and falls back to the topic query', async () => {
    render(<LessonEnrichment lessonId="finance-m1-l1" levelId="M1" />);
    await screen.findByText('It estimates the price of options.');
    const call = global.fetch.mock.calls.map((c) => String(c[0])).find((u) => u.startsWith('/api/lesson-enrichment/wiki'));
    expect(call).toContain('title=Black%E2%80%93Scholes+model');
    expect(call).toContain('q=Option+Pricing');
  });

  it('shows only the subject reference sheet when a lesson has no topic-specific content', async () => {
    install({ enrichment: () => ok({ ...ENRICHMENT, wiki_title: '', topic: { formulas: [], tables: [], cases: [] } }) });
    render(<LessonEnrichment lessonId="finance-m1-l2" levelId="M2" />);
    expect(await screen.findByText(/Finance reference sheet/)).toBeInTheDocument();
    expect(screen.queryByText('On this topic')).toBeNull();
  });

  it('does nothing outside Master\'s levels', () => {
    const { container } = render(<LessonEnrichment lessonId="x" levelId="UG3" />);
    expect(container).toBeEmptyDOMElement();
    expect(global.fetch).not.toHaveBeenCalled();
  });

  it('stays quiet when enrichment cannot be loaded', async () => {
    install({ enrichment: () => fail() });
    const { container } = render(<LessonEnrichment lessonId="finance-m1-l1" levelId="M1" />);
    await vi.waitFor(() => expect(container).toBeEmptyDOMElement());
  });

  it('still shows formulas and cases when no related article is found', async () => {
    install({ article: () => ok({ available: false }) });
    render(<LessonEnrichment lessonId="finance-m1-l1" levelId="M1" />);
    expect(await screen.findByText('C − P = S − K e^(−rT)')).toBeInTheDocument();
    expect(screen.queryByLabelText('Related article')).toBeNull();
  });
});
