import React, { useEffect, useMemo, useRef, useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { EditorView } from '@codemirror/view';
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { cpp } from '@codemirror/lang-cpp';
import { java } from '@codemirror/lang-java';
import { php } from '@codemirror/lang-php';
import { rust } from '@codemirror/lang-rust';
import { sql } from '@codemirror/lang-sql';
import { StreamLanguage } from '@codemirror/language';
import { ruby } from '@codemirror/legacy-modes/mode/ruby';
import { perl } from '@codemirror/legacy-modes/mode/perl';
import { r as rStreamMode } from '@codemirror/legacy-modes/mode/r';
import { fortran } from '@codemirror/legacy-modes/mode/fortran';
import { csharp } from '@codemirror/legacy-modes/mode/clike';
import { go as goStreamMode } from '@codemirror/legacy-modes/mode/go';
import { oneDark } from '@codemirror/theme-one-dark';
import { useChild } from '../contexts/ChildContext.jsx';
import { fetchProgress, postProgress, deleteSnippet } from '../api/progress.js';

const PYODIDE_CDN = 'https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js';

let pyodidePromise = null;
function loadPyodide() {
  if (pyodidePromise) return pyodidePromise;
  pyodidePromise = new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = PYODIDE_CDN;
    script.onload = async () => {
      try { resolve(await window.loadPyodide()); }
      catch (err) { reject(err); }
    };
    script.onerror = () => reject(new Error('Could not load the Python runtime. Check your internet connection.'));
    document.body.appendChild(script);
  });
  return pyodidePromise;
}

function buildSandboxDoc(code) {
  const escaped = JSON.stringify(code);
  return `<!doctype html><html><body><script>
    const log = [];
    const origLog = console.log;
    console.log = (...args) => { log.push(args.join(' ')); origLog(...args); };
    try { eval(${escaped}); } catch (err) { log.push('Error: ' + err.message); }
    parent.postMessage({ type: 'code-output', output: log.join('\\n') }, '*');
  </script></body></html>`;
}

const LANGUAGES = [
  { id: 'javascript', label: 'JavaScript', mode: 'browser' },
  { id: 'typescript', label: 'TypeScript', mode: 'typescript' },
  { id: 'python',     label: 'Python',     mode: 'pyodide' },
  { id: 'java',       label: 'Java',       mode: 'backend' },
  { id: 'c',          label: 'C',          mode: 'backend' },
  { id: 'cpp',        label: 'C++',        mode: 'backend' },
  { id: 'csharp',     label: 'C#',         mode: 'backend' },
  { id: 'go',         label: 'Go',         mode: 'backend' },
  { id: 'rust',       label: 'Rust',       mode: 'backend' },
  { id: 'php',        label: 'PHP',        mode: 'backend' },
  { id: 'ruby',       label: 'Ruby',       mode: 'backend' },
  { id: 'perl',       label: 'Perl',       mode: 'backend' },
  { id: 'r',          label: 'R',          mode: 'backend' },
  { id: 'fortran',    label: 'Fortran',    mode: 'backend' },
  { id: 'sql',        label: 'SQL',        mode: 'backend' },
];

const DEFAULT_CODE = {
  javascript: '// JavaScript\nconsole.log("Hello, world!");',
  typescript: '// TypeScript\nfunction greet(name: string): string {\n  return `Hello, ${name}!`;\n}\nconsole.log(greet("world"));',
  python:     '# Python\nprint("Hello, world!")',
  java: `// Java (must declare "public class Main")
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello from Java!");
    }
}`,
  c: `// C
#include <stdio.h>

int main() {
    printf("Hello from C!\\n");
    return 0;
}`,
  cpp: `// C++
#include <iostream>
using namespace std;

int main() {
    cout << "Hello from C++!" << endl;
    return 0;
}`,
  csharp: `// C#
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello from C#!");
    }
}`,
  go: `// Go
package main

import "fmt"

func main() {
    fmt.Println("Hello from Go!")
}`,
  rust: `// Rust
fn main() {
    println!("Hello from Rust!");
}`,
  php: `<?php
// PHP
echo "Hello from PHP!\\n";`,
  ruby: `# Ruby
puts "Hello from Ruby!"`,
  perl: `# Perl
print "Hello from Perl!\\n";`,
  r: `# R
cat("Hello from R!\\n")`,
  fortran: `! Fortran
program hello
  print *, "Hello from Fortran!"
end program hello`,
  sql: `-- SQL (SQLite)
CREATE TABLE students (id INTEGER, name TEXT, grade INTEGER);
INSERT INTO students VALUES (1, 'Alice', 90);
INSERT INTO students VALUES (2, 'Bob',   85);
SELECT name, grade FROM students WHERE grade >= 88;`,
};

