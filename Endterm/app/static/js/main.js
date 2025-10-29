// main.js

document.addEventListener("DOMContentLoaded", () => {

  // --- PAGE FADE IN ---
  const formCard = document.querySelector(".form-card");
  if (formCard) formCard.classList.add("animate-fade-in");

  // --- FLASH MESSAGES ---
  const flashes = document.querySelectorAll(".flash");
  flashes.forEach((f, i) => {
    setTimeout(() => f.classList.add("show"), i * 200);
    setTimeout(() => f.classList.remove("show"), 4000 + i * 200);
  });

  // --- FORM BUTTON LOADING ---
  const forms = document.querySelectorAll("form");
  forms.forEach(form => {
    form.addEventListener("submit", () => {
      const btn = form.querySelector(".btn");
      if(btn){
        btn.disabled = true;
        btn.dataset.original = btn.textContent;
        btn.textContent = "Processing...";
        const loader = document.createElement("span");
        loader.classList.add("loader");
        btn.appendChild(loader);
      }
    });
  });

  // --- PAGE TRANSITION ON LINK CLICK (login <-> register) ---
  const links = document.querySelectorAll("a[href^='/client']");
  links.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      const href = link.getAttribute("href");

      // fade out the form
      if(formCard) formCard.classList.remove("animate-fade-in");
      formCard.style.transition = "opacity 300ms ease, transform 300ms ease";
      formCard.style.opacity = 0;
      formCard.style.transform = "translateY(10px)";

      // navigate after fade out
      setTimeout(() => {
        window.location.href = href;
      }, 300);
    });
  });

});
