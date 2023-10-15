console.log('WORKS WORKS WORKS');

  // Add a click event listener to the "frame-1" image
  const frame1Image = document.querySelector(".frame-1");

  frame1Image.addEventListener("click", function() {
    // Redirect to the same URL as the "Create Your Story" button
    window.location.href = "/generate_image";
  });