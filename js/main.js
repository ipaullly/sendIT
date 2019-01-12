document.getElementById('signupbutton').addEventListener('click', signUp);

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

