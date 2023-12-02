const scrollBtn = document.querySelector(".scroll-to-top");

window.addEventListener("scroll", () => {
  // show the button when the user scrolls down
  if (window.pageYOffset > 250) {
    scrollBtn.classList.add("visible");
  } else {
    scrollBtn.classList.remove("visible");
  }
});

scrollBtn.addEventListener("click", (event) => {
  event.preventDefault();
  // scroll to the top of the page when the button is clicked
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
