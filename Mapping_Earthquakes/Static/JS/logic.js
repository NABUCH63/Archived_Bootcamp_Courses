// Create a base layer that holds both maps.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/satellite-streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: API_KEY
});

let streets = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: API_KEY
});

let navNight = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/navigation-night-v1',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: API_KEY
});

let baseMaps = {
    "Streets": streets,
    "Satellite": satelliteStreets,
    "Navigation Night": navNight
  };

  var map = L.map("map", {
    center: [44, -80],
    zoom: 2,
    layers: [streets]
});

// SET API URLS
var earthquakesAPI = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
var tectonicPlates = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";
var majorEarthquakes = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"

// create function to size radius based on magnitude
function getRadius(magnitude) {
    if (magnitude === 0) {
        return 1;
    }
    return magnitude * 4;
};

// Create Color Function
function getColor(magnitude) {
    if (magnitude >=6) {
        return "#000000";
    }
    if (magnitude > 5) {
    return "#ea2c2c";
    }
    if (magnitude > 4) {
    return "#ea822c";
    }
    if (magnitude > 3) {
    return "#ee9c00";
    }
    if (magnitude > 2) {
    return "#eecc00";
    }
    if (magnitude > 1) {
    return "#d4ee00";
    }
    return "#98ee00";
}

// create function to define styling of earthquake marker using setRadius function
function styleInfo1(feature) {
    return {
        opacity: 1,
        fillOpacity: 1,
        fillColor: getColor(feature.properties.mag),
        color: "#000000",
        radius: getRadius(feature.properties.mag),
        stroke: true,
        weight: 0.5
    };
};

// Create function for plates styling
function styleInfo2(feature) {
    return {
        opacity: 1,
        color: "hotpink",
        borderColor: "black",
        stroke: true,
        weight: 1.5
    };
};

// ADD EARTHQUAKE DATA
d3.json(earthquakesAPI).then(function(earthquakesAPI) {
    L.geoJSON(earthquakesAPI, {
        pointToLayer: function(feature, latlng) {
                return L.circleMarker(latlng).bindPopup("<h5>Location: " + feature.properties.place + "<hr> Magintude: " + feature.properties.mag + "</h5>")
            },
        style: styleInfo1
    }).addTo(allearthquakes);
});

d3.json(majorEarthquakes).then(function(majorEarthquakes) {
    L.geoJSON(majorEarthquakes, {
        pointToLayer: function(feature, latlng) {
                return L.circleMarker(latlng).bindPopup("<h5>Location: " + feature.properties.place + "<hr> Magintude: " + feature.properties.mag + "</h5>")
            },
        style: styleInfo1
    }).addTo(majorquakes);
});

// ADD TECTONIC PLATES DATA
d3.json(tectonicPlates).then(function(tectonicPlates) {
    L.geoJSON(tectonicPlates, {
        pointToLayer: function(feature, latlng) {
                return L.circleMarker(latlng)
            },
        style: styleInfo2
    }).addTo(plates);
});

var allearthquakes = new L.LayerGroup();
var majorquakes = new L.LayerGroup();
var plates = new L.LayerGroup();

allearthquakes.addTo(map);
majorquakes.addTo(map);
plates.addTo(map);

var overlays = {
    "All Earthquakes": allearthquakes,
    "Major Earthquakes": majorquakes,
    "Tectonic Plates": plates
};

L.control.layers(baseMaps, overlays).addTo(map);

// create legend control object

var legend = L.control({
    position: "bottomright"
});

legend.onAdd = function() {
    let div = L.DomUtil.create("div", "info legend");


    const magnitudes = [0,1,2,3,4,5,6];
    const colors = [ 
        "#98ee00",
        "#d4ee00",
        "#eecc00",
        "#ee9c00",
        "#ea822c",
        "#ea2c2c",
        "#000000",
    ];

    for (var i = 0; i < magnitudes.length; i++) {
        div.innerHTML +=
            "<i style='background: " + colors[i] + "'></i> " +
            magnitudes[i] + (magnitudes[i + 1] ? "&ndash;" + magnitudes[i + 1] + "<br>" : "+");
        }
    return div;
};

legend.addTo(map)

