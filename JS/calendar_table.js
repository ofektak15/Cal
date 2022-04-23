// global vars
var currentDate = new Date();
var year = currentDate.getFullYear();
var month = currentDate.getMonth() + 1 // a number (1-12). 1 = January
var numberOfDaysInMonth = new Date(year, month, 0).getDate(); // number of days in the current month
var startPoint = new Date(year, month - 1, 1).getDay() + 1;
var daysDiv = document.getElementsByClassName("days")[0]; // a div element where all the days are written
const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
document.getElementById("current_month").innerHTML = monthNames[month - 1];
document.getElementById("current_year").innerHTML = year;

get_days();

function get_days(){
    //b = eel.get_events()('ofek');
    //alert(b);

    startPoint = new Date(year, month - 1, 1).getDay(); // 0=Sunday
    numberOfDaysInMonth = new Date(year, month, 0).getDate(); // setting the number of days in the current month
    numberOfDaysInPrevMonth = new Date(year, month - 1, 0).getDate(); // setting the number of days in the prev month
    content = "";
    for (j = 1; j <= startPoint; j++) {
        content += "<li class='prev_next'>" + (numberOfDaysInPrevMonth - startPoint + j) + "</li>";

    }
    // TODO
    for (i = 1; i <= numberOfDaysInMonth; i++){
        if (i == currentDate.getDate() && month == currentDate.getMonth() + 1 && year == currentDate.getFullYear()){
            content += "<li onclick='return open_create_event_screen();' class='active'>" + i + "</li>";
        }
        else if (i > currentDate.getDate() && month < currentDate.getMonth() + 1 && year == currentDate.getFullYear()) { // TODO
            content += "<li onclick='return open_create_event_screen();'>" + i + "</li>";
        }
        else { // if the date has already passed - no ability to create event
            content += "<li>" + i + "</li>";
        }
    }

    numberOfDaysNextMonth = 7 - (new Date(year, month, 0).getDay() + 1);
    for (n = 1; n <= numberOfDaysNextMonth; n++) {
        content += "<li class='prev_next'>" + n + "</li>";
    }

    daysDiv.innerHTML = content;
    document.getElementById("current_month").innerHTML = monthNames[month - 1];
    document.getElementById("current_year").innerHTML = year;
}

function prev_month() {
    if (month == 1){ // if the month is January
        year = year - 1;
        month = 12;
    }
    else { // if the month is anything but January
        month = month - 1;
    }
    get_days();
}

function next_month() {
    if (month == 12) { // if the month is December
        year = year + 1;
        month = 1;
    }
    else { // if the month ia anything but December
        month = month + 1;
    }
    get_days();
}

function open_create_event_screen() {
    document.getElementsByClassName("calendar")[0].style.width = "60%";
    document.getElementById("create_event").style.display = "block";
}

function close_create_event_screen() {
    document.getElementsByClassName("calendar")[0].style.width = "100%";
    document.getElementById("create_event").style.display = "none";

    document.getElementById("event_name").value = "";
}

function create_event() {
    var event_name = document.getElementById('event_name').value;
    if (event_name == "") {
        document.getElementById("event_name_error").innerHTML = "You must enter the name of the event!";
        return false;
    }
    document.getElementById("event_name_error").innerHTML = "";

    eel.create_event(event_name, 'ofek'); // TODO: change 'ofek'
    close_create_event_screen();
}



function back_to_current_month() {
    year = currentDate.getFullYear();
    month = currentDate.getMonth() + 1 // a number (1-12). 1 = January
    numberOfDaysInMonth = new Date(year, month, 0).getDate(); // number of days in the current month
    get_days();
}





