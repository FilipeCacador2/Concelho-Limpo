document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".form-toggle button");
  const forms = document.querySelectorAll(".form-section");

  function showForm(formId, button) {
    forms.forEach(section => section.style.display = "none");
    document.getElementById(formId).style.display = "block";

    buttons.forEach(btn => btn.classList.remove("active"));
    button.classList.add("active");
  }

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const formId = button.getAttribute("data-form");
      showForm(formId, button);
    });
  });

  if (buttons.length > 0) {
    buttons[0].click();
  }
});

