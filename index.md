---
title: Patent Trolls in the Tweetosphere
---

<link href='css/metricsgraphics.css' rel='stylesheet' type='text/css'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.min.js' charset='utf-8'></script>
<script src='js/metricsgraphics.min.js'></script>
<script src='js/main.js'></script>


<xmp theme="journal" style="display:none;">

Patent Trolls in the Tweetosphere
=================================

<br>
<br>

Twitter Keyword Mentions 
------------------------
The figures below show a year-by-year breakdown of twitter mentions of particular keywords, as articulated by each graphic's respective legend. The sample size of each graphic is the entirety of the Twitter corpus for each graphic's respective year.


From the figure we see gradual inreases in the mentions of terms relating to patent trolls or patent assertion entities over time, which may correspond to the increasing popularity and user base of Twitter. However, we see significant spikes in mentions for the term "pae", or patent assertion entity, which occurs around the end of the first quarter of 2013. The trend dies down to a regular level by the end of the year but spikes again to the highest point in mid 2014. This correlates almost exactly with the Alice Corp vs CLS Bank Supreme Court case which many of the major technology companies were eager and actively urging to have heard by the Supreme Court. The case was argued in March of 2014 and decided in June. 


The Alice Corp case was highly anticipated by major players in the technology and software industry, as well as lawyers involved in patent litigation, and preliminary studies have shown a decrease in patent lawsuits since the ruling. It may be too early to tell if this case was the main cause of the decline but the ruling was significant enough to believe that it may be shifting the tactics of many "patent trolls" as more dubious software patents are likely to be covering unpatentable ideas and processes. This, along with increased publicity as shown by the Twitter mention proxy we present in the figures, will change the rate at which companies settle lawsuits or choose to fight them in court. 


We've also included important dates in the patent troll world over the last 5 years. Each landmark is denoted by a vertical line in the graph with a number associated with that line. The numbers correspond to the table at the end of this section.


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

<br>
---
<br>

Court Jurisdiction and Patent Lawsuits
--------------------------------------
From the analysis of patent lawsuits from 2010 to 2012 we discovered that there are about 10 primary entities that bring the majority of lawsuits, and these are heard, for the most part, in three court districts. Texas is the leading district in both years, with Delaware and California close behind. These three combine for 50% of all lawsuits in 2010 and then increased to 71% in 2012. The top 10 districts all saw increase in the overall number of lawsuits from 1483 in 2010, to 3787 in 2012. This is a dramatic increase in number that some researchers have argued is the result of new legislation that prohibits multiple defendents per lawsuit, meaning an individual suit must be filed for each person or entity implicated in the lawsuit.


Patent holding companies increased the most lawsuits of all eight categories described by the authors of the study, from 290 in 2010 to an astonishing 1728 in 2012. This category contains many of the entities described as "patent trolls" and the data show why their notoriety is on the rise. 