const BACKEND_HINTS = {
  java: 'Compiled with javac and run with java on the server.',
  c: 'Compiled with gcc on the server.',
  cpp: 'Compiled with g++ (C++17) on the server.',
  csharp: 'Compiled with mcs and run with mono on the server.',
  go: 'Run with "go run" on the server.',
  rust: 'Compiled with rustc on the server.',
  php: 'Run with the PHP CLI on the server.',
  ruby: 'Run with the Ruby interpreter on the server.',
  perl: 'Run with the Perl interpreter on the server.',
  r: 'Run with Rscript on the server.',
  fortran: 'Compiled with gfortran on the server.',
};

// A one-line "why would I use this?" for a student picking a language for the first time.
const STARTER_BLURBS = {
  javascript: 'The language of the web — runs in every browser, great for interactive pages.',
  typescript: 'JavaScript with type-checking bolted on, so many mistakes get caught before you run the code.',
  python: 'Reads almost like English. A great first "real" programming language.',
  java: 'Verbose but structured — widely taught in schools and used in big, long-lived systems (and Android apps).',
  c: 'Close to the hardware. Understanding C teaches you how memory and computers actually work.',
  cpp: "C with extra features (objects, generics). Used for games, browsers, and anything needing raw speed.",
  csharp: 'Microsoft\'s answer to Java — common in Windows apps and the Unity game engine.',
  go: 'Designed at Google to be simple and fast to compile. Popular for servers and command-line tools.',
  rust: 'Like C++ but the compiler stops you from a whole class of memory bugs before the program even runs.',
  php: 'Built for the web — still powers a huge share of websites (including WordPress).',
  ruby: 'Designed to be pleasant to write. Powers the Rails web framework.',
  perl: 'A veteran text-processing language — famous for regular expressions and quick scripts.',
  r: "The standard language for statistics, data analysis, and plotting in science and research.",
  fortran: 'One of the oldest languages, still used today for heavy-duty scientific and numerical computing.',
  sql: 'Not a general-purpose language — it\'s how you ask a database questions ("SELECT... WHERE...").',
};

const LANG_EXTENSIONS = {
  javascript: () => javascript({ jsx: false, typescript: false }),
  typescript: () => javascript({ jsx: false, typescript: true }),
  python: () => python(),
  java: () => java(),
  c: () => cpp(),
  cpp: () => cpp(),
  csharp: () => StreamLanguage.define(csharp),
  go: () => StreamLanguage.define(goStreamMode),
  rust: () => rust(),
  php: () => php(),
  ruby: () => StreamLanguage.define(ruby),
  perl: () => StreamLanguage.define(perl),
  r: () => StreamLanguage.define(rStreamMode),
  fortran: () => StreamLanguage.define(fortran),
  sql: () => sql(),
};

const MAX_RUN_HISTORY = 5;

function snippetSavedAt(snippet, fallbackId) {
  const ts = snippet?.savedAt ?? Number(String(fallbackId).replace('snippet-', ''));
  return Number.isFinite(ts) ? new Date(ts) : null;
}

function snippetPreview(code) {
  const firstLine = (code || '').split('\n').find((l) => l.trim()) || '';
  return firstLine.length > 60 ? `${firstLine.slice(0, 60)}…` : firstLine;
}

