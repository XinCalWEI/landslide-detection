---
layout: default
title: News
---

<main>
    <div class="news-item">
        <h2>NASA Applied Remote Sensing (ARSET)</h2>
        <span class="date">March 11, 13, 18, 2025</span>
        <a href="https://appliedsciences.nasa.gov/get-involved/training/english/arset-landslide-monitoring-and-risk-assessment-using-nasa-earth">Learn More</a>
        <span class="tag conference">Conference</span>
        <p>A three-part introductory training that covers a number of topics related to landslides, demonstrating a wide variety of NASA Earth science data uses to characterize landslides and their impacts.</p>
        <p>Part 1: Remote Sensing for Landslide Science and Disaster Planning</p>
        <p>Part 2: Mapping Landslide Occurrence Using Earth Observations</p>
        <p>Part 3: Remote Sensing and Landslide Susceptibility</p>
        <div class="news-images">
            <img src="./img/news/NASA_Arset.png" alt="NASA ARSET">
        </div>
    </div>
    <div class="news-item">
        <h2>Jowaria Khan's Presents on Geospatial Foundation Models</h2>
        <span class="date">February 14, 2025</span>
        <a href="https://scholar.google.com/citations?user=q6_Cq_cAAAAJ&hl=en">Learn More</a>
        <span class="tag presentation">Presentation</span>
        <div class="news-images">
            <img src="./img/news/2-14-25-img1.jpg" alt="2-12-25">
            <img src="./img/news/2-14-25-img2.jpg" alt="2-12-25">
        </div>
    </div>
</main>

<style>
    main {
        margin: 0 auto;
        padding: 20px;
    }
    .news-item {
        max-width: 100%;
        border-bottom: 1px solid #4C4332;
        padding: 1rem;
    }
    .news-images{
        margin-top: 5px;
    }
    .news-images img {
        height: 300px; 
        width: auto;
        object-fit: cover;
        margin-right: 10px;
        margin-bottom: 10px;
        border-radius: 8px;
        display: inline-block;
        vertical-align: top;
    }
    .news-item h2 {
        margin: 0;
        font-size: 1.8em;
        color: #333;
    }
    .news-item .date {
        font-size: 0.9em;
        color: gray;
    }
    .news-item p {
        font-size: 1em;
        line-height: 1.6;
        margin-top: 10px;
    }
    .news-item a {
        color: #0078A8;
        text-decoration: none;
    }
    .news-item a:hover {
        text-decoration: underline;
    }
    .tag {
        display: inline-block;
        margin-top: 5px;
        padding: 5px 10px;
        margin-left: 10px;
        font-size: 0.9em;
        border-radius: 5px;
        color: white;
    }
    .tag.conference, .tag.presentation {
        background-color:rgb(92, 196, 237);
    }
    .tag.research, .tag.paper, .tag.project {
        background-color:rgb(242, 69, 78);
    }
    .tag.people {
        background-color:rgb(227, 146, 39);
    }
    .tag.article, .tag.blog {
        background-color: #7DBA87;
    }
</style>