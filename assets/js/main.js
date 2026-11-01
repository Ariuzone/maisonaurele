/* ============================================================
   MAISON AURÈLE — interactions
   Démonstration réalisée par Matrice Studio
   ============================================================ */
(function () {
  'use strict';

  document.documentElement.classList.add('reveal-ready');
  var noReveal = /[?&]noreveal\b/.test(location.search);
  if (noReveal) {
    window.addEventListener('DOMContentLoaded', function () {
      document.querySelectorAll('img[loading="lazy"]').forEach(function (i) { i.loading = 'eager'; });
    });
  }

  /* ---------- En-tête : voile au scroll, masquage intelligent ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var lastY = window.scrollY;
    var ticking = false;
    var onScroll = function () {
      var y = window.scrollY;
      header.classList.toggle('is-scrolled', y > 24);
      if (Math.abs(y - lastY) > 6) {
        header.classList.toggle('is-hidden', y > lastY && y > 320 && !document.body.classList.contains('nav-locked'));
        lastY = y;
      }
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();
  }

  /* ---------- Navigation mobile ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    var closeNav = function () {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      document.body.classList.remove('nav-locked');
    };
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
      document.body.classList.toggle('nav-locked', !open);
      if (!open) {
        var first = nav.querySelector('a');
        if (first) first.focus();
      }
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeNav();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { closeNav(); toggle.focus(); }
    });
  }

  /* ---------- Révélations au scroll ---------- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  if (noReveal || !('IntersectionObserver' in window) || revealEls.length === 0) {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Lightbox galerie ---------- */
  var lightbox = document.getElementById('lightbox');
  if (lightbox) {
    var lbImg = lightbox.querySelector('img');
    var lbCap = lightbox.querySelector('figcaption');
    var items = Array.prototype.slice.call(document.querySelectorAll('.gallery-item'));
    var current = -1;
    var openAt = function (i) {
      current = (i + items.length) % items.length;
      var btn = items[current];
      var img = btn.querySelector('img');
      lbImg.src = btn.getAttribute('data-full') || img.src;
      lbImg.alt = img.alt;
      lbCap.textContent = btn.getAttribute('data-caption') || img.alt;
      if (typeof lightbox.showModal === 'function') lightbox.showModal();
      lightbox.querySelector('.lightbox-close').focus();
    };
    items.forEach(function (btn, i) {
      btn.addEventListener('click', function () { openAt(i); });
    });
    lightbox.querySelector('.lightbox-close').addEventListener('click', function () { lightbox.close(); });
    lightbox.addEventListener('click', function (e) {
      var r = lightbox.getBoundingClientRect();
      var inFigure = e.target.closest('figure');
      if (!inFigure || (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom)) {
        lightbox.close();
      }
    });
    lightbox.querySelector('.lb-prev').addEventListener('click', function () { openAt(current - 1); });
    lightbox.querySelector('.lb-next').addEventListener('click', function () { openAt(current + 1); });
    lightbox.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') openAt(current + 1);
      if (e.key === 'ArrowLeft') openAt(current - 1);
    });
  }

  /* ---------- Utilitaires formulaires ---------- */
  var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var setInvalid = function (field, on) {
    var wrap = field.closest('.field') || field.closest('fieldset');
    if (wrap) wrap.classList.toggle('invalid', on);
    field.setAttribute('aria-invalid', on ? 'true' : 'false');
  };
  var validate = function (form) {
    var ok = true;
    var firstBad = null;
    form.querySelectorAll('[required]').forEach(function (el) {
      var bad = false;
      if (el.type === 'checkbox') { bad = !el.checked; }
      else if (el.type === 'email') { bad = !emailRe.test(el.value.trim()); }
      else { bad = el.value.trim().length < (el.getAttribute('data-min') ? parseInt(el.getAttribute('data-min'), 10) : 1); }
      if (el.type === 'date' && !bad) {
        var d = new Date(el.value + 'T12:00:00');
        var today = new Date(); today.setHours(0, 0, 0, 0);
        if (isNaN(d.getTime()) || d < today) bad = true;
      }
      setInvalid(el, bad);
      if (bad) { ok = false; if (!firstBad) firstBad = el; }
      el.addEventListener('input', function () { setInvalid(el, false); }, { once: true });
      el.addEventListener('change', function () { setInvalid(el, false); }, { once: true });
    });
    if (firstBad) firstBad.focus();
    return ok;
  };
  var showSuccess = function (formSel, successSel, fill) {
    var form = document.querySelector(formSel);
    var panel = document.querySelector(successSel);
    if (!form || !panel) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(form)) return;
      var submit = form.querySelector('[type="submit"]');
      if (submit) { submit.disabled = true; submit.textContent = 'Un instant…'; }
      window.setTimeout(function () {
        form.hidden = true;
        panel.hidden = false;
        if (fill) fill(form);
        panel.focus();
      }, 550);
    });
  };
  var fmtDate = function (iso) {
    try { return new Date(iso + 'T12:00:00').toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }); }
    catch (err) { return iso; }
  };

  /* ---------- Réservation ---------- */
  showSuccess('#form-reservation', '#reservation-success', function (form) {
    var out = document.querySelector('#reservation-recap');
    if (!out) return;
    var date = form.querySelector('#res-date').value;
    var day = new Date(date + 'T12:00:00').getDay();
    if (day === 0 || day === 1) {
      var wrap = document.querySelector('#res-date').closest('.field');
      if (wrap) {
        wrap.classList.add('invalid');
        var err = wrap.querySelector('.error');
        if (err) err.textContent = 'La maison est fermée dimanche et lundi.';
      }
      form.hidden = false;
      document.querySelector('#reservation-success').hidden = true;
      var submit = form.querySelector('[type="submit"]');
      if (submit) { submit.disabled = false; submit.textContent = 'Confirmer la demande'; }
      return;
    }
    out.innerHTML =
      '<li><strong>Demander</strong> ' + form.querySelector('#res-name').value.replace(/</g, '&lt;') + '</li>' +
      '<li><strong>Date</strong> ' + fmtDate(date) + '</li>' +
      '<li><strong>Service</strong> ' + (form.querySelector('#res-service').selectedOptions[0].text) + '</li>' +
      '<li><strong>Couverts</strong> ' + form.querySelector('#res-guests').value + '</li>';
  });

  /* ---------- Contact ---------- */
  showSuccess('#form-contact', '#contact-success', function (form) {
    var subject = 'Maison Aurèle — ' + form.querySelector('#ct-subject').selectedOptions[0].text;
    var body = form.querySelector('#ct-message').value.replace(/</g, '&lt;');
    var name = form.querySelector('#ct-name').value.replace(/</g, '&lt;');
    var link = document.querySelector('#contact-mailto');
    if (link) {
      link.href = 'mailto:matricestudio@protonmail.com?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(name + ' :\n\n' + body);
    }
  });

  /* ---------- Formulaire bon cadeau ---------- */
  showSuccess('#form-cadeau', '#cadeau-success', function () {});

  /* ---------- Newsletter (pied de page) ---------- */
  var nl = document.querySelector('.newsletter-form');
  if (nl) {
    nl.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = nl.querySelector('input[type="email"]');
      var note = nl.parentElement.querySelector('.newsletter-note');
      if (!emailRe.test(input.value.trim())) {
        note.textContent = 'Merci d\u2019indiquer une adresse e-mail valide.';
        input.focus();
        return;
      }
      note.textContent = 'Merci\u00a0! Vous recevrez les nouvelles de la maison \u00e0 l\u2019adresse ' + input.value.trim() + '.';
      note.classList.add('is-ok');
      nl.reset();
    });
  }
})();
