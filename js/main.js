const registerButton = document.getElementById('signupbutton');
const loginButton = document.getElementById('loginbut');

function signUp(){
    let output;
    fetch('https://sendit-versiontwo.herokuapp.com/auth/v2/signup', {
        mode: 'cors',
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json; charset=UTF-8"
        },
        body: JSON.stringify({
            email: document.getElementById('signemail').value,
            password: document.getElementById('signpassword').value
        })
    })
    .then((res) => {
        if (res.ok){
            return res.json().then((data) => {
                output = `<p style="background: #004e00;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${data.message}</p>`;
                return document.getElementById('signupresponse').innerHTML = output;
            })
        }
        if (res.status == 400){
            return res.json().then((data) => {
                output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${data.message}</p>`;
                return document.getElementById('signupresponse').innerHTML = output;
            })
        }
    });
}

function logIn(){
    let output;
    fetch('https://sendit-versiontwo.herokuapp.com/auth/v2/login', {
        mode: 'cors',
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json; charset=UTF-8"
        },
        body: JSON.stringify({
            email: document.getElementById('loginemail').value,
            password: document.getElementById('loginpass').value
        })
    })
    .then((res) => {
        if (res.ok){
            redirect: window.location.assign("./orders_display_users.html")
            return res.json().then((myJson) => {
                localStorage.setItem( 'token', myJson.data );
                localStorage.setItem( 'loginResponse', myJson.message );                     
            })
        }
        if (res.status == 400){
            return res.json().then((myJson) => {
                output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('loginresponse').innerHTML = output;
            })
        }
        if (res.status == 401){
            return res.json().then((myJson) => {
                output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('loginresponse').innerHTML = output;
            })
        }
    });
}

if (registerButton){
    registerButton.addEventListener('click', signUp);
}
if (loginButton){
    loginButton.addEventListener('click', logIn);
}