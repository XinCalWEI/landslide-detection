---
layout: default
title: Datasets
---

<head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.1/dist/leaflet.css" />
    <style>
        html, body {
            height: 100%;
            margin: 0;  
            padding: 0;
        }
        #map {
            height: calc(100vh - 60px); 
            width: 100%;
        }
    </style>
</head>

<main>
    <!-- Create a container for the map -->
    <div id="map"></div>
</main>

<!-- Leaflet.js Map Setup -->
<script src="https://unpkg.com/leaflet@1.9.1/dist/leaflet.js"></script>
<script>
    // Initialize map
    const map = L.map('map').setView([0, 0], 5); // Center of the globe, zoom level 2
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    {% for dataset in site.data.dataset %}
        // Log coordinates to check if data is parsed
        console.log("Dataset coordinates:", {{ dataset.coordX }}, {{ dataset.coordY }});

        const lat = {{ dataset.coordY }};
        const lon = {{ dataset.coordX }};
        
        // Create marker for each dataset point
        const marker = L.marker([lat, lon]).addTo(map);
        
        // Build popup content dynamically, only including non-empty fields
        let popupContent = `
            <strong>Title:</strong> {{ dataset.title }}<br>
            <strong>Description:</strong> {{ dataset.description }}<br>
            <strong>Country:</strong> {{ dataset.country }}<br>
            {% if dataset.linkDownload != "Upon Request" and dataset.linkDownload != "" %}
                <a href="{{ dataset.linkDownload }}">Link to Download</a><br>
            {% elsif dataset.linkDownload == "Upon Request" %}
                <a>Upon Request to Author</a><br>
            {% endif %}
            <strong>Number of Landslide Records:</strong> {{ dataset.numLandslideRecords }}<br>
            <strong>Dataset Details:</strong> {{ dataset.datasetDetails }}<br>
            <strong>Landslide Inventory Type:</strong> {{ dataset.inventoryType }}<br>
            {% if dataset.linkPaper != "" and dataset.linkPaper != null and dataset.linkPaper != "nan" %}
                <a href="{{ dataset.linkPaper }}">Link to Paper</a><br>
            {% endif %}
            {% if dataset.modelsUsed != "" and dataset.modelsUsed != null and dataset.modelsUsed != "nan" %}
                <strong>Models Used:</strong> {{ dataset.modelsUsed }}<br>
            {% endif %}
            {% if dataset.inputModel != "" and dataset.inputModel != null and dataset.inputModel != "nan" %}
                <strong>Input Model:</strong> {{ dataset.inputModel }}<br>
            {% endif %}
            {% if dataset.dataResolution != "" and dataset.dataResolution != null and dataset.dataResolution != "nan" %}
                <strong>Data Resolution:</strong> {{ dataset.dataResolution }}<br>
            {% endif %}
            {% if dataset.outputModel != "" and dataset.outputModel != null and dataset.outputModel != "nan" %}
                <strong>Output Model:</strong> {{ dataset.outputModel }}<br>
            {% endif %}
            {% if dataset.paperInfo != "" and dataset.paperInfo != null and dataset.paperInfo != "nan" %}
                <strong>Other Information About the Paper:</strong> {{ dataset.paperInfo }}<br>
            {% endif %}
            <strong>Other Information About the Dataset:</strong> {{ dataset.otherInfo }}<br>
        `;

        // Bind the popup to the marker
        marker.bindPopup(popupContent);
    {% endfor %}
</script>

<!-- For custon marker -->
<!-- <script>
    // Initialize map
    const map = L.map('map').setView([0, 0], 5); // Center of the globe, zoom level 5
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    // Define a custom icon
    // const customIcon = L.icon({
    //     iconUrl: 'path/to/your/icon.png', // Replace with your custom icon URL
    //     iconSize: [32, 32], // Size of the icon
    //     iconAnchor: [16, 32], // Point of the icon which will correspond to the marker's location
    //     popupAnchor: [0, -32], // Point from which the popup will open relative to the icon
    // });

    {% for dataset in site.data.dataset %}
        // Log coordinates to check if data is parsed
        console.log("Dataset coordinates:", {{ dataset.coordX }}, {{ dataset.coordY }});

        const lat = {{ dataset.coordY }};
        const lon = {{ dataset.coordX }};
        
        // Create marker with custom icon
        // const marker = L.marker([lat, lon], { icon: customIcon }).addTo(map);
        
        // Build popup content dynamically
        let popupContent = `
            <strong>Title:</strong> {{ dataset.title }}<br>
            <strong>Description:</strong> {{ dataset.description }}<br>
            <strong>Country:</strong> {{ dataset.country }}<br>
            {% if dataset.linkDownload != "Upon Request" and dataset.linkDownload != "" %}
                <a href="{{ dataset.linkDownload }}">Link to Download</a><br>
            {% elsif dataset.linkDownload == "Upon Request" %}
                <a>Upon Request to Author</a><br>
            {% endif %}
            <strong>Number of Landslide Records:</strong> {{ dataset.numLandslideRecords }}<br>
            <strong>Dataset Details:</strong> {{ dataset.datasetDetails }}<br>
            <strong>Landslide Inventory Type:</strong> {{ dataset.inventoryType }}<br>
            {% if dataset.linkPaper != "" and dataset.linkPaper != null and dataset.linkPaper != "nan" %}
                <a href="{{ dataset.linkPaper }}">Link to Paper</a><br>
            {% endif %}
            {% if dataset.modelsUsed != "" and dataset.modelsUsed != null and dataset.modelsUsed != "nan" %}
                <strong>Models Used:</strong> {{ dataset.modelsUsed }}<br>
            {% endif %}
            {% if dataset.inputModel != "" and dataset.inputModel != null and dataset.inputModel != "nan" %}
                <strong>Input Model:</strong> {{ dataset.inputModel }}<br>
            {% endif %}
            {% if dataset.dataResolution != "" and dataset.dataResolution != null and dataset.dataResolution != "nan" %}
                <strong>Data Resolution:</strong> {{ dataset.dataResolution }}<br>
            {% endif %}
            {% if dataset.outputModel != "" and dataset.outputModel != null and dataset.outputModel != "nan" %}
                <strong>Output Model:</strong> {{ dataset.outputModel }}<br>
            {% endif %}
            {% if dataset.paperInfo != "" and dataset.paperInfo != null and dataset.paperInfo != "nan" %}
                <strong>Other Information About the Paper:</strong> {{ dataset.paperInfo }}<br>
            {% endif %}
            <strong>Other Information About the Dataset:</strong> {{ dataset.otherInfo }}<br>
        `;

        // Bind the popup to the marker
        marker.bindPopup(popupContent);
    {% endfor %}
</script> -->
