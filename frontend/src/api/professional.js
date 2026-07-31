async function request(path, options) {
  const response = await fetch(`/api/pro${path}`, options);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.detail || `Request failed (${response.status})`);
  }
  return response.json();
}

export function ensureProfessionalUser(profile) {
  return request('/users/ensure', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(profile),
  });
}

export const getProfessionalDashboard = (userId) => request(`/dashboard/${userId}`);
export const listResearchProjects = (userId) => request(`/research/projects/${userId}`);
export const createResearchProject = (body) => request('/research/projects', jsonPost(body));
export const saveResearchNote = (body) => request('/research/notes', jsonPost(body));
export const searchResearch = (query, projectId = '') =>
  request(`/research/search?q=${encodeURIComponent(query)}&project_id=${encodeURIComponent(projectId)}`);
export const listAssessments = () => request('/assessments');
export const createAssessment = (body) => request('/assessments', jsonPost(body));
export const listPortfolio = (userId) => request(`/portfolio/${userId}`);
export const createPortfolioItem = (body) => request('/portfolio', jsonPost(body));
export const listCpd = (userId) => request(`/cpd/${userId}`);
export const createCpd = (body) => request('/cpd', jsonPost(body));
export const listCareerPathways = () => request('/career/pathways');
export const listOrganizations = () => request('/organizations');
export const createOrganization = (body) => request('/organizations', jsonPost(body));
export const listProfessionalCourses = () => request('/courses');
export const getLtiConfig = () => request('/lms/lti/config');

function jsonPost(body) {
  return {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  };
}
