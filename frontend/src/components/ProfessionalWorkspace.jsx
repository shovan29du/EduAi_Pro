import { useEffect, useState } from 'react';
import {
  ensureProfessionalUser,
  getProfessionalDashboard,
  listProfessionalCourses,
} from '../api/professional.js';

const SECTIONS = ['Dashboard'];

const FAVOURITES = [
  ['Study Coach', '🧭', 'Get a personalised study plan and encouragement from Ark AI.'],
];

export default function ProfessionalWorkspace({ level = '1', onNavigate }) {
  const [section, setSection] = useState('Dashboard');
  const [user, setUser] = useState(null);
  const [dashboard, setDashboard] = useState({});
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(true);

  async function refresh(activeUser) {
    const [dash, courseRows] = await Promise.all([
      getProfessionalDashboard(activeUser.id),
      listProfessionalCourses(),
    ]);
    setDashboard(dash);
    setCourses(courseRows);
  }

  useEffect(() => {
    ensureProfessionalUser({ email: 'shovan@legacy.local', display_name: 'Shovan', role: 'admin' })
      .then(async (activeUser) => {
        setUser(activeUser);
        await refresh(activeUser);
      })
      .catch((err) => setError(err.message))
      .finally(() => setBusy(false));
  }, []);

  const metricCards = [
    ['Research projects', dashboard.research_projects || 0],
    ['Knowledge notes', dashboard.notes || 0],
    ['Assessment attempts', dashboard.assessment_attempts || 0],
    ['Portfolio projects', dashboard.portfolio_items || 0],
    ['CPD hours', Number(dashboard.cpd_hours || 0).toFixed(1)],
  ];

  return (
    <section className="overflow-hidden rounded-2xl border bg-white shadow-sm dark:border-gray-700 dark:bg-gray-900">
      <header className="bg-gradient-to-r from-slate-950 via-indigo-950 to-blue-900 p-6 text-white">
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-blue-200">Adult learning workspace</p>
        <h2 className="mt-2 text-3xl font-bold">EduAI_Pro Command Centre</h2>
        <p className="mt-2 max-w-3xl text-sm text-slate-200">
          Adult and professional learning from Level 1 through M2.
          Current level: <strong>{level}</strong>
        </p>
      </header>

      <nav aria-label="Professional workspace" className="flex flex-wrap gap-2 border-b p-3 dark:border-gray-700">
        {SECTIONS.map((item) => (
          <button
            key={item}
            onClick={() => setSection(item)}
            className={`rounded-full px-3 py-1.5 text-sm font-medium ${
              section === item
                ? 'bg-indigo-600 text-white'
                : 'text-gray-700 hover:bg-indigo-50 dark:text-gray-200 dark:hover:bg-gray-800'
            }`}
          >
            {item}
          </button>
        ))}
      </nav>

      <div className="min-h-[38rem]">
        <div className="p-5">
          {error && <p role="alert" className="mb-4 rounded-lg bg-red-50 p-3 text-sm text-red-700">{error}</p>}
          {busy && <p className="mb-3 text-sm text-gray-500">Updating workspace…</p>}

          {section === 'Dashboard' && (
            <div className="space-y-6">
              <div>
                <h3 className="text-xl font-bold">Welcome, {user?.display_name || 'learner'}</h3>
                <p className="text-sm text-gray-500">Your learning, research and professional evidence in one place.</p>
              </div>
              {onNavigate && (
                <Panel title="Favourites">
                  <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-4">
                    {FAVOURITES.map(([tab, emoji, description]) => (
                      <button
                        key={tab}
                        type="button"
                        onClick={() => onNavigate(tab)}
                        className="rounded-xl border p-3 text-left transition-colors hover:border-indigo-400 hover:bg-indigo-50 dark:border-gray-700 dark:hover:bg-indigo-950"
                      >
                        <span className="text-2xl">{emoji}</span>
                        <p className="mt-1 text-sm font-semibold">{tab}</p>
                        <p className="mt-0.5 text-xs text-gray-500">{description}</p>
                      </button>
                    ))}
                  </div>
                </Panel>
              )}
              <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-5">
                {metricCards.map(([label, value]) => (
                  <div key={label} className="rounded-xl border p-4 dark:border-gray-700">
                    <div className="text-2xl font-bold text-indigo-700 dark:text-indigo-300">{value}</div>
                    <div className="mt-1 text-xs text-gray-500">{label}</div>
                  </div>
                ))}
              </div>
              <div className="grid gap-4 lg:grid-cols-2">
                <Panel title="Continue learning">
                  {courses.slice(0, 5).map((course) => (
                    <div key={course.id} className="border-b py-2 text-sm last:border-0 dark:border-gray-700">
                      <strong>{course.title}</strong>
                      <span className="ml-2 text-xs text-gray-500">{course.level_id}</span>
                    </div>
                  ))}
                  {courses.length === 0 && <Empty>Run the JSON migration to populate database courses.</Empty>}
                </Panel>
                <Panel title="Recommended next actions">
                  <ul className="list-disc space-y-2 pl-5 text-sm">
                    <li>Continue a course from where you left off.</li>
                    <li>Visit Study Coach for a personalised study plan.</li>
                  </ul>
                </Panel>
              </div>
            </div>
          )}

        </div>
      </div>
    </section>
  );
}

function Panel({ title, children }) {
  return <div className="rounded-xl border p-4 dark:border-gray-700"><h4 className="mb-3 font-semibold">{title}</h4>{children}</div>;
}

function Empty({ children }) {
  return <p className="text-sm text-gray-500">{children}</p>;
}
