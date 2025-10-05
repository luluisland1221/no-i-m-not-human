// Navigation bar interaction
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Configuration for noimnothuman.xyz
    const config = {
        domain: 'noimnothuman.xyz',
        imageUrl: 'https://images.noimnothuman.xyz', // R2 CDN URL after migration
        apiEndpoint: 'https://api.noimnothuman.xyz'
    };

    
    // Sidebar collapse functionality
    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const guideSidebar = document.querySelector('.guide-sidebar');
    const guideMainContent = document.querySelector('.guide-main-content');

    // Mobile menu toggle
    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Sidebar collapse toggle
    if (sidebarCollapseBtn) {
        sidebarCollapseBtn.addEventListener('click', function() {
            guideSidebar.classList.toggle('collapsed');

            // Update collapse button icon
            const collapseIcon = this.querySelector('.collapse-icon');
            if (guideSidebar.classList.contains('collapsed')) {
                collapseIcon.textContent = '☰';
                // Save collapsed state to localStorage
                localStorage.setItem('sidebarCollapsed', 'true');
            } else {
                collapseIcon.textContent = '☰';
                // Save expanded state to localStorage
                localStorage.setItem('sidebarCollapsed', 'false');
            }
        });
    }

    // Check saved sidebar state on page load
    const savedSidebarState = localStorage.getItem('sidebarCollapsed');
    if (savedSidebarState === 'true' && guideSidebar) {
        guideSidebar.classList.add('collapsed');
    }

    // Close menu when clicking navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Navigation bar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(0, 0, 0, 0.95)';
        } else {
            navbar.style.background = 'rgba(0, 0, 0, 0.9)';
        }
    });

    // Smooth scrolling
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            // Only handle internal anchor links (starting with #), not external page links
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetSection = document.querySelector(targetId);

                if (targetSection) {
                    const offsetTop = targetSection.offsetTop - 70;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
            // External page links (like guide/) will work normally
        });
    });

    // Scroll animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements that need animation
    const animatedElements = document.querySelectorAll('.feature-card, .news-item, .screenshot-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Typewriter effect - only on index.html
    const heroTitle = document.querySelector('.hero-title');
    const isIndexPage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('/');

    if (heroTitle && isIndexPage) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        let index = 0;

        function typeWriter() {
            if (index < text.length) {
                heroTitle.textContent += text.charAt(index);
                index++;
                setTimeout(typeWriter, 100);
            }
        }

        // Delay starting typewriter effect
        setTimeout(typeWriter, 500);
    }

    // Mouse follow effect (optional)
    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', function(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Create glow effect
        const glow = document.createElement('div');
        glow.style.position = 'fixed';
        glow.style.left = mouseX + 'px';
        glow.style.top = mouseY + 'px';
        glow.style.width = '20px';
        glow.style.height = '20px';
        glow.style.background = 'radial-gradient(circle, rgba(0, 255, 136, 0.3) 0%, transparent 70%)';
        glow.style.borderRadius = '50%';
        glow.style.pointerEvents = 'none';
        glow.style.zIndex = '9999';
        glow.style.transition = 'opacity 0.5s ease';

        document.body.appendChild(glow);

        setTimeout(() => {
            glow.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(glow);
            }, 500);
        }, 100);
    });

    // Button hover effect
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
            this.style.boxShadow = '0 15px 30px rgba(0, 255, 136, 0.4)';
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 10px 20px rgba(0, 255, 136, 0.3)';
        });
    });

    // Feature card hover effect
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.02)';
            this.style.boxShadow = '0 25px 50px rgba(0, 255, 136, 0.4)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 20px 40px rgba(0, 255, 136, 0.3)';
        });
    });

    // Initialization after page load completion
    window.addEventListener('load', function() {
        // Add loading animation
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.5s ease';

        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });

    // Prevent right-click menu (optional, adds mystery)
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        return false;
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Press ESC key to close mobile menu
        if (e.key === 'Escape') {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }

        // Press H key to return to homepage
        if (e.key === 'h' || e.key === 'H') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    });

    // Dynamic background effect
    let particles = [];
    const particleCount = 50;

    function createParticle() {
        return {
            x: Math.random() * window.innerWidth,
            y: Math.random() * window.innerHeight,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            size: Math.random() * 2 + 1,
            opacity: Math.random() * 0.5 + 0.1
        };
    }

    // Initialize particles
    for (let i = 0; i < particleCount; i++) {
        particles.push(createParticle());
    }

    // Animation loop
    function animateParticles() {
        const canvas = document.createElement('canvas');
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '-1';
        canvas.style.opacity = '0.1';

        document.body.appendChild(canvas);

        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            particles.forEach(particle => {
                particle.x += particle.vx;
                particle.y += particle.vy;

                // Boundary detection
                if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
                if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;

                // Draw particles
                ctx.beginPath();
                ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(0, 255, 136, ${particle.opacity})`;
                ctx.fill();
            });

            requestAnimationFrame(animate);
        }

        animate();
    }

    // Delay starting particle effect
    setTimeout(animateParticles, 2000);
});