function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
	
	console.log('Email: ' + profile.getEmail()); 
  
	if(!profile.getEmail().includes('@istitutopilati.it')){
	    alert('Email non valida!');
	}
	else {
        registration(profile, id_token);
    }
    
}

function registration(data, key) {
    console.log(key);
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
                setCookie("key", key, "");
                $(".not-logged").addClass("logged")
                $(".not-logged").removeClass("not-logged")
                $("#join").removeAttr("disabled")
            }
            else console.log("Errore")
        }
    })
	
	$("#join").click(function () {
        window.location.replace("index_home.html");
	})
	
	$('body').addClass('loaded');
}

function renderButton() {
    gapi.signin2.render('signin', {
        'scope': 'profile email',
        'width':250,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        "onsuccess": onSignIn
    });
    $('body').addClass('loaded');
}

function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";max-age=" + 30*24*60*60; + ";path=/";
}

