// ── Saved-snippets browser ─────────────────────────────────────────────────

function SnippetBrowser({ child, open, onLoad }) {
  const [snippets, setSnippets] = useState(null);
  const [busyId, setBusyId] = useState(null);

  useEffect(() => {
    if (!open) return;
    fetchProgress(child)
      .then((p) => setSnippets(p.snippets || {}))
      .catch(() => setSnippets({}));
  }, [open, child]);

  async function handleDelete(id) {
    setBusyId(id);
    try {
      const result = await deleteSnippet(child, id);
      setSnippets(result.snippets || {});
    } catch {
      // leave the list as-is; the delete button remains available to retry
    } finally {
      setBusyId(null);
    }
  }

  if (!open) return null;

  const entries = Object.entries(snippets || {}).sort(([a], [b]) => (a < b ? 1 : -1));

  return (
    <div role="region" aria-label="Saved snippets" className="rounded-lg border p-3 dark:border-gray-600 space-y-2">
      {snippets === null && <p className="text-sm text-gray-500">Loading snippets…</p>}
      {snippets !== null && entries.length === 0 && (
        <p className="text-sm text-gray-500">No saved snippets yet — write some code and click "Save snippet".</p>
      )}
      {entries.map(([id, snippet]) => {
        const code = typeof snippet === 'string' ? snippet : snippet?.code || '';
        const lang = typeof snippet === 'object' ? snippet?.language : null;
        const langLabel = LANGUAGES.find((l) => l.id === lang)?.label;
        const savedAt = snippetSavedAt(snippet, id);
        return (
          <div key={id} className="flex items-center justify-between gap-2 rounded border px-2 py-1.5 dark:border-gray-700">
            <button
              type="button"
              onClick={() => onLoad({ id, code, language: lang })}
              className="flex-1 min-w-0 text-left"
            >
              <span className="block truncate font-mono text-xs text-gray-700 dark:text-gray-300">
                {snippetPreview(code) || '(empty)'}
              </span>
              <span className="text-[11px] text-gray-400">
                {langLabel ? `${langLabel} · ` : ''}{savedAt ? savedAt.toLocaleString() : id}
              </span>
            </button>
            <button
              type="button"
              onClick={() => handleDelete(id)}
              disabled={busyId === id}
              aria-label={`Delete snippet saved ${savedAt ? savedAt.toLocaleString() : id}`}
              className="rounded border px-2 py-1 text-xs text-red-600 hover:bg-red-50 disabled:opacity-50 dark:text-red-400 dark:hover:bg-red-950"
            >
              {busyId === id ? '…' : '🗑'}
            </button>
          </div>
        );
      })}
    </div>
  );
}

// ── Quine Museum ────────────────────────────────────────────────────────────
// A quine is a program that prints its own source code exactly. Real quines,
// one per language, from the open-source Quine Museum project.

