import React, { Suspense, lazy, useEffect, useState } from 'react';
import { getLessonEnrichment, getRelatedArticle, isEnrichedLevel } from '../api/lessonEnrichment.js';
import ImageCredit from './ImageCredit.jsx';

const LessonChart = lazy(() => import('./LessonChart.jsx'));

const thumbCache = {};

function useThumbnail(wikiTitle) {
  const [src, setSrc] = useState(thumbCache[wikiTitle] || null);
  useEffect(() => {
    if (!wikiTitle) return undefined;
    if (thumbCache[wikiTitle] !== undefined) { setSrc(thumbCache[wikiTitle] || null); return undefined; }
    let active = true;
    fetch(`/api/museum/thumbnail?wiki_title=${encodeURIComponent(wikiTitle)}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        // Only freely licensed Wikimedia Commons images are shown.
        const url = /^https:\/\/upload\.wikimedia\.org\/wikipedia\/commons\//.test(d?.thumbnail_url || '') ? d.thumbnail_url : '';
        thumbCache[wikiTitle] = url;
        if (active && url) setSrc(url);
      })
      .catch(() => {});
    return () => { active = false; };
  }, [wikiTitle]);
  return src;
}

const wikiUrl = (title) => `https://en.wikipedia.org/wiki/${encodeURIComponent(title.replace(/ /g, '_'))}`;

export function FormulaList({ formulas }) {
  if (!formulas?.length) return null;
  return (
    <ul className="grid gap-2" aria-label="Formulas and equations">
      {formulas.map((f) => (
        <li key={f.label + f.expr} className="rounded-lg border bg-white p-3 dark:border-gray-700 dark:bg-gray-900">
          <p className="text-sm font-semibold">{f.label}</p>
          <p className="mt-1 overflow-x-auto whitespace-pre-wrap font-mono text-base" data-testid="formula">{f.expr}</p>
          {f.note && <p className="mt-1 text-xs text-gray-600 dark:text-gray-400">{f.note}</p>}
        </li>
      ))}
    </ul>
  );
}

export function DataTables({ tables }) {
  if (!tables?.length) return null;
  return tables.map((t) => (
    <div key={t.title} className="overflow-x-auto">
      <table className="w-full border-collapse text-sm">
        <caption className="mb-1 text-left font-semibold">{t.title}</caption>
        <thead>
          <tr>{t.headers.map((h, i) => <th key={i} className="border bg-gray-100 p-2 text-left dark:border-gray-700 dark:bg-gray-800">{h}</th>)}</tr>
        </thead>
        <tbody>
          {t.rows.map((row, r) => <tr key={r}>{row.map((cell, c) => <td key={c} className="border p-2 dark:border-gray-700">{cell}</td>)}</tr>)}
        </tbody>
      </table>
    </div>
  ));
}

function CaseStudy({ item }) {
  const src = useThumbnail(item.wiki);
  return (
    <li className="flex flex-col gap-3 rounded-lg border bg-white p-3 dark:border-gray-700 dark:bg-gray-900 sm:flex-row">
      {src && (
        <div className="shrink-0 sm:w-40">
          <img src={src} alt={item.title} loading="lazy" className="h-28 w-full rounded object-cover sm:w-40" />
          <ImageCredit src={src} />
        </div>
      )}
      <div className="min-w-0">
        <h6 className="font-semibold">{item.title} <span className="text-xs font-normal text-gray-500">· {item.when}</span></h6>
        <p className="mt-1 text-sm">{item.summary}</p>
        <p className="mt-1 text-sm"><span className="font-semibold">Takeaway:</span> {item.takeaway}</p>
        {item.wiki && (
          <a href={wikiUrl(item.wiki)} target="_blank" rel="noopener noreferrer" className="mt-1 inline-block text-xs text-blue-600 underline">
            Read more on Wikipedia
          </a>
        )}
      </div>
    </li>
  );
}

export function CaseStudies({ cases }) {
  if (!cases?.length) return null;
  return <ul className="grid gap-3" aria-label="Case studies and real events">{cases.map((c) => <CaseStudy key={c.title} item={c} />)}</ul>;
}

function RelatedArticle({ wikiTitle, query }) {
  const [state, setState] = useState({ status: 'loading' });
  useEffect(() => {
    let active = true;
    setState({ status: 'loading' });
    getRelatedArticle({ title: wikiTitle, query })
      .then((a) => { if (active) setState(a?.available ? { status: 'ready', article: a } : { status: 'none' }); })
      .catch(() => { if (active) setState({ status: 'none' }); });
    return () => { active = false; };
  }, [wikiTitle, query]);

  if (state.status !== 'ready' || !state.article.extract) return null;
  const a = state.article;
  return (
    <section className="rounded-xl border bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-800" aria-label="Related article">
      <h5 className="font-semibold">Background</h5>
      <div className="mt-2 min-w-0">
        <p className="font-semibold">{a.title}{a.description ? <span className="font-normal text-gray-600 dark:text-gray-400"> — {a.description}</span> : null}</p>
        <p className="mt-1 text-sm">{a.extract}</p>
        <p className="mt-2 text-xs text-gray-600 dark:text-gray-400">
          From the closest matching Wikipedia article (found automatically, so check it fits your lesson) ·{' '}
          <a href={a.page_url} target="_blank" rel="noopener noreferrer" className="underline">Read the full article</a>{' '}
          · Text under CC BY-SA
        </p>
      </div>
    </section>
  );
}

export default function LessonEnrichment({ lessonId, levelId }) {
  const [state, setState] = useState({ status: 'loading' });
  const enabled = isEnrichedLevel(levelId) && !!lessonId;

  useEffect(() => {
    if (!enabled) return undefined;
    let active = true;
    setState({ status: 'loading' });
    getLessonEnrichment(levelId, lessonId)
      .then((data) => { if (active) setState({ status: 'ready', data }); })
      .catch(() => { if (active) setState({ status: 'error' }); });
    return () => { active = false; };
  }, [enabled, levelId, lessonId]);

  if (!enabled || state.status === 'error') return null;
  if (state.status === 'loading') return <p className="mt-4 text-sm text-gray-500" role="status">Loading enrichment…</p>;

  const { topic, subject_pack: pack, subject, query, wiki_title: wikiTitle } = state.data;
  const hasTopic = topic.formulas.length || topic.charts.length || topic.tables.length || topic.cases.length;
  return (
    <section className="mt-6 space-y-5" aria-label="Lesson enrichment">
      <h5 className="text-lg font-semibold">Enrich this lesson</h5>
      <RelatedArticle wikiTitle={wikiTitle} query={query} />
      {hasTopic ? (
        <div className="space-y-3">
          <h5 className="font-semibold">On this topic</h5>
          <FormulaList formulas={topic.formulas} />
          {topic.charts.map((chart) => (
            <Suspense key={chart.title} fallback={<p className="text-sm text-gray-500">Loading chart…</p>}>
              <LessonChart chart={chart} />
            </Suspense>
          ))}
          <DataTables tables={topic.tables} />
          <CaseStudies cases={topic.cases} />
        </div>
      ) : null}
      <details open className="rounded-xl border p-4 dark:border-gray-700">
        <summary className="cursor-pointer font-semibold">{subject} reference sheet — key data and landmark cases</summary>
        <div className="mt-3 space-y-3">
          <DataTables tables={pack.tables} />
          <CaseStudies cases={pack.cases} />
        </div>
      </details>
    </section>
  );
}
