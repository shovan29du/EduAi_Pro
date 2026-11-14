import React, { useEffect, useState } from 'react';

const creditCache = {};

export default function ImageCredit({ src }) {
  const [credit, setCredit] = useState(creditCache[src] || null);

  useEffect(() => {
    // Placeholders (local SVGs) have nothing to credit.
    if (!/^https?:/.test(src || '')) { setCredit(null); return undefined; }
    if (creditCache[src]) { setCredit(creditCache[src]); return undefined; }
    let active = true;
    fetch(`/api/museum/credit?image=${encodeURIComponent(src)}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (data?.known) creditCache[src] = data;
        if (active) setCredit(data?.known ? data : null);
      })
      .catch(() => { if (active) setCredit(null); });
    return () => { active = false; };
  }, [src]);

  if (!credit) return null;
  return (
    <p className="-mt-2 mb-4 text-xs text-gray-500 dark:text-gray-400" data-testid="image-credit">
      Photo{credit.line ? `: ${credit.artist ? credit.artist : credit.line.split(' · ')[0]}` : ''}
      {credit.license && (
        <>
          {' · '}
          {credit.license_url
            ? <a href={credit.license_url} target="_blank" rel="noopener noreferrer" className="underline">{credit.license}</a>
            : credit.license}
        </>
      )}
      {credit.source_url && (
        <>
          {' · '}
          <a href={credit.source_url} target="_blank" rel="noopener noreferrer" className="underline">Source</a>
        </>
      )}
    </p>
  );
}
