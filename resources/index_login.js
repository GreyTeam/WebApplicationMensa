$(document).ready(function () {

	$("#submit").click(function () {
		console.log("Cliccato");
		let data = {};
		data.nome = document.getElementById("fname").value;
		data.cognome = document.getElementById("lname").value;
		$.post(
			"/prenota", data, function (result) {
				console.log(result)
			}
		)
	})
})


function onSignIn(googleUser) {
    // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);

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