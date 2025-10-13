// Optimized JavaScript for noimnothuman.xyz - ES6+ Modern browser version
// Removed all polyfills and unnecessary transforms for better performance

(() => {
    'use strict';

    // Cache DOM elements
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navbar = document.querySelector('.navbar');

    // Configuration for noimnothuman.xyz
    const config = {
        domain: 'noimnothuman.xyz',
        imageUrl: 'https://images.noimnothuman.xyz',
        apiEndpoint: 'https://api.noimnothuman.xyz'
    };

    // Mobile menu toggle - using modern event handling
    hamburger?.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu?.classList.toggle('active');
    });

    // Close menu on navigation link click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger?.classList.remove('active');
            navMenu?.classList.remove('active');
        });
    });

    // Optimized scroll effect using requestAnimationFrame
    let ticking = false;
    const updateNavbar = () => {
        if (!navbar) return;
        const scrolled = window.scrollY > 100;
        navbar.style.background = `rgba(0, 0, 0, ${scrolled ? 0.95 : 0.9})`;
        ticking = false;
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateNavbar);
            ticking = true;
        }
    });

    // Smooth scrolling for anchor links only
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute('href'));
            target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // Optimized intersection observer for animations
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    animationObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Set up animated elements
        document.querySelectorAll('.feature-card, .screenshot-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            animationObserver.observe(el);
        });
    }

    // Sidebar functionality - simplified
    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const guideSidebar = document.querySelector('.guide-sidebar');

    sidebarCollapseBtn?.addEventListener('click', () => {
        const isCollapsed = guideSidebar?.classList.toggle('collapsed');
        localStorage.setItem('sidebarCollapsed', isCollapsed);
    });

    // Restore sidebar state
    if (localStorage.getItem('sidebarCollapsed') === 'true') {
        guideSidebar?.classList.add('collapsed');
    }

    // Keyboard shortcuts - simplified
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hamburger?.classList.remove('active');
            navMenu?.classList.remove('active');
        }
    });

    // Performance-optimized hover effects using CSS
    // No JavaScript needed for basic hover states - CSS handles them

    // Optional: Simple loading fade
    requestAnimationFrame(() => {
        document.body.style.opacity = '1';
        document.body.style.transition = 'opacity 0.3s ease';
    });

})();