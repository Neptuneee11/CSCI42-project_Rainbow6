function updateClock() {
    var currentTime = new Date();
    var ap = (hrs < 12) ? "AM" : "PM";

    var hrs = currentTime.getHours();
    var min = currentTime.getMinutes();
    var sec = currentTime.getSeconds();
    
    hrs = (hrs > 12) ? hrs - 12 : hrs;
    hrs = (hrs === 0) ? 12 : hrs;
    min = (min < 10 ? "0" : "") + min;
    sec = (sec < 10 ? "0" : "") + sec;

    var totalTime = hrs + ":" + min + ":" + sec + " " + ap;

    document.getElementById("clock").textContent = totalTime;

}

setInterval(updateClock, 1000);