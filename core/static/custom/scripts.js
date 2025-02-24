
  window.addEventListener('scroll', function () {
  const elements = document.querySelectorAll('.fade-up');
  const windowHeight = window.innerHeight;

  elements.forEach(function (element) {
    const elementTop = element.getBoundingClientRect().top;

    if (elementTop < windowHeight) {
      element.classList.add('visible');
    }
  });
});