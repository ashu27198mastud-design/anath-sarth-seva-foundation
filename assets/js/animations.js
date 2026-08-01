/**
 * animations.js - Scroll reveal and interactive animations
 * Handles progressive enhancement animation logic.
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
});

/**
 * Initialize scroll reveal animations with progressive enhancement
 * Ensures content is never invisible by default, especially without JS or with reduced motion.
 */
function initScrollReveal() {
  // 1. Check for reduced motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  // 2. If user prefers reduced motion, exit early (content remains visible)
  if (prefersReducedMotion) {
    return;
  }

  // 3. Setup animations for those who allow motion
  const revealElements = document.querySelectorAll('.reveal');
  
  if (revealElements.length === 0) return;

  // Add hidden class to setup initial state (e.g., opacity: 0, translate)
  revealElements.forEach(el => {
    el.classList.add('reveal--hidden');
    
    // Stagger animation for grid items (children)
    const children = el.querySelectorAll('.reveal-child');
    if (children.length > 0) {
      children.forEach((child, index) => {
        // Add 0.1s delay for each subsequent child, starting after a base delay (e.g., 0.2s)
        const delay = 0.2 + (index * 0.1);
        child.style.transitionDelay = `${delay}s`;
        child.classList.add('reveal-child--hidden');
      });
    }
  });

  // Create observer
  const observerOptions = {
    root: null,
    rootMargin: '-40px', // Trigger slightly before element comes into view
    threshold: 0.15      // 15% of element must be visible to trigger
  };

  const revealCallback = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        
        // Remove hidden state, add visible state
        el.classList.remove('reveal--hidden');
        el.classList.add('reveal--visible');
        
        // Handle children stagger if present
        const children = el.querySelectorAll('.reveal-child');
        if (children.length > 0) {
          children.forEach(child => {
            child.classList.remove('reveal-child--hidden');
            child.classList.add('reveal-child--visible');
          });
        }
        
        // Unobserve after revealing (one-time animation)
        observer.unobserve(el);
      }
    });
  };

  const observer = new IntersectionObserver(revealCallback, observerOptions);
  
  // Start observing
  revealElements.forEach(el => observer.observe(el));
}

/**
 * Animates a number from 0 to target over a specified duration.
 * Intended for future use with impact metrics when real data is available.
 * Respects prefers-reduced-motion settings.
 * 
 * @param {HTMLElement} element - The DOM element where the number will be displayed
 * @param {number} target - The target number to reach
 * @param {number} duration - Total duration of the animation in milliseconds
 */
export function animateCounter(element, target, duration = 2000) {
  if (!element || typeof target !== 'number') return;
  
  // Check reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    element.textContent = target.toLocaleString();
    return;
  }

  let startTimestamp = null;
  
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    
    // Easing function (easeOutExpo) for smoother deceleration
    const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
    const currentValue = Math.floor(easeProgress * target);
    
    element.textContent = currentValue.toLocaleString();
    
    if (progress < 1) {
      window.requestAnimationFrame(step);
    } else {
      element.textContent = target.toLocaleString(); // Ensure exact target at the end
    }
  };
  
  window.requestAnimationFrame(step);
}
