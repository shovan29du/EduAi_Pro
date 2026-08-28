import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SubjectLessons from '../src/components/SubjectLessons.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

vi.mock('../src/components/MediaSection.jsx', () => ({
  default: ({ title }) => <div>{title}</div>,
}));

const subject = {
  books: [{ id: 'b1', title: 'A Book', link: 'https://example.com', safe: true }],
  video_resources: [{ title: 'A Video', url: 'https://www.youtube.com/watch?v=abc123', safe: true }],
  info_cards: [{ title: 'A Card', fact: 'A fact', safe: true }],
};

beforeEach(() => {
  localStorage.clear();
  global.fetch = vi.fn((url) => {
    if (url === '/api/progress/Shovan') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ completed_lessons: {} }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('SubjectLessons', () => {
  it('shows every lesson open from the start, with no lock on later lessons', async () => {
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Math" subject={subject} />
      </ChildProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Lesson 1: Learn')).toBeInTheDocument();
    });
    // All lessons are visible and unlocked immediately -- no "Complete X first" gating.
    expect(screen.queryByText(/first to unlock/)).not.toBeInTheDocument();
    expect(screen.getByText('Lesson 2: Watch')).toBeInTheDocument();

    fireEvent.click(screen.getAllByRole('button', { name: 'Mark lesson complete' })[0]);

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/progress/Shovan',
        expect.objectContaining({ method: 'POST' })
      );
    });
    // Lesson 2 remains visible and was never gated behind lesson 1's completion.
    expect(screen.getByText('Lesson 2: Watch')).toBeInTheDocument();
  });
});

