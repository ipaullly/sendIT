const registerButton = document.getElementById('signupbutton');
const loginButton = document.getElementById('loginbut');
const createOrderButton = document.getElementById('createparcel');
const userOrderButton = document.getElementById('userorders');

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
                sessionStorage.setItem( 'token', myJson.data );
                sessionStorage.setItem( 'loginResponse', myJson.message );                     
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

function decodeJwt (token) {
    let base64Url = token.split('.')[1];
    let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(window.atob(base64));
}

function loginResponse(){
    let response = sessionStorage.getItem( 'loginResponse' );
    let output = `<p style="background: #004e00;color: white;text-align: center;padding: 20px;font-family: 'Boogaloo', cursive;">${response}</p>`;
    return document.getElementById('redirectedlogin').innerHTML = output;
}


function createParcel(){
    let output;
    let token = sessionStorage.getItem( 'token' ).replace("'", "");
    token = token.substr(0, token.length-1); 
    fetch('https://sendit-versiontwo.herokuapp.com/api/v2/parcels', {
        mode: 'cors',
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Access-Control-Allow-Origin": null,
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({
            item: document.getElementById('parcelname').value,
            pickup: document.getElementById('parcelpickup').value,
            dest: document.getElementById('parceldestination').value,
            pricing: document.getElementById('parcelprice').value,
        })
    })
    .then((res) => {
        if (res.ok){
            return res.json().then((myJson) => {
                output = `<p style="background: #004e00;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('redirectedlogin').innerHTML = output;
            })
        }
        if (res.status == 400){
            return res.json().then((myJson) => {
                output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('redirectedlogin').innerHTML = output;
            })
        }
    });

}

function retrieveUserOrders(){
    let token = sessionStorage.getItem( 'token' ).replace("'", "");
    token = token.substr(0, token.length-1); 
    let decodedToken = decodeJwt(token);
    decodedTokenId = Object.values(decodedToken)[2];
    fetch('https://sendit-versiontwo.herokuapp.com/api/v2/users/'+decodedTokenId+'/parcels', {
        mode: 'cors',
        method: 'GET',
        headers: {
            Accept: "application/json",
            "Access-Control-Allow-Origin": null,
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": "Bearer " + token
        }
    })
    .then((res) => {
        if (res.ok){
            return res.json().then((myJson) => {
                let output;
                let orderList = myJson.data;
                orderList = orderList[Object.keys(orderList)[0]]; 
                orderList.forEach((order) => {
                    output += `
                    <li>
                        <a href="order_display_page.html"><h3>${order.item_name}</h3></a>
                        <p>Present Location: ${order.current_location}</p>
                        <p>Destination: ${order.destination}</p>
                        <p>Order Id: ${order.order_id}</p>
                    </li>
                    `;
                });
                let message = `<p style="background: #004e00;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('redirectedlogin').innerHTML = message,
                document.getElementById('singleuserorders').innerHTML = output;

            })
        }
        if (res.status == 400){
            return res.json().then((myJson) => {
                output = `<p style="background: #a60000;color: white;text-align: center;padding: 20px;font-size: 1.3em;font-family: 'Boogaloo', cursive;">${myJson.message}</p>`;
                return document.getElementById('redirectedlogin').innerHTML = output;
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
if (createOrderButton){
    createOrderButton.addEventListener('click', createParcel);
}
if (userOrderButton){
    userOrderButton.addEventListener('click', retrieveUserOrders);
}