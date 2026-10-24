import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import PDFExplainer from '../src/components/PDFExplainer.jsx';

const uploadedDoc = {
  id: 'doc123',
  filename: 'bio.pdf',
  child: 'TestChild',
  page_count: 1,
  char_count: 103,
  summary: 'A short summary of the uploaded PDF.',
};

function mockFetch({ documents = [] } = {}) {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u.startsWith('/api/pdf-explainer/upload') && options.method === 'POST') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(uploadedDoc) });
    }
    if (u.startsWith('/api/pdf-explainer?') || u === '/api/pdf-explainer') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(documents) });
    }
    if (u.match(/\/api\/pdf-explainer\/doc123\/explain$/)) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ explanation: 'This document explains cell biology simply.' }) });
    }
    if (u.match(/\/api\/pdf-explainer\/doc123\/ask$/)) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ answer: 'The mitochondria is the powerhouse of the cell.' }) });
    }
    if (u.match(/\/api\/pdf-explainer\/doc123\/quiz$/)) {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          quiz: [
            { question: 'What is the powerhouse of the cell?', options: { A: 'Nucleus', B: 'Mitochondria', C: 'Ribosome', D: 'Golgi' }, answer: 'B', explanation: 'Mitochondria produce energy.' },
          ],
        }),
      });
    }
    if (u.match(/\/api\/pdf-explainer\/doc123\/notes/) && (!options.method || options.method === 'GET')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u.match(/\/api\/pdf-explainer\/doc123\/notes$/) && options.method === 'POST') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ id: 'note1', doc_id: 'doc123', text: 'my note', child: 'TestChild' }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

function uploadFile() {
  const file = new File(['%PDF-1.4 fake pdf content'], 'bio.pdf', { type: 'application/pdf' });
  const input = document.querySelector('input[type="file"]');
  fireEvent.change(input, { target: { files: [file] } });
}

describe('PDFExplainer', () => {
  it('shows empty state when no documents are uploaded', async () => {
    render(<PDFExplainer />);
    expect(await screen.findByText('No PDFs uploaded yet.')).toBeInTheDocument();
  });

  it('uploads a PDF and selects it automatically', async () => {
    render(<PDFExplainer child="TestChild" />);
    await screen.findByText('No PDFs uploaded yet.');

    uploadFile();

    expect(await screen.findByRole('heading', { name: 'bio.pdf' })).toBeInTheDocument();
    expect(screen.getByText('A short summary of the uploaded PDF.')).toBeInTheDocument();
  });

  it('explains the selected document', async () => {
    render(<PDFExplainer child="TestChild" />);
    await screen.findByText('No PDFs uploaded yet.');
    uploadFile();
    await screen.findByRole('heading', { name: 'bio.pdf' });

    fireEvent.click(screen.getByText('Explain this document'));

    expect(await screen.findByText('This document explains cell biology simply.')).toBeInTheDocument();
  });

  it('answers a question about the document', async () => {
    render(<PDFExplainer child="TestChild" />);
    await screen.findByText('No PDFs uploaded yet.');
    uploadFile();
    await screen.findByRole('heading', { name: 'bio.pdf' });

    fireEvent.click(screen.getByText('❓ Ask'));
    fireEvent.change(screen.getByPlaceholderText('Ask a question about this document…'), {
      target: { value: 'What is mitochondria?' },
    });
    fireEvent.click(screen.getByText('Ask'));

    expect(await screen.findByText('The mitochondria is the powerhouse of the cell.')).toBeInTheDocument();
  });

  it('generates and takes a quiz', async () => {
    render(<PDFExplainer child="TestChild" />);
    await screen.findByText('No PDFs uploaded yet.');
    uploadFile();
    await screen.findByRole('heading', { name: 'bio.pdf' });

    fireEvent.click(screen.getByText('📝 Quiz'));
    fireEvent.click(screen.getByText('Generate a quiz'));

    expect(await screen.findByText(/What is the powerhouse of the cell\?/)).toBeInTheDocument();
    fireEvent.click(screen.getByText(/B\) Mitochondria/));
    fireEvent.click(screen.getByText('Submit'));

    await waitFor(() => {
      expect(screen.getByText('Score: 1 / 1')).toBeInTheDocument();
    });
  });

  it('adds a note to the document', async () => {
    render(<PDFExplainer child="TestChild" />);
    await screen.findByText('No PDFs uploaded yet.');
    uploadFile();
    await screen.findByRole('heading', { name: 'bio.pdf' });

    fireEvent.click(screen.getByText('🗒️ Notes'));
    fireEvent.change(screen.getByPlaceholderText('Write a note about this document…'), {
      target: { value: 'my note' },
    });
    fireEvent.click(screen.getByText('Save note'));

    expect(await screen.findByText('my note')).toBeInTheDocument();
  });
});