The data used for this section was gathered and made public as part of an academic study of non-practicing entities conducted by Christopher A. Cotropia, Jay P. Kesan, and David L. Schwartz. The website for their project can be found [here](http://npedata.com/), and the .csv files of their findings which we used can be found [here]()


<br>
2010
----
| Patentee Category                          |E.D. Tex.  |D. Del.    |C.D. Cal.  |N.D. Cal.  |N.D. Ill.  |D.N.J.     |S.D.N.Y.   |D. Mass.   |M.D. Fla.  |D. Minn.   |Grand Total   |
| ------------------------------------------ | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ------------ |
|6. Operating company                        |94         |190        |130        |103        |111        |125        |71         |55         |44         |52         |975           |
|5. Patent holding company                   |120        |40         |30         |23         |35         |9          |14         |3          |15         |1          |290           |
|2. Individual/family trust                  |21         |2          |21         |10         |4          |4          |5          |7          |4          |3          |81            |
|3. Large aggregator                         |20         |7          |1          |5          |3          |1          |2          |           |           |           |39            |
|4. Failed operating company/failed start-up |13         |2          |1          |9          |7          |           |1          |           |           |           |33            |
|8. Technology development company           |5          |5          |3          |10         |2          |1          |2          |1          |           |           |29            |
|7. IP Holding company of operating company  |4          |3          |3          |7          |           |1          |           |           |           |4          |22            |
|1. University/College                       |4          |2          |1          |2          |1          |1          |           |2          |           |           |13            |
|**Grand Total**                             |282        |251        |190        |169        |163        |142        |95         |68         |63         |60         |1483          |


| Patentee Category                          |E.D. Tex.  |D. Del.    |C.D. Cal.  |N.D. Cal.  |N.D. Ill.  |D.N.J.     |S.D.N.Y.   |D. Mass.   |M.D. Fla.  |D. Minn.   |
| ------------------------------------------ | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
|6. Operating company                        |10%        |19%        |13%        |11%        |11%        |13%        |7%         |6%         |5%         |5%         |
|5. Patent holding company                   |41%        |14%        |10%        |8%         |12%        |3%         |5%         |1%         |5%         |0%         |
|2. Individual/family trust                  |26%        |2%         |26%        |12%        |5%         |5%         |6%         |9%         |5%         |4%         |
|3. Large aggregator                         |51%        |18%        |3%         |13%        |8%         |3%         |5%         |0%         |0%         |0%         |
|4. Failed operating company/failed start-up |39%        |6%         |3%         |27%        |21%        |0%         |3%         |0%         |0%         |0%         |
|8. Technology development company           |17%        |17%        |10%        |34%        |7%         |3%         |7%         |3%         |0%         |0%         |
|7. IP Holding company of operating company  |18%        |14%        |14%        |32%        |0%         |5%         |0%         |0%         |0%         |18%        |
|1. University/College                       |31%        |15%        |8%         |15%        |8%         |8%         |0%         |15%        |0%         |0%         |
|**Grand Total**                             |19%        |17%        |13%        |11%        |11%        |10%        |6%         |5%         |4%         |4%         |


<br>
2012
----
| Patentee Category                          |E.D. Tex.  |D. Del.    |C.D. Cal.  |N.D. Cal.  |N.D. Ill.  |D.N.J.     |S.D. Cal.  |S.D. Fla.  |S.D.N.Y.   |E.D. Va.   |Grand Total |
| ------------------------------------------ | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------- |
|5. Patent holding company                   |719        |520        |168        |86         |65         |26         |5          |93         |11         |35         |1728        |
|6. Operating company                        |212        |305        |200        |112        |89         |107        |104        |29         |99         |36         |1293        |
|2. Individual/family trust                  |122        |35         |35         |19         |19         |4          |8          |1          |8          |7          |258         |
|3. Large aggregator                         |50         |46         |52         |20         |43         |4          |13         |5          |11         |           |244         |
|4. Failed operating company/failed start-up |121        |23         |2          |9          |           |           |1          |           |1          |1          |158         |
|8. Technology development company           |5          |44         |1          |10         |           |           |1          |           |           |6          |67          |
|1. University/College                       |5          |1          |           |2          |6          |4          |1          |3          |           |           |22          |
|7. IP Holding company of operating company  |1          |10         |4          |           |           |           |2          |           |           |           |17          |
|**Grand Total**                             |1235       |984        |462        |258        |222        |145        |135        |131        |130        |85         |3787        |


| Patentee Category                          |E.D. Tex.  |D. Del.    |C.D. Cal.  |N.D. Cal.  |N.D. Ill.  |D.N.J.     |S.D. Cal.  |S.D. Fla.  |S.D.N.Y.   |E.D. Va.   |
| ------------------------------------------ | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
|5. Patent holding company                   |42%        |30%        |10%        |5%         |4%         |2%         |0%         |5%         |1%         |2%         |
|6. Operating company                        |16%        |24%        |15%        |9%         |7%         |8%         |8%         |2%         |8%         |3%         |
|2. Individual/family trust                  |47%        |14%        |14%        |7%         |7%         |2%         |3%         |0%         |3%         |3%         |
|3. Large aggregator                         |20%        |19%        |21%        |8%         |18%        |2%         |5%         |2%         |5%         |0%         |
|4. Failed operating company/failed start-up |77%        |15%        |1%         |6%         |0%         |0%         |1%         |0%         |1%         |1%         |
|8. Technology development company           |7%         |66%        |1%         |15%        |0%         |0%         |1%         |0%         |0%         |9%         |
|1. University/College                       |23%        |5%         |0%         |9%         |27%        |18%        |5%         |14%        |0%         |0%         |
|7. IP Holding company of operating company  |6%         |59%        |24%        |0%         |0%         |0%         |12%        |0%         |0%         |0%         |
|**Grand Total**                             |33%        |26%        |12%        |7%         |6%         |4%         |4%         |3%         |3%         |2%         |

<br>
---
<br>

Twitter Keyword Mentions by State (2010 - 2014)
-----------------------------------------------
This is a breakdown of total keyword mentions ("patent troll" OR "#patenttroll" OR "patent monitization entity", all case-insensitive) over the last 5 years. Again, this data is from the Twitter Firehose API, so it is representative of ALL tweets between 2010 and the present (12/21/14).


<div class='container' style='width: 1200px'>
    <div id='mentions-by-state'></div>
</div>

<br>
<br>

Twitter Keyword Sentiment by Year (2010 - 2014)
-----------------------------------------------
The following graphics show a year-by-year breakdown of sentiment for each of 4 keyword sets, as articulated by the graphics' respective legends. Topsy (the API we used to gather the data) calculates sentiment as a normalized score on the interval [0,100], with 0 being least favorable and 100 being most favorable. The score is calculated based on incidences of connotation-bearing words within the tweets ("awesome" = favorable, "annoying" = unfavorable, etc.). The same set of landmark events in the patent troll timeline which were used in the "mentions" section have been added to this set of graphics as well for reference and orientation.


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

<br>
---
<br>

Methodology
-----------
**Tools**
- [metricsgraphicsjs](http://metricsgraphicsjs.org/)
- [strapdownjs](http://strapdownjs.com/)
- [Topsy API](http://api.topsy.com/doc/resources/)
- [python](https://www.python.org/) programming language
- [requests](http://docs.python-requests.org/en/latest/) package for python
- [pytopsy](https://github.com/WillChilds-Klein/cpsc183-final/tree/master/pytopsy), a custom python package for accessing Topsy's REST API written by [Will Childs-Klein](http://will.childs-kle.in)


All code and data can be found on the project's GitHub [repository](https://github.com/WillChilds-Klein/cpsc183-final).

</xmp>

<script src="http://strapdownjs.com/v/0.2/strapdown.js"></script>
