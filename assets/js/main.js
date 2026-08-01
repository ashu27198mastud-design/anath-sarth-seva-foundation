/**
 * main.js - Core interactive functionality for Ananth Sarth Seva Foundation
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  initSmoothScroll();
  initDesktopDropdowns();
  initActiveNavHighlight();
  initStoryFilter();
});

/**
 * 1. Sticky Header with Glass Effect
 */
function initStickyHeader() {
  const header = document.getElementById('header');
  if (!header) return;

  let ticking = false;

  const onScroll = () => {
    if (window.scrollY > 80) {
      header.classList.add('header--scrolled');
    } else {
      header.classList.remove('header--scrolled');
    }
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });
}

/**
 * 2. Mobile Menu
 */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobile-toggle');
  const closeBtn = document.getElementById('mobile-menu-close');
  const mobileMenu = document.getElementById('mobile-menu');
  const body = document.body;

  if (!toggleBtn || !mobileMenu) return;

  const openMenu = () => {
    mobileMenu.classList.add('mobile-menu--open');
    mobileMenu.setAttribute('aria-hidden', 'false');
    toggleBtn.setAttribute('aria-expanded', 'true');
    body.style.overflow = 'hidden'; // Prevent scrolling
    trapFocus(mobileMenu);
  };

  const closeMenu = () => {
    mobileMenu.classList.remove('mobile-menu--open');
    mobileMenu.setAttribute('aria-hidden', 'true');
    toggleBtn.setAttribute('aria-expanded', 'false');
    body.style.overflow = ''; // Restore scrolling
    toggleBtn.focus();
  };

  toggleBtn.addEventListener('click', openMenu);
  if (closeBtn) {
    closeBtn.addEventListener('click', closeMenu);
  }

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('mobile-menu--open')) {
      closeMenu();
    }
  });

  // Close when clicking outside nav area
  mobileMenu.addEventListener('click', (e) => {
    if (e.target === mobileMenu) {
      closeMenu();
    }
  });

  // Accordion sub-menus
  const accordions = mobileMenu.querySelectorAll('.mobile-menu__accordion-toggle');
  accordions.forEach(accordion => {
    accordion.addEventListener('click', function (e) {
      e.preventDefault();
      
      const parentItem = this.closest('.mobile-menu__item');
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      // Close all other accordions
      accordions.forEach(acc => {
        if (acc !== this) {
          acc.setAttribute('aria-expanded', 'false');
          const p = acc.closest('.mobile-menu__item');
          if (p) p.classList.remove('mobile-menu__accordion--open');
        }
      });

      // Toggle current accordion
      if (isExpanded) {
        this.setAttribute('aria-expanded', 'false');
        if (parentItem) parentItem.classList.remove('mobile-menu__accordion--open');
      } else {
        this.setAttribute('aria-expanded', 'true');
        if (parentItem) parentItem.classList.add('mobile-menu__accordion--open');
      }
    });
  });

  // Simple focus trap for accessibility
  function trapFocus(element) {
    const focusableEls = element.querySelectorAll('a[href]:not([disabled]), button:not([disabled]), textarea:not([disabled]), input[type="text"]:not([disabled]), input[type="radio"]:not([disabled]), input[type="checkbox"]:not([disabled]), select:not([disabled])');
    if (focusableEls.length === 0) return;
    
    const firstFocusableEl = focusableEls[0];  
    const lastFocusableEl = focusableEls[focusableEls.length - 1];

    element.addEventListener('keydown', function(e) {
      const isTabPressed = (e.key === 'Tab' || e.keyCode === 9);
      if (!isTabPressed) return;
      if (e.shiftKey) { 
        if (document.activeElement === firstFocusableEl) {
          lastFocusableEl.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusableEl) {
          firstFocusableEl.focus();
          e.preventDefault();
        }
      }
    });
    
    // Delay to ensure element is visible before focusing
    setTimeout(() => {
        if (firstFocusableEl) firstFocusableEl.focus();
    }, 100);
  }
}

/**
 * 3. Smooth Scroll
 */
function initSmoothScroll() {
  const mobileMenu = document.getElementById('mobile-menu');
  const body = document.body;
  const toggleBtn = document.getElementById('mobile-toggle');

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();

        // Close mobile menu if open
        if (mobileMenu && mobileMenu.classList.contains('mobile-menu--open')) {
          mobileMenu.classList.remove('mobile-menu--open');
          mobileMenu.setAttribute('aria-hidden', 'true');
          if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
          body.style.overflow = '';
        }

        const isMobile = window.innerWidth < 768;
        const headerHeight = isMobile ? 64 : 72; // Account for fixed header height
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * 4. Desktop Dropdown Enhancement
 */
function initDesktopDropdowns() {
  const dropdownParents = document.querySelectorAll('.header__nav-item--has-dropdown');
  
  dropdownParents.forEach(parent => {
    const link = parent.querySelector('.header__nav-link');
    const dropdown = parent.querySelector('.header__dropdown');
    
    if (!link || !dropdown) return;

    // Keyboard support: Enter/Space to toggle
    link.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        parent.classList.toggle('header__nav-item--active');
        
        if (parent.classList.contains('header__nav-item--active')) {
          link.setAttribute('aria-expanded', 'true');
          // Focus first item in dropdown
          const firstItem = dropdown.querySelector('a, button');
          if (firstItem) firstItem.focus();
        } else {
          link.setAttribute('aria-expanded', 'false');
        }
      }
    });

    // Close on Escape and return focus
    parent.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        parent.classList.remove('header__nav-item--active');
        link.setAttribute('aria-expanded', 'false');
        link.focus();
      }
    });

    // Handle focus leaving the dropdown
    parent.addEventListener('focusout', () => {
      setTimeout(() => {
        if (!parent.contains(document.activeElement)) {
          parent.classList.remove('header__nav-item--active');
          link.setAttribute('aria-expanded', 'false');
        }
      }, 10);
    });
  });
}

/**
 * 5. Active Navigation Highlighting
 */
function initActiveNavHighlight() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.header__nav-link');
  
  if (sections.length === 0 || navLinks.length === 0) return;

  const observerOptions = {
    root: null,
    rootMargin: '-50% 0px -50% 0px', // Trigger when section is in middle of viewport
    threshold: 0
  };

  const observerCallback = (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        
        navLinks.forEach(link => {
          link.classList.remove('header__nav-link--active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('header__nav-link--active');
          }
        });
      }
    });
  };

  const observer = new IntersectionObserver(observerCallback, observerOptions);
  sections.forEach(section => {
    observer.observe(section);
  });
}

/**
 * 6. Featured Story Filter
 */
function initStoryFilter() {
  const filterBtns = document.querySelectorAll('.featured-story__filter-btn');
  
  if (filterBtns.length === 0) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active class from all
      filterBtns.forEach(b => b.classList.remove('featured-story__filter-btn--active'));
      
      // Add active class to clicked
      btn.classList.add('featured-story__filter-btn--active');
      
      // Note: Data filtering logic would go here, currently visual toggle only
    });
  });
}
