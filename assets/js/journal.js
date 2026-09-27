/* Accessible, dependency-free studio viewer. Links remain usable without JavaScript. */
(() => {
  'use strict';
  // Use the site's compact header treatment while reading the long journal.
  const header = document.getElementById('header');
  const syncHeader = () => header?.classList.toggle('header--scrolled', window.scrollY > 60);
  window.addEventListener('scroll', syncHeader, {passive:true});
  syncHeader();
  const tiles = [...document.querySelectorAll('[data-photo]')];
  const viewer = document.getElementById('journal-viewer');
  if (!tiles.length || !viewer || typeof viewer.showModal !== 'function') return;
  const image = document.getElementById('viewer-image');
  const caption = document.getElementById('viewer-caption');
  const chapter = document.getElementById('viewer-chapter');
  const counter = document.getElementById('viewer-counter');
  const strip = document.getElementById('viewer-thumbs');
  const close = document.getElementById('viewer-close');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let current = 0, opener, previousOverflow = '', touchStart;
  const photos = tiles.map(tile => ({src: tile.href, thumb: tile.querySelector('img').getAttribute('srcset').split(' ')[0], caption: tile.querySelector('img').alt, chapter: tile.dataset.chapter}));
  const thumbs = photos.map((photo, i) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.setAttribute('aria-label', `View photograph ${i + 1}: ${photo.caption}`);
    const thumbnail = document.createElement('img');
    thumbnail.src = photo.thumb; thumbnail.alt = ''; thumbnail.loading = 'lazy';
    button.append(thumbnail); button.addEventListener('click', () => show(i)); strip.append(button);
    return button;
  });
  function show(index) {
    current = (index + photos.length) % photos.length;
    const photo = photos[current];
    image.src = photo.src; image.alt = photo.caption;
    caption.textContent = photo.caption; chapter.textContent = photo.chapter;
    counter.textContent = `${String(current + 1).padStart(2, '0')} / ${photos.length}`;
    thumbs.forEach((button, i) => button.setAttribute('aria-current', String(i === current)));
    // Scroll only the thumbnail strip, never the page behind the dialog.
    const target = thumbs[current];
    strip.scrollTo({left: Math.max(0, target.offsetLeft - strip.offsetLeft - strip.clientWidth / 2 + target.clientWidth / 2), behavior: reduced.matches ? 'instant' : 'smooth'});
    const preload = new Image(); preload.src = photos[(current + 1) % photos.length].src;
  }
  tiles.forEach((tile, i) => tile.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault(); opener = tile;
    previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    viewer.showModal(); show(i); close.focus();
  }));
  close.addEventListener('click', () => viewer.close());
  viewer.addEventListener('close', () => {
    document.body.style.overflow = previousOverflow;
    opener?.focus({preventScroll:true});
  });
  document.getElementById('viewer-prev').addEventListener('click', () => show(current - 1));
  document.getElementById('viewer-next').addEventListener('click', () => show(current + 1));
  viewer.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault(); show(current + (event.key === 'ArrowRight' ? 1 : -1));
    }
    if (event.key === 'Escape') { event.preventDefault(); event.stopPropagation(); viewer.close(); }
    if (event.key === 'Tab') {
      const buttons = [...viewer.querySelectorAll('button')];
      const first = buttons[0], last = buttons[buttons.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    }
  });
  const stage = viewer.querySelector('.journal-viewer-stage');
  stage.addEventListener('touchstart', event => {
    if (event.touches.length === 1) touchStart = {x:event.touches[0].clientX, y:event.touches[0].clientY};
  }, {passive:true});
  stage.addEventListener('touchend', event => {
    if (!touchStart) return;
    const dx = event.changedTouches[0].clientX - touchStart.x, dy = event.changedTouches[0].clientY - touchStart.y;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) show(current + (dx < 0 ? 1 : -1));
    touchStart = null;
  }, {passive:true});
  stage.addEventListener('touchcancel', () => {touchStart = null;}, {passive:true});
})();
