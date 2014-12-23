---
title: A Data-Driven Analysis of Patent Trolls
---

<link href='https://netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.css' rel='stylesheet' type='text/css'>
<link href='https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css' rel='stylesheet' type='text/css'>
<link href='css/metricsgraphics.css' rel='stylesheet' type='text/css'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.min.js' charset='utf-8'></script>
<script src='js/metricsgraphics.min.js'></script>
<script src='js/main.js'></script>

Overview
-------
Lorem ipsum dolor sit amet.


Twitter mentions of patent troll, pae, etc. 
===========================================
From the figure we see gradual inreases in the mentions of terms relating to patent trolls or patent assertion entities over time, which may correspond to the increasing popularity and user base of Twitter. However, we see significant spikes in mentions for the term "pae", or patent assertion entity, which occurs around the end of the first quarter of 2013. The trend dies down to a regular level by the end of the year but spikes again to the highest point in mid 2014. This correlates almost exactly with the Alice Corp vs CLS Bank Supreme Court case which many of the major technology companies were eager and actively urging to have heard by the Supreme Court. The case was argued in March of 2014 and decided in June. 
The Alice Corp case was highly anticipated by major players in the technology and software industry, as well as lawyers involved in patent litigation, and preliminary studies have shown a decrease in patent lawsuits since the ruling. It may be too early to tell if this case was the main cause of the decline but the ruling was significant enough to believe that it may be shifting the tactics of many "patent trolls" as more dubious software patents are likely to be covering unpatentable ideas and processes. This, along with increased publicity as shown by the Twitter mention proxy we present in the figures, will change the rate at which companies settle lawsuits or choose to fight them in court. 

<div class='container' style='width: 1200px'>
    <div id='mentions1-2010'></div>
    <div id='mentions1-2010_legend'></div>
    <div id='mentions1-2011'></div>
    <div id='mentions1-2011_legend'></div>
    <div id='mentions1-2012'></div>
    <div id='mentions1-2012_legend'></div>
    <div id='mentions1-2013'></div>
    <div id='mentions1-2013_legend'></div>
    <div id='mentions1-2014'></div>
    <div id='mentions1-2014_legend'></div>
</div>

Court jurisdiction and patent lawsuits
======================================
From the analysis of patent lawsuits from 2010 to 2012 we discovered that there are about 10 primary entities that bring the majority of lawsuits, and these are heard, for the most part, in three court districts. Texas is the leading district in both years, with Delaware and California close behind. These three combine for 50% of all lawsuits in 2010 and then increased to 71% in 2012. The top 10 districts all saw increase in the overall number of lawsuits from 1483 in 2010, to 3787 in 2012. This is a dramatic increase in number that some researchers have argued is the result of new legislation that prohibits multiple defendents per lawsuit, meaning an individual suit must be filed for each person or entity implicated in the lawsuit.
Patent holding companies increased the most lawsuits of all eight categories described by the authors of the study, from 290 in 2010 to an astonishing 1728 in 2012. This category contains many of the entities described as "patent trolls" and the data show why their notoriety is on the rise. 

<div class='container' style='width: 1200px'>
    <div id='mentions-by-state'></div>
</div>

<div class='container' style='width: 1200px'>
    <div id='sentiment-2010'></div>
    <div id='sentiment-2010_legend'></div>
    <div id='sentiment-2011'></div>
    <div id='sentiment-2011_legend'></div>
    <div id='sentiment-2012'></div>
    <div id='sentiment-2012_legend'></div>
    <div id='sentiment-2013'></div>
    <div id='sentiment-2013_legend'></div>
    <div id='sentiment-2014'></div>
    <div id='sentiment-2014_legend'></div>
</div>

<!-- <div class='container' style='width: 1200px'>
    <div id='mentions2-2010'></div>
    <div id='mentions2-2010_legend'></div>
    <div id='mentions2-2011'></div>
    <div id='mentions2-2011_legend'></div>
    <div id='mentions2-2012'></div>
    <div id='mentions2-2012_legend'></div>
    <div id='mentions2-2013'></div>
    <div id='mentions2-2013_legend'></div>
    <div id='mentions2-2014'></div>
    <div id='mentions2-2014_legend'></div>
</div> -->
