/*
$(document).ready(function () {

    $("#back").click(function () {
        window.location.replace("index_home.html");
	})
})

$.ajax({
    url:"/chronology",
    type:"POST",
    headers: { 
        "Accept" : "application/json; charset=utf-8",
        "Content-Type": "application/json; charset=utf-8",
        "key": getCookie("key"),
    },
    dataType:"json",
    success: function(result) {

        if (result.result == "OK") {
            console.log(result.chronology)
            table = document.getElementById("table")
            for (let i = 0; i < result.chronology.length; i++) {
                var tr = document.createElement('tr');

                var td = document.createElement('td');
                td.innerText = result.chronology[i];
                td.classList.add("cell");

                var tstatus = document.createElement('td');
                status = getStatus(result.chronology[i]);
                console.log(status)
                tstatus.innerText = status;
                tstatus.classList.add("cell");
          
                tr.appendChild(td);
                tr.appendChild(tstatus);
                table.appendChild(tr);
            }
        }
        else console.log(result.message)
    }
})

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift()
    }
}

function parseDate(date) {
    return new Date(currentDate.getFullYear(), parseInt(date.slice(3, 5)) - 1, date.slice(0, 2));
}

function isToday(date) {
    currentDate = new Date();
    parsedDate = parseDate(date);
    console.log(currentDate);
    console.log(parsedDate);
    return currentDate.getDate() == parsedDate.getDate();
}

function getStatus(date) {
    if (isToday(date)) {
        currentTime = new Date().getHours();
        return currentTime < 8 ? "Prenotazione non inviata" : "Prenotazione arrivata"
    }
    else if (parseDate(date) > new Date())
        return "Non ancora prenotato"
    else return "Prenotazione terminata"
}



calendario*/

    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    function drawCalendarMonths()
    {
        for(var i = 0; i < months.length; i++)
        {
            var doc = document.createElement("div");
            doc.innerHTML = months[i];
            doc.classList.add("dropdown-item");

            doc.onclick = (function () {
                var selectedMonth = i;
                return function ()
                {
                    month = selectedMonth;
                    document.getElementById("curMonth").innerHTML = months[month];
                    loadCalendarDays();
                    return month;
                }
            })();

            document.getElementById("months").appendChild(doc);
        }
    }
	
	
	 function daysInMonth(month, year)
    {
        let d = new Date(year, month+1, 0);
        return d.getDate();
    }

    function loadCalendarDays()
    {
        document.getElementById("calendarDays").innerHTML = "";

        var tmpDate = new Date(year, month, 0);
        var num = daysInMonth(month, year);
        var dayofweek = tmpDate.getDay();       // find where to start calendar day of week

	  // create day prefixes

     for(var i = 0; i <= dayofweek; i++)
        {
            var d = document.createElement("div");
            d.classList.add("day");
            d.classList.add("blank");
            document.getElementById("calendarDays").appendChild(d);
        }


 function loadYears()
    {
        // whichever date range makes the most sense
        var startYear = 1900;
        var endYear = 2022;

        for(var i = startYear; i <= endYear; i++)
        {
            var doc = document.createElement("div");
            doc.innerHTML = i;
            doc.classList.add("dropdown-item");

            doc.onclick = (function(){
                var selectedYear = i;
                return function(){
                    year = selectedYear;
                    document.getElementById("curYear").innerHTML = year;
                    loadCalendarDays();
                    return year;
                }
            })();

            document.getElementById("years").appendChild(doc);
        }
    }
	
	
	     // render the rest of the days
        for(var i = 0; i < num; i++)
        {
            var tmp = i + 1;
            var d = document.createElement("div");
            d.id = "calendarday_" + i;
            d.className = "day";
            d.innerHTML = tmp;
            document.getElementById("calendarDays").appendChild(d);
        }

        var clear = document.createElement("div");
        clear.className = "clear";
        document.getElementById("calendarDays").appendChild(clear);
    }
	
	
	
	    var selectedDays = new Array();
        var mousedown = false;
		
		
		
		function loadCalendarDays() {
    document.getElementById("calendarDays").innerHTML = "";

    var tmpDate = new Date(year, month, 0);
    var num = daysInMonth(month, year);
    var dayofweek = tmpDate.getDay();       // find where to start calendar day of week

    for (var i = 0; i <= dayofweek; i++) {
        var d = document.createElement("div");
        d.classList.add("day");
        d.classList.add("blank");
        document.getElementById("calendarDays").appendChild(d);
    }

    for (var i = 0; i < num; i++) {
        var tmp = i + 1;
        var d = document.createElement("div");
        d.id = "calendarday_" + tmp;
        d.className = "day";
        d.innerHTML = tmp;
        d.dataset.day = tmp;              // easier to retrieve the date

        /* ****************** Click Event ********************** */
        d.addEventListener('click', function(){
            this.classList.toggle('selected');

            if (!selectedDays.includes(this.dataset.day))
                selectedDays.push(this.dataset.day);

            else
                selectedDays.splice(selectedDays.indexOf(this.dataset.day), 1);
        });
        /* **************************************************** */

        document.getElementById("calendarDays").appendChild(d);
    }

    var clear = document.createElement("div");
    clear.className = "clear";
    document.getElementById("calendarDays").appendChild(clear);
}



/* ****************** Click Event ********************** */
        d.addEventListener('click', function(){
            this.classList.toggle('selected');

            if (!selectedDays.includes(this.dataset.day))
                selectedDays.push(this.dataset.day);

            else
                selectedDays.splice(selectedDays.indexOf(this.dataset.day), 1);
        });
        /* **************************************************** */
    
	
	
         d.addEventListener('mousedown', function(e){
            e.preventDefault();
            mousedown = true;
        });
    
    
	
	
        d.addEventListener('mouseup', function(e){
            e.preventDefault();
            mousedown = false;
        });
		
		d.addEventListener('mousemove', function(e){
           e.preventDefault();
            if (mousedown)
            {
                this.classList.add('selected');

                if (!selectedDays.includes(this.dataset.day))
                    selectedDays.push(this.dataset.day);
            }
        });
    
