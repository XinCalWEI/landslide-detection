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
        #global-dataset-list {
            background-color: #7DBA87;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            margin-bottom: 30px;
        }
        #global-dataset-list h2 {
            font-size: 2rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        details {
            background-color: #B0C8EC;
            border: 1px solid #ddd;
            margin-bottom: 15px;
            border-radius: 8px;
            padding: 15px;
            transition: background-color 0.3s ease;
        }
        details[open] {
            background-color: #e0f7fa;  /* Light cyan when dropdown is open */
        }
        details summary {
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
        }
        details p {
            margin: 10px 0;
            font-size: 1rem;
        }
        details a {
            color: #0078A8;
            text-decoration: none;
        }
        details a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<main>
    <!-- Create a container for the map -->
    <div id="map"></div>
    <!-- Section for listing global datasets -->
    <section>
        <div id="global-dataset-list">
            <h2>Global Datasets</h2>
            {% for dataset in site.data.dataset %}
                {% if dataset.country == "Global" %}
                    <details>
                        <summary><strong>{{ dataset.title }}</strong></summary>
                        <p><strong>Description:</strong> {{ dataset.description }}</p>
                        <p><strong>Number of Landslide Records:</strong> {{ dataset.numLandslideRecords }}</p>
                        <p><strong>Dataset Details:</strong> {{ dataset.datasetDetails }}</p>
                        <p><strong>Landslide Inventory Type:</strong> {{ dataset.inventoryType }}</p>
                        {% if dataset.linkDownload != "Upon Request" and dataset.linkDownload != "" %}
                            <p><a href="{{ dataset.linkDownload }}">Download Dataset</a></p>
                        {% elsif dataset.linkDownload == "Upon Request" %}
                            <p>Download Available Upon Request</p>
                        {% endif %}
                        {% if dataset.linkPaper != "" and dataset.linkPaper != null and dataset.linkPaper != "nan" %}
                            <p><a href="{{ dataset.linkPaper }}">Read Paper</a></p>
                        {% endif %}
                        {% if dataset.modelsUsed != "" and dataset.modelsUsed != null and dataset.modelsUsed != "nan" %}
                            <p><strong>Models Used:</strong> {{ dataset.modelsUsed }}</p>
                        {% endif %}
                        {% if dataset.inputModel != "" and dataset.inputModel != null and dataset.inputModel != "nan" %}
                            <p><strong>Input Model:</strong> {{ dataset.inputModel }}</p>
                        {% endif %}
                        {% if dataset.dataResolution != "" and dataset.dataResolution != null and dataset.dataResolution != "nan" %}
                            <p><strong>Data Resolution:</strong> {{ dataset.dataResolution }}</p>
                        {% endif %}
                        {% if dataset.outputModel != "" and dataset.outputModel != null and dataset.outputModel != "nan" %}
                            <p><strong>Output Model:</strong> {{ dataset.outputModel }}</p>
                        {% endif %}
                        {% if dataset.paperInfo != "" and dataset.paperInfo != null and dataset.paperInfo != "nan" %}
                            <p><strong>Other Paper Information:</strong> {{ dataset.paperInfo }}</p>
                        {% endif %}
                        <p><strong>Other Dataset Information:</strong> {{ dataset.otherInfo }}</p>
                    </details>
                {% endif %}
            {% endfor %}
        </div>
    </section>
</main>

<!-- Leaflet.js Map Setup -->
<script src="https://unpkg.com/leaflet@1.9.1/dist/leaflet.js"></script>
<script>
    // Initialize map
    const map = L.map('map').setView([0, 0], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    {% for dataset in site.data.dataset %}
        {% if dataset.country != "Global" %}
            // Assign lat and lon without redeclaring them
            var lat = parseFloat("{{ dataset.coordY }}");
            var lon = parseFloat("{{ dataset.coordX }}");
            var marker = L.marker([lat, lon]).addTo(map);
            var popupContent = `
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
            marker.bindPopup(popupContent);
        {% endif %}
    {% endfor %}
</script>
