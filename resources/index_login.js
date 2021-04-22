function onSignIn(googleUser) {

    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;

    registration(profile, id_token);
}

function registration(data, key) {
    $.ajax({
        url:"/registration",
        type:"POST",
        headers: { 
            "Accept" : "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
            "nome": data.getGivenName(),
            "cognome": data.getFamilyName(),
            "email": data.getEmail(),
            "profile_pic": data.getImageUrl(),
            "key": key
        },
        dataType:"json",
        success: function (result) {
            console.log(result)
            if (result.result == "OK") {
                document.cookie = "key=" + key + " path=/;";
                window.location.replace("index_home.html");
            }
            else console.log("Errore")
        }
    })
}

function onSuccess(googleUser) {
console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
}


function renderButton() {
gapi.signin2.render('signin', {
    'scope': 'profile email',
    'width': 350,
    'height': 50,
    'longtitle': true,
    'theme': 'dark',
    "onsuccess": onSignIn
});
}