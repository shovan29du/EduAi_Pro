import React from 'react';
import {
  ResponsiveContainer, LineChart, Line, BarChart, Bar, ComposedChart, Scatter, XAxis, YAxis,
  CartesianGrid, Tooltip, Legend,
} from 'recharts';

const COLORS = ['#2563eb', '#dc2626', '#16a34a', '#d97706', '#7c3aed', '#0891b2'];
const compact = new Intl.NumberFormat('en', { notation: 'compact', maximumFractionDigits: 1 });

// Start at zero unless every value sits in a narrow band (e.g. CO2 from 317 to 421), where zero hides the trend.
function yDomain(chart) {
  if (chart.log) return ['auto', 'auto'];
  const values = chart.data.flatMap((r) => [...chart.series, ...(chart.lines || [])].map((s) => r[s])).filter((v) => typeof v === 'number');
  const min = Math.min(...values);
  const max = Math.max(...values);
  return chart.kind !== 'bar' && min > 0 && min > 0.5 * max ? ['auto', 'auto'] : [0, 'auto'];
}

function seriesPoints(rows, key) {
  return rows.filter((r) => r[key] != null).map((r) => ({ x: r.x, y: r[key] }));
}

// ResponsiveContainer must receive the recharts chart element itself, not a wrapper component.
function buildChart(chart) {
  const { kind, data, series, lines = [], log, x_label: xLabel, y_label: yLabel } = chart;
  const common = { margin: { top: 8, right: 16, bottom: 28, left: 8 } };
  const axes = [
    <CartesianGrid key="g" strokeDasharray="3 3" />,
    <XAxis key="x" dataKey="x" type={kind === 'bar' ? 'category' : 'number'} domain={['dataMin', 'dataMax']} label={{ value: xLabel, position: 'insideBottom', offset: -14 }} />,
    <YAxis key="y" type="number" scale={log ? 'log' : 'auto'} domain={yDomain(chart)} width={76} tickFormatter={(v) => (Math.abs(v) >= 10000 ? compact.format(v) : v)} label={{ value: yLabel, angle: -90, position: 'insideLeft', offset: -2, style: { textAnchor: 'middle' } }} />,
    <Tooltip key="t" />,
    <Legend key="l" verticalAlign="top" />,
  ];
  if (kind === 'bar') {
    return (
      <BarChart data={data} {...common}>
        {axes}
        {series.map((s, i) => <Bar key={s} dataKey={s} fill={COLORS[i % COLORS.length]} />)}
      </BarChart>
    );
  }
  if (kind === 'scatter') {
    return (
      <ComposedChart {...common}>
        {axes}
        {series.map((s, i) => <Scatter key={s} name={s} data={seriesPoints(data, s)} dataKey="y" fill={COLORS[i % COLORS.length]} />)}
        {lines.map((s, i) => <Line key={s} name={s} data={seriesPoints(data, s)} dataKey="y" stroke={COLORS[(i + 1) % COLORS.length]} dot={false} isAnimationActive={false} />)}
      </ComposedChart>
    );
  }
  return (
    <LineChart data={data} {...common}>
      {axes}
      {series.map((s, i) => <Line key={s} type="monotone" dataKey={s} stroke={COLORS[i % COLORS.length]} dot={data.length <= 12} strokeWidth={2} isAnimationActive={false} connectNulls />)}
    </LineChart>
  );
}

export default function LessonChart({ chart }) {
  const columns = ['x', ...chart.series, ...(chart.lines || [])];
  const rows = chart.data;
  return (
    <figure className="rounded-xl border bg-white p-3 dark:border-gray-700 dark:bg-gray-900">
      <figcaption className="mb-2 font-semibold">{chart.title}</figcaption>
      <div role="img" aria-label={`${chart.title}. ${chart.note || ''}`} className="h-72 w-full">
        <ResponsiveContainer width="100%" height="100%">
          {buildChart(chart)}
        </ResponsiveContainer>
      </div>
      {chart.note && <p className="mt-2 text-xs text-gray-600 dark:text-gray-400">{chart.note}</p>}
      <details className="mt-2 text-sm">
        <summary className="cursor-pointer text-blue-600">View the data as a table</summary>
        <div className="mt-2 max-h-56 overflow-auto">
          <table className="w-full border-collapse text-xs">
            <thead>
              <tr>{columns.map((c) => <th key={c} className="border bg-gray-100 p-1 text-left dark:border-gray-700 dark:bg-gray-800">{c === 'x' ? chart.x_label : c}</th>)}</tr>
            </thead>
            <tbody>
              {rows.map((row, i) => (
                <tr key={i}>{columns.map((c) => <td key={c} className="border p-1 dark:border-gray-700">{row[c] ?? ''}</td>)}</tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </figure>
  );
}
