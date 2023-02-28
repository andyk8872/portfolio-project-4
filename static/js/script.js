// copyright
document.getElementById("copyright").textContent=(new Date().getFullYear());

// map
var map = L.map('map').setView([54.27, -8.4961], 14 );


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker = L.marker([54.2673456244, -8.4723157056]).addTo(map);

marker.bindPopup("<b>TEAM | BUILD</b>").openPopup();