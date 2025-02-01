document.addEventListener('DOMContentLoaded', function () {
    const donorForm = document.getElementById('donor-registration-form');
    const generateOtpButton = document.getElementById('generate-otp');
    const otpRow = document.getElementById('otp-row');

    if (donorForm) {
        donorForm.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Form submitted successfully!');
        });

        donorForm.addEventListener('reset', function () {
            alert('Form reset successfully!');
        });

        generateOtpButton.addEventListener('click', function () {
            otpRow.style.display = 'flex';
        });
    }

    const passwordUpdateForm = document.getElementById('password-update-form');
    const updateMessage = document.getElementById('update-message');

    if (passwordUpdateForm) {
        passwordUpdateForm.addEventListener('submit', function (e) {
            e.preventDefault();
            // Here you can add the logic to update the password in your backend.
            // For now, we just show the update message.
            updateMessage.style.display = 'block';
        });

        passwordUpdateForm.addEventListener('reset', function () {
            alert('Form reset successfully!');
        });
    }

    const loginForm = document.getElementById('login-form');
    const forgotPasswordLink = document.getElementById('forgot-password-link');
    const passwordUpdateMessage = document.getElementById('password-update-message');

    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Form submitted successfully!');
        });

        loginForm.addEventListener('reset', function () {
            alert('Form reset successfully!');
        });

        forgotPasswordLink.addEventListener('click', function (e) {
            e.preventDefault();
            passwordUpdateMessage.style.display = 'block';
            // Here you can add the logic to send the password update email in your backend.
        });
    }
});
