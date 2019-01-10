document.getElementById('signupbutton').addEventListener('click', signUp);

function signUp(){
    let email = document.getElementById('signemail').nodeValue;
    let password = document.getElementById('signpassword').nodeValue;

    fetch('https://sendit-versiontwo.herokuapp.com/auth/v2/signup', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({email:email, password:password})
    })
    .then((res) => res.json())
    .then((data) => console.log(data))
}