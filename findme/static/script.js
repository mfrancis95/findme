var map, marker;

var request = data();

function init() {
    request.then(function(json) {
        document.getElementById("lastUpdated").innerHTML = json.last_updated;
        map = new google.maps.Map(document.getElementById("map"), {
            center: json.position,
            zoom: 16
        });
        marker = new google.maps.Marker({
            map: map,
            position: json.position,
            title: "My Position"
        });
        setInterval(function() {
            data().then(update);
        }, 60000);
    });
}

function data() {
    return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", function() {
            if (xhr.status === 200) {
                resolve(JSON.parse(xhr.responseText));
            }
            else {
                reject();
            }
        });
        xhr.open("GET", "/data");
        xhr.send();
    });
}

function update(json) {
    document.getElementById("lastUpdated").innerHTML = json.last_updated;
    marker.setPosition(new google.maps.LatLng(json.position.lat, json.position.lng));
    map.setCenter(marker.getPosition());
}
