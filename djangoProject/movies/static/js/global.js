
/* GO TO TOP */
const goToTopBtn = document.getElementById("goToTopBtn");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            goToTopBtn.style.display = "block";
        } else {
            goToTopBtn.style.display = "none";
        }
    });

    goToTopBtn.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
    });
});


