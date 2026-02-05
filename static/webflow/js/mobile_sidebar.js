document.addEventListener('DOMContentLoaded', function () {
    var offcanvas = new bootstrap.Offcanvas(document.getElementById('mobile-sidebar'));

    // Variables for swipe detection
    let startX = 0;
    let startY = 0;
    let isSwiping = false;

    // Detect swipe gesture anywhere on the screen
    document.addEventListener('touchstart', function(e) {
        // Only process the swipe when the sidebar is not visible
        if (!offcanvas._isShown) {
            startX = e.changedTouches[0].screenX;
            startY = e.changedTouches[0].screenY;
            isSwiping = false;  // Reset swipe flag
        }
    });

    document.addEventListener('touchmove', function(e) {
        isSwiping = true;  // We're moving, so let's mark it as a swipe in progress
    });

    document.addEventListener('touchend', function(e) {
        const endX = e.changedTouches[0].screenX;
        const endY = e.changedTouches[0].screenY;
        const diffX = endX - startX;
        const diffY = endY - startY;

        // Only consider horizontal swipe (left-right)
        if (isSwiping && Math.abs(diffX) > Math.abs(diffY)) {
            if (diffX > 100) {  // Swipe right: open the sidebar
                offcanvas.show();
            } else if (diffX < -100) {  // Swipe left: close the sidebar
                offcanvas.hide();
            }
        }
        isSwiping = false;  // Reset swipe flag after the action
    });
});