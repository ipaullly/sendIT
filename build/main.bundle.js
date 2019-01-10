'use strict';

document.getElementById('signupbutton').addEventListener('click', signUp);

function signUp() {
    var email = document.getElementById('signemail').nodeValue;
    var password = document.getElementById('signpassword').nodeValue;

    fetch('https://sendit-versiontwo.herokuapp.com/auth/v2/signup', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    }).then(function (res) {
        return res.json();
    }).then(function (data) {
        return console.log(data);
    });
}
