document.getElementById('signupbutton').addEventListener('click', signUp);

function signUp(){

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
    .then((res) => res.json())
    .then((data) => {
        let output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;">${data.message}</p>`;
        document.getElementById('signupresponse').innerHTML = output;
    });

    //.catch((error) => console.log('Request failed', error));
}