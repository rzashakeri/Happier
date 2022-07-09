module.exports = {
    content: [
        '../templates/**/*.{html,js,py}',
        '../feed/**/*.{html,js,py}',
        '../comment/**/*.{html,js,py}',
        '../home/**/*.{html,js,py}',
        '../user_profile/**/*.{html,js,py}',
        '../post/**/*.{html,js, py}',
        '../user_management/**/*.{html,js,py}',
        '../venv/Lib/site-packages/crispy_tailwind/templates/**/*.{html,js}',
    ],
    darkMode: 'data-theme',
    theme: {
        extend: {},
        screens: {
            '2sm': '481px',
            // => @media (min-width: 481px) { ... }

            'sm': '640px',
            // => @media (min-width: 640px) { ... }

            'md': '768px',
            // => @media (min-width: 768px) { ... }

            'lg': '1024px',
            // => @media (min-width: 1024px) { ... }

            'xl': '1280px',
            // => @media (min-width: 1280px) { ... }

            '2xl': '1536px',
            // => @media (min-width: 1536px) { ... }
            'max-2xl': {'max': '1535px'},
            // => @media (max-width: 1535px) { ... }

            'max-xl': {'max': '1279px'},
            // => @media (max-width: 1279px) { ... }

            'max-lg': {'max': '1023px'},
            // => @media (max-width: 1023px) { ... }

            'max-md': {'max': '767px'},
            // => @media (max-width: 767px) { ... }

            'max-sm': {'max': '639px'},
            // => @media (max-width: 639px) { ... }

            'max-2sm': {'max': '480px'},
            // => @media (max-width: 480px) { ... }
        }
    },
    plugins: [require("daisyui"), require('@tailwindcss/line-clamp')],
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