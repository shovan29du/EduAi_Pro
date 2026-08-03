import { useEffect, useState } from 'react';
import LevelSelector from './LevelSelector.jsx';
import {
  askCourseAssistant,
  deleteResourceTabDocument,
  listCourseProviders,
  listLocalLibrary,
  listResourceTabDocuments,
  resourceTabDownloadUrl,
  scanLocalLibrary,
  selectLocalLibraryFolder,
  uploadResourceTabDocument,
} from '../api/resourceTab.js';

export default function ResourceTab() {
  const [documents, setDocuments] = useState([]);
  const [providers, setProviders] = useState([]);
  const [localFiles, setLocalFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [courseQuery, setCourseQuery] = useState('');
  const [providerCategory, setProviderCategory] = useState('');
  const [folder, setFolder] = useState('');
  const [scanning, setScanning] = useState(false);
  const [selectingFolder, setSelectingFolder] = useState(false);
  const [scanMessage, setScanMessage] = useState('');
  const [localCategory, setLocalCategory] = useState('');
  const [localQuery, setLocalQuery] = useState('');
  const [selectedDocIds, setSelectedDocIds] = useState([]);
  const [courseLevel, setCourseLevel] = useState('1');
  const [courseQuestion, setCourseQuestion] = useState('');
  const [courseAnswer, setCourseAnswer] = useState(null);
  const [courseAsking, setCourseAsking] = useState(false);
  const [courseError, setCourseError] = useState('');

  function toggleDocSelected(id) {
    setSelectedDocIds((prev) => (prev.includes(id) ? prev.filter((d) => d !== id) : [...prev, id]));
  }

  async function handleAskCourseAssistant(event) {
    event.preventDefault();
    if (!selectedDocIds.length || !courseQuestion.trim()) return;
    setCourseAsking(true);
    setCourseError('');
    setCourseAnswer(null);
    try {
      const data = await askCourseAssistant(selectedDocIds, courseQuestion.trim(), { level: courseLevel });
      setCourseAnswer(data);
    } catch (err) {
      setCourseError(err.message);
    } finally {
      setCourseAsking(false);
    }
  }

  function refreshDocuments() {
    setLoading(true);
    listResourceTabDocuments()
      .then(setDocuments)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }

  useEffect(() => {
    refreshDocuments();
    listCourseProviders().then((data) => setProviders(data.providers)).catch(() => {});
    listLocalLibrary().then((data) => setLocalFiles(data.files)).catch(() => {});
  }, []);

  async function searchCourses(event) {
    event.preventDefault();
    setError(null);
    try {
      const data = await listCourseProviders(courseQuery);
      setProviders(data.providers);
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleFolderScan(event) {
    event.preventDefault();
    if (!folder.trim()) {
      setError('Choose a folder or paste its full path before scanning.');
      return;
    }
    setScanning(true);
    setError(null);
    setScanMessage('');
    try {
      const result = await scanLocalLibrary(folder.trim(), true);
      setFolder(result.root || folder.trim());
      setLocalFiles(Array.isArray(result.files) ? result.files : []);
      const details = result.indexed === 0
        ? 'Scan completed, but no supported books, videos, audio, or pictures were found.'
        : `Indexed ${result.indexed} files in place; analysed ${result.books_analysed} owned books; Ark AI categorised ${result.ai_analysed || 0} new or changed books, audio, and video files.`;
      const skipped = result.skipped ? ` Skipped ${result.skipped} unreadable or unsupported item${result.skipped === 1 ? '' : 's'}.` : '';
      const truncated = result.truncated ? ' The file limit was reached; narrow the folder and scan again for the remaining files.' : '';
      const truncatedAi = result.truncated_ai ? ' Ark AI categorisation stopped early for this scan; rescan to continue where it left off.' : '';
      setScanMessage(`${details}${skipped}${truncated}${truncatedAi}`);
    } catch (err) {
      setError(err.message);
    } finally {
      setScanning(false);
    }
  }

  async function chooseFolder() {
    setSelectingFolder(true);
    setError(null);
    try {
      const result = await selectLocalLibraryFolder();
      if (result.folder) {
        setFolder(result.folder);
        setScanMessage('Folder selected. Press “Scan folder” to index its supported files.');
      } else if (result.cancelled) {
        setScanMessage('Folder selection cancelled. No files were changed.');
      }
    } catch (err) {
      setError(`${err.message}. You can still paste the folder location.`);
    } finally {
      setSelectingFolder(false);
    }
  }

  async function filterLocalFiles(category = localCategory, query = localQuery) {
    setError(null);
    try {
      const data = await listLocalLibrary(category, query);
      setLocalFiles(data.files);
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleUpload(event) {
    const file = event.target.files?.[0];
    event.target.value = '';
    if (!file) return;
    setUploading(true);
    setError(null);
    try {
      await uploadResourceTabDocument(file);
      refreshDocuments();
    } catch (err) {
      setError(err.message);
    } finally {
      setUploading(false);
    }
  }

  async function handleDelete(id) {
    setError(null);
    try {
      await deleteResourceTabDocument(id);
      setDocuments((items) => items.filter((item) => item.id !== id));
      setSelectedDocIds((ids) => ids.filter((docId) => docId !== id));
    } catch (err) {
      setError(err.message);
    }
  }

  function formatBytes(value) {
    if (value < 1024) return `${value} B`;
    if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`;
    return `${(value / (1024 * 1024)).toFixed(1)} MB`;
  }

  return (
    <section aria-label="Learning Resources" className="space-y-6 rounded border p-4 dark:border-gray-700">
      <div>
        <h2 className="text-xl font-bold">Learning Resources</h2>
        <p className="mt-1 text-sm text-gray-600 dark:text-gray-300">
          Search course providers, index owned files without copying them, or upload a document.
        </p>
      </div>

      {error && <p role="alert" className="rounded bg-red-50 p-3 text-red-700">{error}</p>}

      <div className="rounded-xl border p-4 dark:border-gray-700">
        <h3 className="font-semibold">Open libraries, multimedia and courses</h3>
        <p className="mt-1 text-sm text-gray-600 dark:text-gray-300">
          Search {providers.length || 'dozens of'} open libraries, media networks, news portals,
          museum collections, archives and course platforms. Each source states whether access
          is open, public domain, CC0, borrowing, mixed, government, or simply free to view.
        </p>
        <form onSubmit={searchCourses} className="mt-3 flex gap-2">
          <input
            value={courseQuery}
            onChange={(event) => setCourseQuery(event.target.value)}
            placeholder="Subject, skill, or course"
            className="min-w-0 flex-1 rounded border px-3 py-2 dark:border-gray-600 dark:bg-gray-900"
          />
          <button className="rounded bg-blue-600 px-4 py-2 text-white">Search sources</button>
        </form>
        <div className="mt-3 flex flex-wrap gap-2" role="group" aria-label="Open source category">
          {[
            ['', 'All'],
            ['books', 'Books'],
            ['audio', 'Audiobooks'],
            ['multimedia', 'Open media'],
            ['media-server', 'Media servers'],
            ['news', 'Open news'],
            ['museum', 'Open museums'],
            ['culture', 'Museums & archives'],
            ['courses', 'Courses'],
            ['video', 'Video'],
          ].map(([value, label]) => (
            <button
              key={value || 'all'}
              type="button"
              onClick={() => setProviderCategory(value)}
              aria-pressed={providerCategory === value}
              className={`rounded-full border px-3 py-1 text-xs ${
                providerCategory === value
                  ? 'border-blue-700 bg-blue-700 text-white'
                  : 'border-gray-300 dark:border-gray-600'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
        <div className="mt-3 grid gap-3 sm:grid-cols-2">
          {providers.filter((provider) => !providerCategory || provider.category === providerCategory).map((provider) => (
            <a
              key={provider.id}
              href={provider.search_url || provider.url}
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg border p-3 hover:border-blue-400 hover:bg-blue-50 dark:border-gray-700 dark:hover:bg-gray-800"
            >
              <span className="flex items-start justify-between gap-2">
                <span className="font-medium text-blue-700 dark:text-blue-300">{provider.name}</span>
                <span className="rounded bg-gray-100 px-2 py-0.5 text-[10px] font-semibold uppercase text-gray-600 dark:bg-gray-800 dark:text-gray-300">
                  {provider.kind}
                </span>
              </span>
              <span className="mt-1 block text-xs text-gray-600 dark:text-gray-400">{provider.access}</span>
            </a>
          ))}
        </div>
      </div>

      <div className="rounded-xl border p-4 dark:border-gray-700">
        <h3 className="font-semibold">Local owned-content library</h3>
        <p className="mt-1 text-sm text-gray-600 dark:text-gray-300">
          Enter a folder on the computer running EduAI_Pro. Books, video, audio and pictures
          remain there; only their paths and learning metadata are indexed. PDF, DOCX, EPUB
          and TXT books are analysed locally and matched to Level 1–M2 topics.
        </p>
        <form onSubmit={handleFolderScan} className="mt-3 flex flex-col gap-2 sm:flex-row">
          <input
            value={folder}
            onChange={(event) => {
              setFolder(event.target.value);
              setScanMessage('');
            }}
            placeholder={'Example: C:\\Books or /home/me/Learning'}
            aria-label="Folder to scan"
            disabled={scanning || selectingFolder}
            className="min-w-0 flex-1 rounded border px-3 py-2 dark:border-gray-600 dark:bg-gray-900"
          />
          <button
            type="button"
            onClick={chooseFolder}
            disabled={selectingFolder || scanning}
            className="rounded border border-emerald-600 px-4 py-2 font-medium text-emerald-700 disabled:opacity-60 dark:text-emerald-300"
          >
            {selectingFolder ? 'Opening…' : 'Choose folder'}
          </button>
          <button
            type="submit"
            disabled={scanning || selectingFolder || !folder.trim()}
            className="rounded bg-emerald-600 px-4 py-2 text-white disabled:opacity-60"
          >
            {scanning ? 'Scanning and analysing…' : 'Scan folder'}
          </button>
        </form>
        {scanMessage && <p className="mt-2 text-sm text-emerald-700 dark:text-emerald-300">{scanMessage}</p>}

        <div className="mt-4 flex flex-wrap gap-2">
          {['', 'books', 'videos', 'audio', 'pictures'].map((category) => (
            <button
              key={category || 'all'}
              type="button"
              onClick={() => {
                setLocalCategory(category);
                filterLocalFiles(category, localQuery);
              }}
              className={`rounded-full border px-3 py-1 text-sm ${
                localCategory === category ? 'bg-gray-900 text-white dark:bg-white dark:text-gray-900' : ''
              }`}
            >
              {category || 'all'}
            </button>
          ))}
          <input
            value={localQuery}
            onChange={(event) => setLocalQuery(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === 'Enter') {
                event.preventDefault();
                filterLocalFiles();
              }
            }}
            placeholder="Filter filenames"
            className="rounded border px-3 py-1 text-sm dark:border-gray-600 dark:bg-gray-900"
          />
        </div>

        {localFiles.length === 0 ? (
          <p className="mt-3 text-sm text-gray-500">No local files indexed yet.</p>
        ) : (
          <ul className="mt-3 max-h-[36rem] space-y-3 overflow-auto">
            {localFiles.map((file) => (
              <li key={file.id} className="rounded-lg border p-3 dark:border-gray-700">
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div className="min-w-0">
                    <a
                      href={file.open_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="break-all font-medium text-blue-600 underline dark:text-blue-400"
                    >
                      {file.ai_title || file.filename}
                    </a>
                    {file.ai_title && <p className="break-all text-xs text-gray-400">{file.filename}</p>}
                    <p className="break-all text-xs text-gray-500">{file.path}</p>
                  </div>
                  <div className="flex flex-wrap justify-end gap-1">
                    <span className="rounded bg-gray-100 px-2 py-1 text-xs uppercase dark:bg-gray-800">
                      {file.category} · {formatBytes(file.size)}
                    </span>
                    {(file.ai_kind || file.ai_genre) && (
                      <span
                        className="rounded bg-emerald-100 px-2 py-1 text-xs text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200"
                        title="Ark AI's best guess from the filename -- it hasn't seen or heard the actual content"
                      >
                        ✨ {[file.ai_kind, file.ai_genre].filter(Boolean).join(' · ')}
                      </span>
                    )}
                  </div>
                </div>
                {file.summary && <p className="mt-2 line-clamp-3 text-sm">{file.summary}</p>}
                {file.matched_topics?.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-1">
                    {file.matched_topics.slice(0, 6).map((match) => (
                      <span
                        key={`${match.level}-${match.subject}-${match.topic}`}
                        className="rounded bg-indigo-100 px-2 py-1 text-xs text-indigo-800 dark:bg-indigo-950 dark:text-indigo-200"
                        title={`NLP relevance score ${match.score}`}
                      >
                        {match.level} · {match.subject}: {match.topic}
                      </span>
                    ))}
                  </div>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>

      <div className="rounded-xl border p-4 dark:border-gray-700">
        <h3 className="font-semibold">Uploaded document copies</h3>
        <p className="mb-3 mt-1 text-sm text-gray-600 dark:text-gray-300">
          Upload PDF, Word, EPUB, MOBI, Kindle, OpenDocument, HTML, Markdown, RTF or text when you want EduAI_Pro to retain a separate copy.
        </p>
        <input
          type="file"
          accept=".pdf,.docx,.txt,.md,.rtf,.html,.htm,.epub,.mobi,.azw,.azw3,.kfx,.fb2,.odt"
          onChange={handleUpload}
          disabled={uploading}
          className="block text-sm"
        />
        {uploading && <p className="mt-2 text-sm">Uploading and analysing…</p>}
        {loading && <p className="mt-2 text-sm">Loading…</p>}
        {!loading && documents.length === 0 && <p className="mt-2 text-sm text-gray-500">No uploaded copies yet.</p>}
        <ul className="mt-3 space-y-3">
          {documents.map((doc) => (
            <li key={doc.id} className="rounded border p-3 dark:border-gray-700">
              <div className="flex items-center justify-between gap-2">
                <label className="flex min-w-0 items-center gap-2">
                  <input
                    type="checkbox"
                    checked={selectedDocIds.includes(doc.id)}
                    onChange={() => toggleDocSelected(doc.id)}
                    aria-label={`Include ${doc.filename} in Course Assistant`}
                  />
                  <a href={resourceTabDownloadUrl(doc.id)} className="truncate font-medium text-blue-600 underline">
                    {doc.filename}
                  </a>
                </label>
                <button type="button" onClick={() => handleDelete(doc.id)} className="shrink-0 rounded border px-2 py-1 text-xs">
                  Remove
                </button>
              </div>
              {doc.summary && <p className="mt-2 text-sm">{doc.summary}</p>}
            </li>
          ))}
        </ul>
      </div>

      {documents.length > 0 && (
        <div className="rounded-xl border p-4 dark:border-gray-700">
          <h3 className="font-semibold">Course Assistant</h3>
          <p className="mb-3 mt-1 text-sm text-gray-600 dark:text-gray-300">
            Check the documents above to include as a knowledge base, then ask a question. Ark AI will answer
            using only those documents — and say so plainly if the answer isn't covered in them.
          </p>
          <form onSubmit={handleAskCourseAssistant} className="space-y-2">
            <p className="text-xs text-gray-500">
              {selectedDocIds.length === 0
                ? 'No documents selected.'
                : `${selectedDocIds.length} document${selectedDocIds.length === 1 ? '' : 's'} selected.`}
            </p>
            <div className="flex flex-col gap-2 sm:flex-row">
              <input
                value={courseQuestion}
                onChange={(event) => setCourseQuestion(event.target.value)}
                placeholder="Ask a question about the selected documents…"
                className="min-w-0 flex-1 rounded border px-3 py-2 dark:border-gray-600 dark:bg-gray-900"
              />
              <LevelSelector level={courseLevel} onChange={setCourseLevel} />
              <button
                type="submit"
                disabled={courseAsking || !selectedDocIds.length || !courseQuestion.trim()}
                className="rounded bg-blue-600 px-4 py-2 text-white disabled:opacity-50"
              >
                {courseAsking ? 'Thinking…' : 'Ask'}
              </button>
            </div>
          </form>
          {courseError && <p role="alert" className="mt-3 rounded bg-red-50 p-3 text-sm text-red-700">{courseError}</p>}
          {courseAnswer && (
            <div className="mt-3 rounded-lg border bg-white p-3 text-sm dark:border-gray-700 dark:bg-gray-900">
              <p className="whitespace-pre-wrap">{courseAnswer.answer}</p>
              <p className="mt-2 text-xs text-gray-500">
                Sources: {courseAnswer.documents.join(', ')}
              </p>
            </div>
          )}
        </div>
      )}
    </section>
  );
}
