import React, { useRef, useState } from 'react';
import { useChild } from '../contexts/ChildContext.jsx';
import { postProgress } from '../api/progress.js';

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

export default function CodeEditor({ defaultLanguage = 'javascript' }) {
  const { child } = useChild();
  const [language, setLanguage] = useState(defaultLanguage);
  const [code, setCode] = useState(DEFAULT_CODE[defaultLanguage] || DEFAULT_CODE.javascript);
  const [output, setOutput] = useState('');
  const [saved, setSaved] = useState(false);
  const [running, setRunning] = useState(false);
  const iframeRef = useRef(null);
  const languageLabel = LANGUAGES.find(item => item.id === language)?.label || 'Programming';

  function handleLanguageChange(lang) {
    setLanguage(lang);
    setOutput('');
    setCode(DEFAULT_CODE[lang] || '');
  }

  function runJavaScript() {
    setOutput('');
    const handleMessage = (event) => {
      if (event.data?.type === 'code-output') {
        setOutput(event.data.output);
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
        setOutput(`Type error:\n${messages.join('\n')}`);
        setRunning(false);
        return;
      }
      const handleMessage = (event) => {
        if (event.data?.type === 'code-output') {
          setOutput(event.data.output);
          window.removeEventListener('message', handleMessage);
          setRunning(false);
        }
      };
      window.addEventListener('message', handleMessage);
      if (iframeRef.current) iframeRef.current.setAttribute('srcdoc', buildSandboxDoc(outputText));
    } catch (err) {
      setOutput(`Error: ${err.message}`);
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
      setOutput(captured.trim() || '(no output)');
    } catch (err) {
      setOutput(`Error: ${err.message}`);
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
      setOutput(d.output || '(no output)');
    } catch (err) {
      setOutput(`Error: ${err.message}`);
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
    await postProgress(child, { snippets: { [`snippet-${Date.now()}`]: code } });
    setSaved(true);
  }

  const runLabel = running
    ? (language === 'python' ? 'Starting Python…' : 'Running…')
    : '▶ Run';

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

      <label className="sr-only" htmlFor="code-editor-textarea">{languageLabel} code</label>
      <textarea
        id="code-editor-textarea"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        rows={10}
        spellCheck={false}
        className="w-full rounded-lg border p-3 font-mono text-sm focus:outline focus:outline-2 focus:outline-blue-500 dark:bg-gray-800 dark:text-white dark:border-gray-600"
      />

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
        {saved && <span role="status" className="text-sm text-green-600 dark:text-green-400">Saved!</span>}
      </div>

      <pre
        role="region"
        aria-label="Code output"
        className="min-h-[3rem] whitespace-pre-wrap rounded-lg border bg-gray-900 text-green-400 p-3 text-sm font-mono dark:border-gray-700"
      >
        {output || <span className="text-gray-600">Output will appear here…</span>}
      </pre>

      <iframe ref={iframeRef} title="code-sandbox" sandbox="allow-scripts" className="hidden" />
    </section>
  );
}
