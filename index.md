---
layout: default
title: About
---

<head>
</head>

<main>
    <div class="image-container">
        <img src="./img/ai/ai5.png" alt="bg">
        <div class="overlay"></div>
        <a href="{{ '/form' | absolute_url }}" class="upload-btn">
            <button>Upload Your Own Data</button>
        </a>
        <!-- <h2>AI Generated Image</h2> -->
    </div>
    <div class="about-container">
        <div class="title-container">
            <h1>
                <span class="highlight">GOBLUE:</span><br />
                <span class="subtitle">A Global Online Base for Landslide Understanding and Exchange</span>
            </h1>
        </div>
        <div class="carousel-container">
            <div class="carousel">
                <div class="carousel-section">
                    <h2>Background</h2>
                    <p>
                    Landslides pose a significant and growing threat to mountainous regions worldwide, exacerbated by urbanization, climate change, and population growth. Globally, landslides caused immense human suffering between 1998-2017, affecting an estimated 4.8 million people and causing over 18,000 deaths, according to the World Health Organization, with climate change projected to increase their frequency. While machine learning (ML) and deep learning (DL) have spurred the development of landslide detection models, progress faces significant challenges. Many existing models are region- and type-specific, demonstrating poor or unverified cross-regional generalization. Furthermore, their development often relies on extensive ground truth landslide inventories, which require substantial resources to create, limiting model training in data-scarce regions. The lack of comprehensive, globally representative, and easily accessible datasets currently hinders the creation of robust, generalizable models, including potentially powerful foundation models.
                    </p>
                </div>
                <div class="carousel-section">
                    <h2>What We've Done So Far</h2>
                    <p>
                    Inspired by large-scale dataset efforts like ImageNet and the rapid advancements in large language models, and to address these critical gaps, we have developed an open-access, continuously updated website hosting a database that aggregates freely available landslide datasets. This repository provides detailed attributes for each dataset, including: the number of landslide records, inventory type (point/polygon), data resolution, spatial coverage (country/region), model input factors (e.g., satellite optical imagery, land use type, vegetation indices, elevation), ML/DL model used, data splitting methodology (e.g., train/validation/test ratios), and whether cross-regional validation was performed. Downloadable links are provided for direct data access. In addition, the website features an interface enabling the global research community to upload their own datasets, fostering a collaborative effort to build this comprehensive resource. Moreover, the website will be regularly updated with information regarding relevant conferences, seminars, and workshops focused on landslide research.
                    </p>
                </div>
                <div class="carousel-section">
                    <h2>What's Next</h2>
                    <p>
                    Our next step will leverage this aggregated data to develop a large-scale landslide detection model with better generalization ability. We plan to apply and adapt this model to specific regions of interest, such as Nepal, utilizing techniques like transfer learning combined with limited local data to predict both historical landslide occurrences and identify potentially unstable slopes prone to future failure.
                    </p>
                </div>
            </div>
            <!-- Arrows -->
            <button class="carousel-prev">←</button>
            <button class="carousel-next">→</button>
        </div>
    </div>
    <div class="title">
        <h1>Partners</h1>
    </div>
    <div class="image-slider-container">
        <div class="image-slider-track">
            <!-- Replace src values with paths to your images -->
            <a href="https://disasterdata.engin.umich.edu/">
                <img src="./img/partners/aidd-logo.png" alt="Logo 1" />
            </a>
            <a href="https://sites.google.com/view/realize-lab/home">
                <img src="./img/partners/realize-logo.png" alt="Logo 2" />
            </a>
            <a href="http://cse.engin.umich.edu/">
                <img src="./img/partners/cse.png" alt="Logo 3" />
            </a>
            <a href="https://cee.engin.umich.edu/">
                <img src="./img/partners/cee.png" alt="Logo 4" />
            </a>
            <a href="https://mae.cee.illinois.edu/index.html">
                <img src="./img/partners/MAECenter.png" alt="Logo 5" />
            </a>
            <!-- Copies -->
            <a href="https://disasterdata.engin.umich.edu/">
                <img src="./img/partners/aidd-logo.png" alt="Logo 1" />
            </a>
            <a href="https://sites.google.com/view/realize-lab/home">
                <img src="./img/partners/realize-logo.png" alt="Logo 2" />
            </a>
            <a href="http://cse.engin.umich.edu/">
                <img src="./img/partners/cse.png" alt="Logo 3" />
            </a>
            <a href="https://cee.engin.umich.edu/">
                <img src="./img/partners/cee.png" alt="Logo 4" />
            </a>
            <a href="https://mae.cee.illinois.edu/index.html">
                <img src="./img/partners/MAECenter.png" alt="Logo 5" />
            </a>
        </div>
    </div>
</main>

