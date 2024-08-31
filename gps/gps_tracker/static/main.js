let map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 28.6139, lng: 77.2090 }, // Default center location
        zoom: 15
    });
    
    updateLocation();
}

function updateLocation() {
    fetch('/gps-data')
        .then(response => response.json())
        .then(data => {
            if (data.latitude && data.longitude) {
                const position = new google.maps.LatLng(data.latitude, data.longitude);
                new google.maps.Marker({
                    position: position,
                    map: map,
                    title: "Bus Location"
                });
                map.setCenter(position);
            }
        })
        .catch(error => console.error('Error fetching GPS data:', error));

    setTimeout(updateLocation, 5000); // Update every 5 seconds
}
