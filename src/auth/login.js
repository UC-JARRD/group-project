function login() {
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    fetch('http://13.239.55.4:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'login': login,
            'password': password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('token', data.token);
            alert('Login successful!');
            // Optionally redirect the user after a successful login
            window.location.href = 'http://13.239.55.4:8000/'; // Redirect to a different page
        } else {
            alert('Login failed: ' + data.message); // Updated to display error messages
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error logging in');
    });
}
