console.log('WORKS WORKS WORKS');

document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the button element by its id
    const clickButton = document.getElementById("clickButton");

    // Add a click event listener to the button
    clickButton.addEventListener("click", () => {
        console.log("button worked?");
    });
});


