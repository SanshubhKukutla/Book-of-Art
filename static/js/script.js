console.log('WORKS WORKS WORKS');

document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the <img> element by its id
    const clickableImage = document.getElementById("clickablePrintConsole");
    console.log(clickableImage); // Check if this returns the image element

    // Add a click event listener to the image
    clickableImage.addEventListener("click", () => {
        console.log("Image clicked!");
    });

    try {
        // Your code here
    } catch (error) {
        console.log("An error occurred:", error);
    }
});

// Get a reference to the button element by its id
const clickButton = document.getElementById("clickButton");

// Add a click event listener to the button
clickButton.addEventListener("click", () => {
    console.log("Button clicked!");
});