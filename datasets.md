---
layout: default
title: Datasets
---

<main>
    <img src="img/Blank_Map.jpg" alt="BlankMap">
    <!-- <img scr="img/Blank_Map.jpg" alt="BlankMap" usemap="#workmap"/> -->
    <br> TODO: Need to add css
    <map name="workmap">
        <area shape="circle" coords="34,44,270,350" alt="" href="">
        <area shape="circle" coords="290,172,333,250" alt="" href="">
        <area shape="circle" coords="337,300,44" alt="" href="">
    </map>
    <br> Datasets:
    {% for dataset in site.data.dataset %}
    <details>
        <summary>{{ dataset.title }}</summary>
        <p> {{ dataset.description }} </p>
        {% if dataset.linkDownload != "Upon Request" %}
            <a href="{{ dataset.linkDownload }}">Link to Download</a>
        {% else %}
            <a>Upon Request to Author</a>
        {% endif %}
        {% if dataset.linkPaper %}
            <a href="{{ dataset.linkPaper }}"> Link to a Paper Using Dataset</a>
        {% endif %}
        <ul>
            {% for other in dataset.other %}
            <li>{{ other }}</li>
            {% endfor %}
        </ul>
    </details>
    {% endfor %}


   
</main>