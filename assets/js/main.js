// YEAR
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();

// PROGRESS BAR
const progress = document.getElementById("progress");
if (progress) {
  window.addEventListener("scroll", () => {
    const h = document.body.scrollHeight - window.innerHeight;
    progress.style.width = (window.scrollY / h) * 100 + "%";
  });
}

// REVEAL
const reveals = document.querySelectorAll(".reveal");
if (reveals.length) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => e.isIntersecting && e.target.classList.add("visible"));
  }, { threshold: 0.15 });
  reveals.forEach(r => observer.observe(r));
}

// CASE NAV HIGHLIGHT
const caseNav = document.querySelector(".case-nav");
if (caseNav) {
  const caseLinks = Array.from(caseNav.querySelectorAll("a[href^=\"#\"]"));
  const caseSections = caseLinks
    .map(link => {
      const id = link.getAttribute("href").slice(1);
      return document.getElementById(id);
    })
    .filter(Boolean);

  const setActive = id => {
    caseLinks.forEach(link => {
      link.classList.toggle("active", link.getAttribute("href") === `#${id}`);
    });
  };

  const caseObserver = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    },
    {
      rootMargin: "-25% 0px -40% 0px",
      threshold: 0.2
    }
  );

  caseSections.forEach(section => caseObserver.observe(section));
}

// IMAGEOMICS ARCH DIAGRAM
const archDiagram = document.getElementById("arch-diagram");
const buttons = document.querySelectorAll(".arch-toggle button");

if (archDiagram && buttons.length) {
  const data = {
    before: [
      "Documents",
      "Forms",
      "Policies",
      "Resources",
      "Miscellaneous"
    ],
    after: [
      "Getting started",
      "Research workflows",
      "Requests & approvals",
      "Shared resources",
      "Institute updates"
    ]
  };

  function render(view) {
    archDiagram.innerHTML = "";
    data[view].forEach((item, i) => {
      const div = document.createElement("div");
      div.className = "arch-node";
      div.style.animationDelay = `${i * 60}ms`;
      div.textContent = item;
      archDiagram.appendChild(div);
    });
  }

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      render(btn.dataset.view);
    });
  });

  render("before");
}

// ROADMAP TOGGLE
const toggle = document.getElementById("expand-next");
const nextContent = document.getElementById("next-content");

if (toggle && nextContent) {
  toggle.addEventListener("click", () => {
    nextContent.classList.toggle("hidden");
    toggle.textContent = nextContent.classList.contains("hidden")
      ? "Show roadmap thinking →"
      : "Hide roadmap thinking ←";
  });
}
