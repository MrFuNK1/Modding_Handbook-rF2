// This script will provide some touch functions for mobile use.

document.addEventListener('DOMContentLoaded', function() {
  var touchstartX = null;
  var touchmoveX = null;
  var menuButton = document.querySelector('.wy-nav-top');

  function handleTouchStart(e) {
    touchstartX = e.touches[0].clientX;
  }

  function handleTouchMove(e) {
    touchmoveX = e.touches[0].clientX;
    var touchDistance = touchmoveX - touchstartX;
    if (touchDistance > 180) { // adjust the threshold value as needed
      document.querySelector('.wy-nav-side').classList.add('shift');
      document.querySelector('.wy-nav-content-wrap').classList.add('shift');
      menuButton.click(); // trigger click event
    } else if (touchDistance < -180) { // adjust the threshold value as needed
      document.querySelector('.wy-nav-side').classList.remove('shift');
      document.querySelector('.wy-nav-content-wrap').classList.remove('shift');
    }
  }

  document.body.addEventListener('touchstart', handleTouchStart);
  document.body.addEventListener('touchmove', handleTouchMove);
});
