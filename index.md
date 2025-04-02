---
layout: default
title: About
---

<head>
</head>

<main>
    <div class="image-container">
        <img src="./img/ai4.png" alt="bg">
        <div class="overlay"></div>
        <a href="/form" class="upload-btn">
            <button>Upload a Dataset</button>
        </a>
        <h2>AI Generated Image</h2>
    </div>
    <div class="text">
        <h1>TBA</h1>
    </div>
</main>

<style>
    .image-container {
        position: relative;
        display: inline-block;
        width: 100vw;
        height: 35vw;
    }

    .image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
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
        background-color: #60816B;
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

    .text{
        padding-left: 30px;
    }

    .container{
        display: flex;
    }
</style>