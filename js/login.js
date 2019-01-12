document.getElementById('loginbut').addEventListener('click', logIn);

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
            /*return res.json().then((myJson) => {
                let token = myJson.data;
                let message = myJson.message;
                return token, message;     
            }).catch((error) => {
                console.log(error);
            }) */
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
//export { token, message };