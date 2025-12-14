#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/12 9:54
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: DesignPattern
# @FileName   : DesignPattern/去除空格.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


text = """
Content-based filtering (CBF) also known as ―cognitive 
filtering‖, recommend the items based on the user’s item 
profile and user profile. This type of profiles is created at the 
beginning, when the user creates the account and starts using 
the system. As a user more interaction with the system , more 
strong user profile is created. Here, only user’s information is 
enough rather than other similar users, so very small scope of 
information are needed for recommendation.   
The idea behind CBF system is that ―if user like the item in 
the past, then user probably like similar type of item in 
future‖, so CBF compare the user’s item profile with current 
item’s profile and try to recommend the similar type of items 
that user may like. The profile of user is made of the different 
keywords, so simple way the CBF system match the keywords 
of highly rated item profile .To built the user profile, user’s 
item preferences and user information are needed, which can 
be gather explicitly or implicitly. In the movie-lens dataset, 
user’s profile is described by demographic information like 
gender, occupation, age, zip code etc. Explicit information can 
be gathered by personal input by clicking the checkbox, 
giving the start rating, thumbs up and down etc. But some 
time user may not give this type of information directly so 
need of the implicit data collection is needed. Thus system 
uses the implicit feedback to gather the information of user.  
Content-based systems are designed mostly to recommend 
text-based items, so keywords are use as content here. For 
example, Fab system [8] which recommends Web pages to 
users, represents Web page content with the 100 most 
important words. Syskill & Webert system [2] represents 
documents with the 128 most informative words. Different 
algorithms are available for content based filtering. The most 
commonly used techniques are TF-IDF, naïve bayes classifier 
etc. 
"""

text = text.replace('\n', '').replace('\t', '').replace('\r', '')

print(text)

# --END--
