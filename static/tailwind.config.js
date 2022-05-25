module.exports = {
  content: [
      '../templates/**/*.{html,js}',
      '../feed/**/*.{html,js}',
      '../home/**/*.{html,js}',
      '../user_profile/**/*.{html,js}',
      '../static/js/**/*.{html,js, json}'
  ],
  darkMode: 'data-theme',
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    styled: true,
    themes: ["light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  },
}
