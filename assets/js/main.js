/* Progressive enhancement: all content and navigation work without JavaScript. */
'use strict';
const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
const menu = document.querySelector('.menu-toggle');
const links = document.getElementById('nav-links');
if (menu && links) {
  menu.hidden = false;
  document.documentElement.classList.add('js');
  const closeMenu = () => menu.setAttribute('aria-expanded', 'false');
  menu.addEventListener('click', () => {
    menu.setAttribute('aria-expanded', String(menu.getAttribute('aria-expanded') !== 'true'));
  });
  links.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      menu.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.nav')) closeMenu();
  });
  const desktop = window.matchMedia('(min-width: 761px)');
  desktop.addEventListener('change', closeMenu);
}
const caseLinks = [...document.querySelectorAll('.case-nav a')];
if (caseLinks.length && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of caseLinks) {
        if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
  caseLinks.forEach(link => {
    const section = document.getElementById(link.hash.slice(1));
    if (section) observer.observe(section);
  });
}