describe('SubjectLessons book excerpts from library', () => {
  it("shows a book excerpt Ark AI linked to a curriculum lesson", async () => {
    const subjectWithLessons = {
      lessons: [
        {
          id: 'l1',
          title: 'Photosynthesis',
          unit: 'Plants',
          book_excerpts: [
            { book: 'Botany Basics', kind: 'example', form: 'summary', content: 'Leaves capture sunlight and convert it into energy.' },
          ],
        },
      ],
    };
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Science" subject={subjectWithLessons} standard={11} />
      </ChildProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Lesson 1: Curriculum Lessons')).toBeInTheDocument();
    });

    expect(screen.getByText('From your library')).toBeInTheDocument();
    expect(screen.getByText('✨ Example')).toBeInTheDocument();
    expect(screen.getByText('summarised')).toBeInTheDocument();
    expect(screen.getByText('Leaves capture sunlight and convert it into energy.')).toBeInTheDocument();
    expect(screen.getByText('from "Botany Basics"')).toBeInTheDocument();
  });

  it('renders a table-kind excerpt as a real table, not a paragraph', async () => {
    const subjectWithLessons = {
      lessons: [{
        id: 'l1', title: 'Photosynthesis', unit: 'Plants',
        book_excerpts: [{
          book: 'Botany Basics', kind: 'table', form: 'full',
          content: '| Stage | Product |\n|---|---|\n| Light reaction | ATP, NADPH |\n| Calvin cycle | Glucose |',
        }],
      }],
    };
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Science" subject={subjectWithLessons} standard={11} />
      </ChildProvider>
    );
    await waitFor(() => expect(screen.getByText('✨ Table')).toBeInTheDocument());

    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();
    expect(screen.getByRole('columnheader', { name: 'Stage' })).toBeInTheDocument();
    expect(screen.getByRole('columnheader', { name: 'Product' })).toBeInTheDocument();
    expect(screen.getByRole('cell', { name: 'Light reaction' })).toBeInTheDocument();
    expect(screen.getByRole('cell', { name: 'Glucose' })).toBeInTheDocument();
  });

  it('renders a concept_map-kind excerpt as connected nodes, not a paragraph', async () => {
    const subjectWithLessons = {
      lessons: [{
        id: 'l1', title: 'The Water Cycle', unit: 'Earth Science',
        book_excerpts: [{
          book: 'Earth Basics', kind: 'concept_map', form: 'full',
          content: 'Evaporation -> Condensation -> Precipitation -> Collection',
        }],
      }],
    };
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Science" subject={subjectWithLessons} standard={11} />
      </ChildProvider>
    );
    await waitFor(() => expect(screen.getByText('✨ Concept map')).toBeInTheDocument());

    expect(screen.getByText('Evaporation')).toBeInTheDocument();
    expect(screen.getByText('Condensation')).toBeInTheDocument();
    expect(screen.getByText('Precipitation')).toBeInTheDocument();
    expect(screen.getByText('Collection')).toBeInTheDocument();
    expect(screen.queryByText(/Evaporation -> Condensation/)).not.toBeInTheDocument();
  });

  it('renders a graph-kind excerpt distinctly from plain prose even without parseable structure', async () => {
    const subjectWithLessons = {
      lessons: [{
        id: 'l1', title: 'Growth Rates', unit: 'Plants',
        book_excerpts: [{
          book: 'Botany Basics', kind: 'graph', form: 'summary',
          content: 'Figure 3 plots leaf growth rate against sunlight exposure over 10 days.',
        }],
      }],
    };
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Science" subject={subjectWithLessons} standard={11} />
      </ChildProvider>
    );
    await waitFor(() => expect(screen.getByText('✨ Graph')).toBeInTheDocument());
    expect(screen.getByText(/📊 Figure 3 plots leaf growth rate/)).toBeInTheDocument();
  });

  it('renders a lesson-specific figure diagram, data table, graph, formulae, and photo', async () => {
    global.fetch = vi.fn((url) => {
      if (url === '/api/progress/Shovan') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ completed_lessons: {} }) });
      }
      if (String(url).startsWith('/api/museum/thumbnail')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: 'https://example.com/photo.jpg' }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    const subjectWithLessons = {
      lessons: [{
        id: 'l1',
        title: 'Percentages',
        unit: 'Number',
        wiki_title: 'Percentages',
        figure: { caption: 'Key concepts in “Percentages”', nodes: ['percent', 'per hundred', 'conversion'] },
        data_table: { headers: ['Fraction', 'Percent'], rows: [['1/4', '25%'], ['1/2', '50%']] },
        graph: { title: 'Example Growth', points: [2, 4, 7, 9], x_axis: 'Week', y_axis: 'Value' },
        formulae: ['Percent = (Part ÷ Whole) × 100'],
      }],
    };
    const { container } = render(
      <ChildProvider>
        <SubjectLessons subjectName="Math" subject={subjectWithLessons} standard={5} />
      </ChildProvider>
    );

    await waitFor(() => expect(screen.getByRole('heading', { name: 'Percentages' })).toBeInTheDocument());

    // Concept-flow figure diagram
    expect(screen.getByText('Key concepts in “Percentages”')).toBeInTheDocument();
    expect(screen.getByText('percent')).toBeInTheDocument();
    expect(screen.getByText('per hundred')).toBeInTheDocument();

    // Data table
    expect(screen.getByRole('columnheader', { name: 'Fraction' })).toBeInTheDocument();
    expect(screen.getByRole('cell', { name: '25%' })).toBeInTheDocument();

    // Graph (SVG line chart)
    expect(screen.getByRole('img', { name: 'Example Growth' })).toBeInTheDocument();

    // Formulae
    expect(screen.getByText('Percent = (Part ÷ Whole) × 100')).toBeInTheDocument();

    // Real-photo lookup via the live Wikipedia thumbnail proxy
    await waitFor(() => expect(container.querySelector('img[src="https://example.com/photo.jpg"]')).toBeInTheDocument());
    expect(global.fetch).toHaveBeenCalledWith('/api/museum/thumbnail?wiki_title=Percentages');
  });

  it('renders code-kind excerpts in a monospace code block', async () => {
    const subjectWithLessons = {
      lessons: [{
        id: 'l1', title: 'Loops', unit: 'Programming',
        book_excerpts: [{
          book: 'Learn Python', kind: 'code', form: 'full',
          content: 'for i in range(10):\n    print(i)',
        }],
      }],
    };
    render(
      <ChildProvider>
        <SubjectLessons subjectName="CS" subject={subjectWithLessons} standard={11} />
      </ChildProvider>
    );
    await waitFor(() => expect(screen.getByText('✨ Code')).toBeInTheDocument());
    expect(screen.getByText((_, el) => el.tagName === 'CODE' && el.textContent.includes('range(10)'))).toBeInTheDocument();
  });
});
