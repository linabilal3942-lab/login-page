// Login
document.getElementById("loginForm").addEventListener("submit", function(e) {

    e.preventDefault();

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("loginUsername").value,
            password: document.getElementById("loginPassword").value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.message;
    });

});


// Register
document.getElementById("registerForm").addEventListener("submit", function(e) {

    e.preventDefault();

    fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("registerUsername").value,
            password: document.getElementById("registerPassword").value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.message;
    });

});