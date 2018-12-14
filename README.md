# A Flask Web for Recommendation System

> It's just a homework for [UCAS-091M5042H -网络数据挖掘](http://jwxk.ucas.ac.cn/course/courseplan/148444).
>
> Because the dataset is too small(the User-Iterm matrix only 0 or 1) , this rec system only run  offline.

![](https://ws2.sinaimg.cn/large/006tNbRwly1fy68gktj58j31ee0o2wgo.jpg)

- [~~在线Demo~~]()   For more details , you can visist my blog ：[记又一次推荐系统](ttps://blog.idejie.com/2018/12/14/a-rec-sys/)。

###  Introduction

- DashBoard

  - Extracted the topic and tags of all news and Data reformated as `json`

  ```json
  {
  	'100648598': { 
  		'title': '消失前的马航370',
  		'content': '【财新网】（实习记者葛菁）据新华社消息........',
  		'news_time': '2014年03月08日12:31',
  		'topic': '时政',
  		'tags': [
              ('马航', 3.9849225009666664),
              ('370', 3.9849225009666664), 
              ('消失', 2.074425740486667)
          ]
  	}
  }
  ```

  - The list of news on web

  ![](https://ws4.sinaimg.cn/large/006tNbRwly1fy68hqrn5oj31c00u04c3.jpg)

- User interface

  - Analysis the topics and the tags-cloud of users

  ![](https://ws4.sinaimg.cn/large/006tNbRwly1fy68om8ixzj31xb0u079c.jpg)

  - Recommand news for users

  ![](https://ws1.sinaimg.cn/large/006tNbRwly1fy68pk87ygj32ko0sswoa.jpg)

  - Recommand similar users and provide the history of user

  ![](https://ws2.sinaimg.cn/large/006tNbRwly1fy68rhg9mrj31hx0u07hd.jpg)

- News interface

  - Classified by topic

  ![](https://ws2.sinaimg.cn/large/006tNbRwly1fy68zu51r7j31hh0u0qgg.jpg)

  - Provide the content /topic and details of news

  ![](https://ws3.sinaimg.cn/large/006tNbRwly1fy68u0xcncj32be0u0k9d.jpg)

  - Provide the similar news and  Potential users

    ![](https://ws1.sinaimg.cn/large/006tNbRwly1fy69uhes4qj31v90u049b.jpg)



    ![](https://ws2.sinaimg.cn/large/006tNbRwly1fy6a6l3oshj31id0u0wun.jpg)

 ## Environment 
 - Python3 
 - Some python packages , you can install them by `pip install requirements`
 - The data for project provided in another repo: [text-classification](https://github.com/idejie/text-classification)

## Usage

- You can import this project using `PyCharm`

- or in terminal `python3 app.py `

 ## Reference
 - [gaussic/text-classification-cnn-rnn](https://github.com/gaussic/text-classification-cnn-rnn)
 - [jieba](https://github.com/fxsjy/jieba)
 - [NicolasHug/Surprise](https://github.com/NicolasHug/Surprise)
 - ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization
Deqing Li, Honghui Mei, Yi Shen, Shuang Su, Wenli Zhang, Junting Wang, Ming Zu, Wei Chen.
Visual Informatics, 2018 [[PDF]](http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/echarts.pdf)
