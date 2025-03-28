document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });
});

// document.addEventListener("DOMContentLoaded", function() {
//     const header = document.querySelector("header");
//     const content = document.querySelector(".main-content");

//     // If we're not on the homepage, set padding dynamically
//     if (content && !document.body.classList.contains('home-page')) {
//         content.style.paddingTop = header.offsetHeight + "px"; // Adjust padding based on header height
//     }
// });
