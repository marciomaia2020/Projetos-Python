document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const profileUrlInput = document.getElementById("profile_url");
    const accessTokenInput = document.getElementById("access_token");
    const errorMessage = document.createElement("div");
    errorMessage.classList.add("error-message");

    form.addEventListener("submit", function(event) {
        errorMessage.textContent = ''; // Clear previous errors
        event.preventDefault(); // Prevent form from submitting by default

        const profileUrl = profileUrlInput.value.trim();
        const accessToken = accessTokenInput.value.trim();

        if (!profileUrl || !accessToken) {
            errorMessage.textContent = "Por favor, preencha todos os campos.";
            form.appendChild(errorMessage);
            return;
        }

        // Optional: Validate the URL format
        const urlRegex = /^(https:\/\/)?(www\.)?facebook\.com\/([a-zA-Z0-9.]+)$/;
        if (!urlRegex.test(profileUrl)) {
            errorMessage.textContent = "Por favor, insira uma URL válida do Facebook.";
            form.appendChild(errorMessage);
            return;
        }

        // If everything is valid, submit the form
        form.submit();
    });
});
