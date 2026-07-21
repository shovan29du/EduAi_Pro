import React, { createContext, useContext, useEffect, useState } from 'react';

const ChildContext = createContext(null);

// Static fallback — overridden once /api/users responds
let _parentProfiles = ['Parent', 'Shovan', 'Bely'];

export function isParentProfile(child) {
  return _parentProfiles.includes(child);
}

export function getParentProfiles() {
  return _parentProfiles;
}

export function ChildProvider({ children }) {
  // No child profiles ship by default (see backend/app/storage.py) -- default to the
  // always-present Parent oversight profile until a real learner profile is added/selected.
  const [child, setChild] = useState(() => localStorage.getItem('selectedChild') || 'Parent');
  const [isRestricted, setIsRestricted] = useState(
    () => localStorage.getItem('isRestricted') === 'true'
  );
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem('darkMode') === 'true');

  const [connectedPlatforms, setConnectedPlatforms] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem('connectedPlatforms')) || {};
    } catch {
      return {};
    }
  });

  const [appearance, setAppearance] = useState(() => {
    try {
      return (
        JSON.parse(localStorage.getItem('appearance')) || {
          bgColor: '',
          fontColor: '',
          fontFamily: '',
          fontSize: 'medium',
          theme: 'default',
        }
      );
    } catch {
      return { bgColor: '', fontColor: '', fontFamily: '', fontSize: 'medium', theme: 'default' };
    }
  });

  useEffect(() => {
    localStorage.setItem('selectedChild', child);
  }, [child]);

  useEffect(() => {
    localStorage.setItem('isRestricted', isRestricted);
  }, [isRestricted]);

  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
    document.documentElement.classList.toggle('dark', darkMode);
  }, [darkMode]);

  useEffect(() => {
    localStorage.setItem('appearance', JSON.stringify(appearance));
    const root = document.documentElement;
    root.style.setProperty('--app-bg-color', appearance.bgColor || '');
    root.style.setProperty('--app-font-color', appearance.fontColor || '');
    root.style.setProperty('--app-font-family', appearance.fontFamily || '');
    const sizeMap = { small: '14px', medium: '16px', large: '19px', 'x-large': '22px', 'xx-large': '26px' };
    root.style.setProperty('--app-font-size', sizeMap[appearance.fontSize] || sizeMap.medium);
    const theme = appearance.theme || 'default';
    root.setAttribute('data-theme', theme);
    root.classList.toggle('dark', theme === 'dark' || theme === 'high-contrast');
    // Apply colour-blind filter
    const cbTheme = appearance.colorBlindTheme || '';
    const filterMap = {
      deuteranopia: 'url(#deuteranopia)',
      protanopia: 'url(#protanopia)',
      tritanopia: 'url(#tritanopia)',
    };
    root.style.filter = filterMap[cbTheme] || '';
  }, [appearance]);

  function updateAppearance(patch) {
    setAppearance((prev) => ({ ...prev, ...patch }));
  }

  useEffect(() => {
    localStorage.setItem('connectedPlatforms', JSON.stringify(connectedPlatforms));
  }, [connectedPlatforms]);

  function togglePlatform(id) {
    setConnectedPlatforms((prev) => ({ ...prev, [id]: !prev[id] }));
  }

  return (
    <ChildContext.Provider
      value={{
        child,
        setChild,
        isRestricted,
        setIsRestricted,
        darkMode,
        setDarkMode,
        appearance,
        updateAppearance,
        connectedPlatforms,
        togglePlatform,
      }}
    >
      {children}
    </ChildContext.Provider>
  );
}

export function useChild() {
  const ctx = useContext(ChildContext);
  if (!ctx) throw new Error('useChild must be used within ChildProvider');
  return ctx;
}
