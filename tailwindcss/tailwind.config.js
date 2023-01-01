/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        body: 'Inter',
        serif: 'Playfair',
      },
      colors: {
        sand: {
          light: '#f7f6f5',
          dark: '#edebe6',
          hover: '#cdc4b8',
        },
      },
      spacing: {
        23: '24%',
      },
      letterSpacing: {
        wide: '.25rem',
        widest: '.3333rem',
        'extra-wide': '.45rem',
      },
    },
  },
  plugins: [],
}
