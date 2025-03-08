/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {
      colors: {
        primary: '#4CAF50',
        secondary: '#FF5722',
        background: '#f5f5f5',
        text: '#333333',
        accent: '#FFC107',
        muted: '#9E9E9E',
        codeBg: '#2D2D2D',
        codeText: '#F8F8F2',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Merriweather', 'serif'],
        mono: ['Fira Code', 'monospace'],
      },
      lineHeight: {
        normal: '1.5',
        relaxed: '1.625',
      },
    },
  },
  plugins: [],
}

