var googleUser = {};
  var startApp = function() {
    gapi.load('auth2', function(){
      // Retrieve the singleton for the GoogleAuth library and set up the client.
      auth2 = gapi.auth2.init({
        client_id: 'YOUR_CLIENT_ID.apps.googleusercontent.com',
        cookiepolicy: 'single_host_origin',
        // Request scopes in addition to 'profile' and 'email'
        //scope: 'additional_scope'
      });
      attachSignin(document.getElementById('customBtn'));
    });
  };

    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
	
	console.log('Email: ' + profile.getEmail()); 
  
	if(!profile.getEmail().includes('@istitutopilati.it')){
	alert('Email non valida!');
	}
	
    registration(profile, id_token);
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
                $("#join").removeAttr("disabled")
            }
            else console.log("Errore")
        }
    })
	
	$("#join").click(function () {
        $.ajax({
            url:"/user/info",
            type:"POST",
            headers: { 
                "Accept" : "application/json; charset=utf-8",
                "Content-Type": "application/json; charset=utf-8",
                "key": getCookie("key")
            },
            dataType:"json",
            success: function (result) {
                if (result.result == "OK") {
                    if (result.classe == null)
                        document.location.replace("/index_classi.html")
                    else 
                        document.location.replace("/index_home.html")
                }
            }
	    })
    })

    $(".close").click(function () {
        $(".modal-content").remove()
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

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift()
    }
}

















