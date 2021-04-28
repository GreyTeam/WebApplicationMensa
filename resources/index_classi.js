$(document).ready(function () {
    $.ajax({
        url:"/classi/lista",
        type:"POST",
        headers: { 
            "Accept" : "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
            "key": getCookie("key"),
        },
        dataType:"json",
        success: function(result) {
            select = document.getElementById("classi")
            console.log(result.classi)
            for (let i = 0; i < result.classi.length; i++) {
                console.log(result.classi[i])
                option = document.createElement("option")
                option.text = result.classi[i]
                option.value = result.classi[i]
                option.classList.add("option")
                select.add(option)    
            }
            $('body').addClass('loaded');
        }
    })

    $("#back").click(function () {
        
	})
})

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift()
    }
}
