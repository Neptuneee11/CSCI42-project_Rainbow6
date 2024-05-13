function domReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1000);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}
 
domReady(function () {
 
    // If found you qr code
    function onScanSuccess(decodeText, decodeResult) {
        alert("Successfully scanned qr code");
        // send a post request to the django server to change the state of the bike

        const csrftoken = getCookie('csrftoken'); // function to retrieve cookie value
        fetch(decodeText, {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
            'state' : 'rented'
        },
        body: JSON.stringify({ "id": 78912 })
        })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))

        window.location.assign(decodeText);
    }
 
    let htmlscanner = new Html5QrcodeScanner(
        "my-qr-reader",
        { fps: 10, qrbos: 250 }
    );
    htmlscanner.render(onScanSuccess);
});