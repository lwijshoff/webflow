// static/webflow/js/theme.js

// Apply user's OS/browser color scheme preference (light or dark)
(function () {
    const html = document.documentElement;

    // Check for saved user preference (optional future extension)
    const stored = localStorage.getItem("color-theme");

    function applyTheme(mode) {
        const html = document.documentElement;
        html.setAttribute('data-bs-theme', mode);
        
        // Switch favicon
        const favicon = document.getElementById('theme-favicon');
        if (favicon && mode === 'light') {
            favicon.href = favicon.dataset.darkSrc;
        }
        
        // Switch header logo (same files!)
        const logo = document.querySelector('.navbar-logo');
        if (logo) {
            logo.src = mode === 'light' ? logo.dataset.logoDark : logo.dataset.logoLight || logo.src;
        }
    }


    if (stored === "light" || stored === "dark") {
        applyTheme(stored);
    } else {
        const prefersDark = window.matchMedia &&
            window.matchMedia("(prefers-color-scheme: dark)").matches;
        applyTheme(prefersDark ? "dark" : "light");
    }

    // React to OS/browser changes
    if (window.matchMedia) {
        window.matchMedia("(prefers-color-scheme: dark)")
            .addEventListener("change", e => {
                const newMode = e.matches ? "dark" : "light";
                applyTheme(newMode);
                // If you *don’t* want this to override user choice later, skip localStorage here
            });
    }
})();