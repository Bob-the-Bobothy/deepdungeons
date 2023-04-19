// Get a reference to the collapse-nav button and the nav div
const collapseNavButton = document.getElementById("collapse-nav");
const navDiv = document.getElementById("nav");

// Add a click event listener to the button
collapseNavButton.addEventListener("click", function() {
  // Toggle the "collapsed" class on the nav div
  navDiv.classList.toggle("collapsed");
});
