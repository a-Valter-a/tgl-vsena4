(function () {
  "use strict";

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  /* ——— Popups ——— */
  function openPopup(id) {
    const popup = document.getElementById(id);
    if (!popup) return;
    popup.classList.add("is-open");
    popup.setAttribute("aria-hidden", "false");
    document.body.classList.add("no-scroll");
  }

  function closePopup(popup) {
    popup.classList.remove("is-open");
    popup.setAttribute("aria-hidden", "true");
    if (!$$(".popup.is-open").length) {
      document.body.classList.remove("no-scroll");
    }
  }

  $$("[data-popup-open]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openPopup(btn.dataset.popupOpen);
    });
  });

  $$(".popup").forEach((popup) => {
    popup.querySelectorAll("[data-popup-close]").forEach((el) => {
      el.addEventListener("click", () => closePopup(popup));
    });
    popup.addEventListener("click", (e) => {
      if (e.target === popup) closePopup(popup);
    });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    $$(".popup.is-open").forEach(closePopup);
  });

  /* ——— Scroll to top ——— */
  const scrollBtn = $("#scroll-top");
  if (scrollBtn) {
    const toggleScrollBtn = () => {
      scrollBtn.classList.toggle("is-visible", window.scrollY > 400);
    };
    window.addEventListener("scroll", toggleScrollBtn, { passive: true });
    toggleScrollBtn();
    scrollBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ——— Reviews slider ——— */
  const reviews = $(".reviews-slider");
  if (reviews) {
    const viewport = $(".reviews-slider__viewport", reviews);
    const track = $(".reviews-slider__track", reviews);
    const slides = $$(".reviews-slider__slide", reviews);
    const prev = $("[data-reviews-prev]", reviews);
    const next = $("[data-reviews-next]", reviews);
    const bullets = $$(".reviews-slider__bullet", reviews);
    let index = 0;

    const goTo = (i) => {
      index = (i + slides.length) % slides.length;
      track.style.transform = `translateX(-${index * 100}%)`;
      bullets.forEach((b, n) => b.classList.toggle("is-active", n === index));
      slides.forEach((s, n) => s.setAttribute("aria-hidden", n !== index));
    };

    prev?.addEventListener("click", () => goTo(index - 1));
    next?.addEventListener("click", () => goTo(index + 1));
    bullets.forEach((b) => {
      b.addEventListener("click", () => goTo(Number(b.dataset.index)));
    });

    const swipeTarget = viewport || track;
    let touchStartX = 0;
    let touchStartY = 0;

    swipeTarget.addEventListener(
      "touchstart",
      (e) => {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        viewport?.classList.add("is-dragging");
      },
      { passive: true }
    );

    swipeTarget.addEventListener(
      "touchend",
      (e) => {
        viewport?.classList.remove("is-dragging");
        const touch = e.changedTouches[0];
        const dx = touch.clientX - touchStartX;
        const dy = touch.clientY - touchStartY;

        if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
        goTo(index + (dx < 0 ? 1 : -1));
      },
      { passive: true }
    );

    swipeTarget.addEventListener(
      "touchcancel",
      () => viewport?.classList.remove("is-dragging"),
      { passive: true }
    );
  }

  /* ——— Gallery slider ——— */
  const gallery = $("#popup-gallery");
  if (gallery) {
    const gTrack = $(".gallery__track", gallery);
    const gSlides = $$(".gallery__slide", gallery);
    let gIndex = 0;

    const goGallery = (i) => {
      gIndex = (i + gSlides.length) % gSlides.length;
      gTrack.style.transform = `translateX(-${gIndex * 100}%)`;
    };

    $("[data-gallery-prev]", gallery)?.addEventListener("click", () =>
      goGallery(gIndex - 1)
    );
    $("[data-gallery-next]", gallery)?.addEventListener("click", () =>
      goGallery(gIndex + 1)
    );
  }

  /* ——— Quiz step form ——— */
  const quiz = $("#quiz");
  if (quiz) {
    const steps = $$(".quiz__step", quiz);
    const progress = $(".quiz__progress-bar", quiz);
    const counter = $(".quiz__counter", quiz);
    const btnPrev = $("[data-quiz-prev]", quiz);
    const btnNext = $("[data-quiz-next]", quiz);
    const btnSubmit = $("[data-quiz-submit]", quiz);
    const success = $(".quiz__success", quiz);
    const form = $("form", quiz);
    let step = 0;
    const total = steps.length;

    const updateQuiz = () => {
      steps.forEach((s, i) => s.classList.toggle("is-active", i === step));
      const pct = ((step + 1) / total) * 100;
      if (progress) progress.style.width = pct + "%";
      if (counter) counter.textContent = step + 1 + "/" + total;
      if (btnPrev) btnPrev.style.visibility = step === 0 ? "hidden" : "visible";
      if (btnNext) btnNext.hidden = step === total - 1;
      if (btnSubmit) btnSubmit.hidden = step !== total - 1;
    };

    const validateStep = () => {
      const current = steps[step];
      const radios = $$('input[type="radio"]', current);
      if (radios.length) {
        return radios.some((r) => r.checked);
      }
      const checks = $$(
        'input[type="checkbox"]:not([name="consent"])',
        current
      );
      if (checks.length) {
        return checks.some((c) => c.checked);
      }
      const phone = $('input[type="tel"]', current);
      if (phone) {
        const digits = phone.value.replace(/\D/g, "");
        if (digits.length < 11) {
          phone.focus();
          return false;
        }
      }
      const consent = $$('input[name="consent"]', current);
      if (consent.length) {
        return consent.every((c) => c.checked);
      }
      return true;
    };

    btnPrev?.addEventListener("click", () => {
      if (step > 0) {
        step--;
        updateQuiz();
      }
    });

    btnNext?.addEventListener("click", () => {
      if (!validateStep()) return;
      if (step < total - 1) {
        step++;
        updateQuiz();
      }
    });

    btnSubmit?.addEventListener("click", () => {
      if (!validateStep()) return;
      form.hidden = true;
      $(".quiz__nav", quiz).hidden = true;
      if (success) success.hidden = false;
      if (progress) progress.style.width = "100%";
    });

    updateQuiz();
  }

  /* ——— Phone mask (simple) ——— */
  $$('input[type="tel"]').forEach((input) => {
    input.addEventListener("input", () => {
      let d = input.value.replace(/\D/g, "");
      if (d.startsWith("8")) d = "7" + d.slice(1);
      if (!d.startsWith("7")) d = "7" + d;
      d = d.slice(0, 11);
      let out = "";
      if (d.length > 0) out = "+7";
      if (d.length > 1) out += " (" + d.slice(1, 4);
      if (d.length >= 4) out += ") " + d.slice(4, 7);
      if (d.length >= 7) out += "-" + d.slice(7, 9);
      if (d.length >= 9) out += "-" + d.slice(9, 11);
      input.value = out;
    });
  });

  /* ——— Forms without submit (visual only) ——— */
  $$("form[data-no-submit]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const box = $(".form-success", form.closest(".popup") || form);
      if (box) {
        form.hidden = true;
        box.hidden = false;
      }
    });
  });
})();
