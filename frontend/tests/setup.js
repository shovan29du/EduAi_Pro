import '@testing-library/jest-dom/vitest';
import { configure } from '@testing-library/react';

// The default 1s timeout for findBy*/waitFor is too tight when the whole suite
// runs next to other heavy processes (it made a ChessTutor test fail only on a
// busy machine). Passing tests are not slowed down by a larger limit.
configure({ asyncUtilTimeout: 5000 });