function QuineBrowser({ open, onLoad }) {
  const [quines, setQuines] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!open || quines !== null) return;
    fetch('/api/quines')
      .then((r) => { if (!r.ok) throw new Error('fetch failed'); return r.json(); })
      .then((data) => setQuines(data.quines || []))
      .catch(() => setError('Could not load the Quine Museum.'));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [open]);

  if (!open) return null;

  return (
    <div role="region" aria-label="Quine Museum" className="rounded-lg border p-3 dark:border-gray-600 space-y-2">
      <p className="text-xs text-gray-500 dark:text-gray-400">
        A quine is a program that prints its own source code exactly. Load one, then press Run to watch it
        reproduce itself.
      </p>
      {error && <p className="text-sm text-red-600 dark:text-red-400">{error}</p>}
      {quines === null && !error && <p className="text-sm text-gray-500">Loading…</p>}
      {quines !== null && (
        <div className="flex flex-wrap gap-2">
          {quines.map((q) => (
            <button
              key={q.language}
              type="button"
              onClick={() => onLoad({ code: q.source, language: q.language })}
              className="rounded-full border px-3 py-1 text-xs font-medium hover:bg-gray-100 dark:border-gray-600 dark:hover:bg-gray-800"
            >
              {q.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default function CodeEditor({ defaultLanguage = 'javascript' }) {
  const { child, darkMode } = useChild();
  const [language, setLanguage] = useState(defaultLanguage);
  const [code, setCode] = useState(DEFAULT_CODE[defaultLanguage] || DEFAULT_CODE.javascript);
  const [output, setOutput] = useState('');
  const [saved, setSaved] = useState(false);
  const [running, setRunning] = useState(false);
  const [snippetsOpen, setSnippetsOpen] = useState(false);
  const [quinesOpen, setQuinesOpen] = useState(false);
  const [runHistory, setRunHistory] = useState([]); // [{code, output, language, at}], newest first
  const [viewingHistoryIdx, setViewingHistoryIdx] = useState(null);
  const iframeRef = useRef(null);
  const languageLabel = LANGUAGES.find(item => item.id === language)?.label || 'Programming';
  const editorExtensions = useMemo(() => {
    const build = LANG_EXTENSIONS[language];
    const langExt = build ? [build()] : [];
    return [
      ...langExt,
      EditorView.contentAttributes.of({ 'aria-label': `${languageLabel} code` }),
    ];
  }, [language, languageLabel]);

  function handleLanguageChange(lang) {
    setLanguage(lang);
    setOutput('');
    setCode(DEFAULT_CODE[lang] || '');
    setViewingHistoryIdx(null);
  }

  function recordRun(finalOutput) {
    setRunHistory((prev) => [
      { code, output: finalOutput, language, at: Date.now() },
      ...prev,
    ].slice(0, MAX_RUN_HISTORY));
    setViewingHistoryIdx(null);
  }

  function runJavaScript() {
    setOutput('');
    const handleMessage = (event) => {
      if (event.data?.type === 'code-output') {
        setOutput(event.data.output);
        recordRun(event.data.output);
        window.removeEventListener('message', handleMessage);
      }
    };
    window.addEventListener('message', handleMessage);
    if (iframeRef.current) {
      iframeRef.current.setAttribute('srcdoc', buildSandboxDoc(code));
    }
  }

  async function runTypeScript() {
    setOutput('');
    setRunning(true);
    try {
      const ts = await loadTypeScriptCompiler();
      const { outputText, diagnostics } = ts.transpileModule(code, {
        compilerOptions: { module: ts.ModuleKind.None, target: ts.ScriptTarget.ES2020 },
        reportDiagnostics: true,
      });
      if (diagnostics && diagnostics.length > 0) {
        const messages = diagnostics.map((d) => ts.flattenDiagnosticMessageText(d.messageText, '\n'));
        const errOutput = `Type error:\n${messages.join('\n')}`;
        setOutput(errOutput);
        recordRun(errOutput);
        setRunning(false);
        return;
      }
      const handleMessage = (event) => {
        if (event.data?.type === 'code-output') {
          setOutput(event.data.output);
          recordRun(event.data.output);
          window.removeEventListener('message', handleMessage);
          setRunning(false);
        }
      };
      window.addEventListener('message', handleMessage);
      if (iframeRef.current) iframeRef.current.setAttribute('srcdoc', buildSandboxDoc(outputText));
    } catch (err) {
      const errOutput = `Error: ${err.message}`;
      setOutput(errOutput);
      recordRun(errOutput);
      setRunning(false);
    }
  }

  async function runPython() {
    setOutput('');
    setRunning(true);
    try {
      const pyodide = await loadPyodide();
      let captured = '';
      pyodide.setStdout({ batched: (t) => { captured += t + '\n'; } });
      pyodide.setStderr({ batched: (t) => { captured += t + '\n'; } });
      try { await pyodide.runPythonAsync(code); }
      catch (err) { captured += `Error: ${err.message}`; }
      const finalOutput = captured.trim() || '(no output)';
      setOutput(finalOutput);
      recordRun(finalOutput);
    } catch (err) {
      const errOutput = `Error: ${err.message}`;
      setOutput(errOutput);
      recordRun(errOutput);
    } finally {
      setRunning(false);
    }
  }

  async function runBackend(lang) {
    setOutput('');
    setRunning(true);
    try {
      const r = await fetch('/api/run-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language: lang, code }),
      });
      const d = await r.json();
      const finalOutput = d.output || '(no output)';
      setOutput(finalOutput);
      recordRun(finalOutput);
    } catch (err) {
      const errOutput = `Error: ${err.message}`;
      setOutput(errOutput);
      recordRun(errOutput);
    } finally {
      setRunning(false);
    }
  }

  function handleRun() {
    setSaved(false);
    const mode = LANGUAGES.find(l => l.id === language)?.mode;
    if (mode === 'pyodide') runPython();
    else if (mode === 'backend') runBackend(language);
    else if (mode === 'typescript') runTypeScript();
    else runJavaScript();
  }

  async function handleSave() {
    await postProgress(child, {
      snippets: { [`snippet-${Date.now()}`]: { code, language, savedAt: Date.now() } },
    });
    setSaved(true);
  }

  function handleLoadSnippet({ code: loadedCode, language: loadedLanguage }) {
    if (loadedLanguage && LANGUAGES.some((l) => l.id === loadedLanguage)) {
      setLanguage(loadedLanguage);
    }
    setCode(loadedCode);
    setOutput('');
    setViewingHistoryIdx(null);
    setSnippetsOpen(false);
  }

  function handleLoadQuine({ code: loadedCode, language: loadedLanguage }) {
    if (loadedLanguage && LANGUAGES.some((l) => l.id === loadedLanguage)) {
      setLanguage(loadedLanguage);
    }
    setCode(loadedCode);
    setOutput('');
    setViewingHistoryIdx(null);
    setQuinesOpen(false);
  }

  const runLabel = running
    ? (language === 'python' ? 'Starting Python…' : 'Running…')
    : '▶ Run';

  const displayedOutput = viewingHistoryIdx === null ? output : runHistory[viewingHistoryIdx]?.output ?? '';

  return (
    <section aria-label="Code editor" className="rounded-xl border dark:border-gray-700 p-4 space-y-3">
      <h2 className="text-lg font-bold dark:text-white">Code Editor</h2>

      {/* Language selector */}
      <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Programming language">
        {LANGUAGES.map(({ id, label }) => (
          <button
            key={id}
            type="button"
            role="radio"
            aria-checked={language === id}
            onClick={() => handleLanguageChange(id)}
            className={`rounded-full border px-4 py-1 text-sm font-medium transition focus:outline focus:outline-2 focus:outline-blue-500 ${
              language === id
                ? 'bg-blue-600 text-white border-blue-600'
                : 'border-gray-300 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-800'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      {/* Starter blurb */}
      {STARTER_BLURBS[language] && (
        <p className="rounded-lg bg-blue-50 dark:bg-blue-950 text-blue-800 dark:text-blue-200 text-xs px-3 py-2">
          💡 {STARTER_BLURBS[language]}
        </p>
      )}

      {/* Hint for server-run languages */}
      {BACKEND_HINTS[language] && (
        <p className="text-xs text-gray-500 dark:text-gray-400">
          {BACKEND_HINTS[language]} Output appears after compilation.
        </p>
      )}
      {language === 'sql' && (
        <p className="text-xs text-gray-500 dark:text-gray-400">Runs against an in-memory SQLite database. Each Run starts fresh.</p>
      )}
      {language === 'typescript' && (
        <p className="text-xs text-gray-500 dark:text-gray-400">Type-checked and transpiled to JavaScript in your browser, then run in the same sandbox as JavaScript.</p>
      )}

      <div className="rounded-lg border overflow-hidden dark:border-gray-600 text-sm">
        <CodeMirror
          aria-label={`${languageLabel} code`}
          value={code}
          height="260px"
          theme={darkMode ? oneDark : 'light'}
          extensions={editorExtensions}
          onChange={(value) => setCode(value)}
          basicSetup={{ tabSize: 4 }}
        />
      </div>

      <div className="flex flex-wrap items-center gap-2">
        <button
          type="button"
          onClick={handleRun}
          disabled={running}
          className="rounded-lg bg-green-600 text-white px-4 py-1.5 text-sm font-semibold hover:bg-green-700 transition disabled:opacity-50 focus:outline focus:outline-2 focus:outline-blue-500"
        >
          {runLabel}
        </button>
        <button
          type="button"
          onClick={handleSave}
          className="rounded-lg border px-4 py-1.5 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 transition focus:outline focus:outline-2 focus:outline-blue-500"
        >
          Save snippet
        </button>
        <button
          type="button"
          onClick={() => setSnippetsOpen((v) => !v)}
          aria-expanded={snippetsOpen}
          className="rounded-lg border px-4 py-1.5 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 transition focus:outline focus:outline-2 focus:outline-blue-500"
        >
          {snippetsOpen ? '📂 Hide snippets' : '📂 My Snippets'}
        </button>
        <button
          type="button"
          onClick={() => setQuinesOpen((v) => !v)}
          aria-expanded={quinesOpen}
          className="rounded-lg border px-4 py-1.5 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 transition focus:outline focus:outline-2 focus:outline-blue-500"
        >
          {quinesOpen ? '🧬 Hide Quine Museum' : '🧬 Quine Museum'}
        </button>
        {saved && <span role="status" className="text-sm text-green-600 dark:text-green-400">Saved!</span>}
      </div>

      <SnippetBrowser child={child} open={snippetsOpen} onLoad={handleLoadSnippet} />
      <QuineBrowser open={quinesOpen} onLoad={handleLoadQuine} />

      <pre
        role="region"
        aria-label="Code output"
        className="min-h-[3rem] whitespace-pre-wrap rounded-lg border bg-gray-900 text-green-400 p-3 text-sm font-mono dark:border-gray-700"
      >
        {displayedOutput || <span className="text-gray-600">Output will appear here…</span>}
      </pre>

      {runHistory.length > 0 && (
        <div role="region" aria-label="Run history" className="space-y-1">
          <p className="text-xs font-semibold text-gray-500 dark:text-gray-400">
            Run history (click to compare against an earlier attempt):
          </p>
          <div className="flex flex-wrap gap-1">
            <button
              type="button"
              onClick={() => setViewingHistoryIdx(null)}
              className={`rounded-full border px-3 py-0.5 text-xs ${viewingHistoryIdx === null ? 'bg-gray-700 text-white border-gray-700 dark:bg-gray-200 dark:text-gray-900' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}`}
            >
              Latest
            </button>
            {runHistory.map((entry, i) => (
              <button
                key={entry.at}
                type="button"
                onClick={() => setViewingHistoryIdx(i)}
                className={`rounded-full border px-3 py-0.5 text-xs ${viewingHistoryIdx === i ? 'bg-gray-700 text-white border-gray-700 dark:bg-gray-200 dark:text-gray-900' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}`}
              >
                {new Date(entry.at).toLocaleTimeString()}
              </button>
            ))}
          </div>
        </div>
      )}

      <iframe ref={iframeRef} title="code-sandbox" sandbox="allow-scripts" className="hidden" />
    </section>
  );
}

const TS_CDN = 'https://cdn.jsdelivr.net/npm/typescript@5.4.5/lib/typescript.js';

let tsPromise = null;
function loadTypeScriptCompiler() {
  if (tsPromise) return tsPromise;
  tsPromise = new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = TS_CDN;
    script.onload = () => resolve(window.ts);
    script.onerror = () => reject(new Error('Could not load the TypeScript compiler. Check your internet connection.'));
    document.body.appendChild(script);
  });
  return tsPromise;
}
