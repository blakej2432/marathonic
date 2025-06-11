import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../backend/', 
    emptyOutDir: false,
    rollupOptions: {
      input: {
        race: path.resolve(__dirname, 'src/entries/race.tsx'),
        login: path.resolve(__dirname, 'src/entries/login.tsx'),
        profile: path.resolve(__dirname, 'src/entries/profile.tsx'),
      },
      output: {
        entryFileNames: (chunkInfo) => {
          const name = chunkInfo.name;
          if (name === 'race') return 'race/static/js/race.bundle.js';
          if (name === 'login') return 'account/static/js/login.bundle.js';
          if (name === 'profile') return 'user/static/js/profile.bundle.js';
          return 'static/js/[name].bundle.js';
        },
      },
    },
  },
});