<style>
    .image-container {
        position: relative;
        display: inline-block;
        width: 100vw;
        height: auto;
    }

    .image-container img {
        width: 100%;
        height: auto;
        object-fit: contain;
        display: block;
    }

    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5); /* Dark overlay */
    }

    .upload-btn {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: inline-block;
        text-decoration: none; 
    }

    .upload-btn button {
        padding: 12px 24px;
        background-color: #7DBA87;
        border: none;
        color: white;
        font-size: 3rem;
        border-radius: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .upload-btn button:hover {
        background-color: #468EA6;
    }

    .image-container h2 {
        position: absolute;
        bottom: 10px;
        left: 10px;
        transform: none;
        color: white;
        font-size: 0.5rem;
        text-align: left;
        z-index: 2;
    }

    /* Image Container Styling */
    .image-container {
        position: relative;
        display: inline-block;
        width: 100vw;
        height: auto;
    }

    .image-container img {
        width: 100%;
        height: auto;
        object-fit: contain;
        display: block;
    }

    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        /* Dark overlay */
        /* background: rgba(0, 0, 0, 0.5);  */
        background: rgba(0, 0, 0, 0);
    }

    .upload-btn {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: inline-block;
        text-decoration: none; 
    }

    .upload-btn button {
        padding: 12px 24px;
        background-color: #7DBA87;
        border: none;
        color: white;
        font-size: 3rem;
        border-radius: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .upload-btn button:hover {
        background-color: #468EA6;
    }

    .image-container h2 {
        position: absolute;
        bottom: 10px;
        left: 10px;
        transform: none;
        color: white;
        font-size: 0.5rem;
        text-align: left;
        z-index: 2;
    }

    /* Titles */
    .title {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        text-align: left;
        margin-top: 20px; 
        margin-left: 20px;
        margin-bottom: 20px;
    }

    .title h1 {
        font-size: 2rem;
        font-weight: bold;
        margin: 20px 0 0;
    }

    .title h1 span {
        margin: 0 20px; 
        font-size: 3rem; 
        color: #000; 
    }

    /* About Container */
    .about-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 40px;
        width: 100%;
        padding: 40px;
        box-sizing: border-box;
        background-color: transparent;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin: 30px 0;
        padding: 20px 20px;
    }

    .title-container {
        width: 30%;
        text-align: left;
        margin-left: 20px;
    }

    .title-container h1 {
        font-size: 2.5rem;
        color: #222;
        margin: 0;
        line-height: 1.2;
    }

    .title-container .highlight {
        font-weight: bold;
        color: #000;
    }

    .title-container .subtitle {
        color: #777;
        font-weight: normal;
    }

    .carousel-container {
        width: 70%;
        height: 50vh;
        /* overflow: hidden; */
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }
    .carousel {
        display: flex;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        width: 100%;
    }

    .carousel-section {
        flex: 0 0 100%;
        display: none;
        padding: 20px;
        box-sizing: border-box;
        scroll-snap-align: start;
    }

    .carousel-section.active {
        display: block;
    }

    .carousel-section h2 {
        font-size: 1.5rem;
        text-align: left;
        margin-bottom: 10px;
        margin-left: 2.5rem;
    }

    .carousel-section p {
        text-align: left;
        margin-right: 2rem;
        margin-left: 2.5rem;
        font-size: 1.2rem;
        color: #333;
    }

    /* Styling for navigation arrows */
    .carousel-prev, .carousel-next {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        font-size: 24px;
        padding: 10px;
        border: none;
        cursor: pointer;
        z-index: 10;
    }

    .carousel-prev {
        left: 10px;
    }

    .carousel-next {
        right: 10px;
    }

    .image-slider-container {
        overflow: hidden;
        width: 100%;
        height: 10vh;
        /* background-color: white; */
        margin: 0 20px;
        position: relative;
        display: flex;
        justify-content: center;
    }

    .image-slider-track {
        display: flex;
        padding-right: 10px;
        gap: 10px;
        /* width: max-content; */
        animation: slideLeft 20s linear infinite;
    }

    .image-slider-track img {
        height: 100%;
        width: auto;
        object-fit: cover;
        object-position: center;
        flex-shrink: 0;
        margin-right: 10px;
        border-radius: 8px;
    }

    @keyframes slideLeft {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(-50%);
        }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const carousel = document.querySelector('.carousel');
        const sections = document.querySelectorAll('.carousel-section');
        const prevBtn = document.querySelector('.carousel-prev');
        const nextBtn = document.querySelector('.carousel-next');

        let currentIndex = 0;

        // Function to show the current section
        function updateCarousel() {
            sections.forEach((section, index) => {
                section.classList.remove('active');  // Hide all sections
                if (index === currentIndex) {
                    section.classList.add('active');  // Show only the current section
                }
            });

            // Hide or show the previous and next buttons based on the index
            if (currentIndex === 0) {
                prevBtn.style.display = 'none'; // Hide the previous button if at the leftmost section
            } else {
                prevBtn.style.display = 'block'; // Show the previous button if not at the leftmost section
            }

            if (currentIndex === sections.length - 1) {
                nextBtn.style.display = 'none'; // Hide the next button if at the rightmost section
            } else {
                nextBtn.style.display = 'block'; // Show the next button if not at the rightmost section
            }
        }

        // Scroll to the next section
        function goToNextSection() {
            if (currentIndex < sections.length - 1) {
                currentIndex++;
                updateCarousel();
            }
        }

        // Scroll to the previous section
        function goToPreviousSection() {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        }

        // Initialize the first section as active
        updateCarousel();

        // Event listeners for buttons
        nextBtn.addEventListener('click', goToNextSection);
        prevBtn.addEventListener('click', goToPreviousSection);
    });

    // Image slider setup
    (function imageSliderInit() {
    const track = document.querySelector('.image-slider-track');
    const container = document.querySelector('.image-slider-container');

    // Duplicate images to ensure seamless loop if not already duplicated
    if (track.children.length <= 3) {
        [...track.children].forEach((img) => {
        track.appendChild(img.cloneNode(true));
        });
    }

    // Add an event listener to reset the animation to create a seamless loop
    track.addEventListener('animationiteration', () => {
        track.style.animation = 'none';
        track.offsetHeight; // Trigger reflow to reset animation
        track.style.animation = 'slideLeft 20s linear infinite';
    });
    })();
</script>
