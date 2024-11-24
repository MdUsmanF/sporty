import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "tailwindcss";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  css: {
    postcss: {
      plugins: [tailwindcss()],
    },
  },
  server: {
    host: true, // Listen on all addresses
    port: 5173, // Default Vite port
    watch: {
      usePolling: true // Required for Docker on some systems
    }
  }
});