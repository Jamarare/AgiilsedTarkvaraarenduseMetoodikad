document
  .getElementById("feedback-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Aitäh tagasiside eest!");
    this.reset();
  });
