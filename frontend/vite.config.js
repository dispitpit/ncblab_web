import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',           // ← 讓外部也能連
    port: 5173,                // ← 可省略，預設就是 5173
    proxy: {
      '/api': {
        target: 'http://flask-backend:5000', // Flask backend
        changeOrigin: true
      }
    }
  }
})
