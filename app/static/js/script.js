document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelector(".forms"),
          pwShowHide = document.querySelectorAll(".eye-icon"),
          links = document.querySelectorAll(".link");

    // Toggle password visibility
    pwShowHide.forEach(eyeIcon => {
        eyeIcon.addEventListener("click", () => {
            let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
            
            pwFields.forEach(password => {
                if(password.type === "password"){
                    password.type = "text";
                    eyeIcon.classList.replace("bx-hide", "bx-show");
                } else {
                    password.type = "password";
                    eyeIcon.classList.replace("bx-show", "bx-hide");
                }
            });
        });
    });

    // Toggle between login and signup forms
    links.forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault(); // Prevent default link behavior

            // Determine which form to show
            if (link.classList.contains("signup-link")) {
                forms.classList.add("show-signup");
            } else if (link.classList.contains("login-link")) {
                forms.classList.remove("show-signup");
            }
        });
    });
});
