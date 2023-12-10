const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Cabin", ...defaultTheme.fontFamily.sans],
        body: "Cabin",
        serif: "Playfair",
      },
      colors: {
        sand: {
          light: "#f7f6f5",
          dark: "#edebe6",
          hover: "#cdc4b8",
        },
      },
      spacing: {
        18: "4.5rem",
        22: "5.5rem",
        30: "7.5rem",
        "1/3": "33.333333%",
        "1/6": "16.666667%",
        "3/2": "150%",
      },
      letterSpacing: {
        // wide: '.25rem',
        widest: ".09rem",
        "wide-title": ".13rem",
        "very-wide": ".2rem",
        "extra-wide": ".45rem",
        "ultra-wide": ".9rem",
      },
      fontSize: {
        nav: "0.6875rem",
        // "small-base":
      },
      cursor: {
        left: "url(/static/left_arrow.svg), pointer",
        right: "url(/static/right_arrow.svg), pointer",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
  safelist: ["p-14", "h-1/6", "h-2/6", "h-3/6", "h-4/6", "h-5/6"],
};
