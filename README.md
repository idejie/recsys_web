# A Flask Web for Recommendation System

> It's just a homework .

> Because the dataset is too small(the User-Iterm matrix only 0 or 1) , this rec system only  offline.
### Feature

- Contented Based
  -  Using CNN to extract the topic of news
  -  Using HanNLP to extract the tags(some entries) of news
  -  According the similarity of users' topics and tags

- SVD Based
  -  Transfering the dataset to User-Item matrix
  -  Using SVD++(Because the interest of user will  decrease in terms of time) to split User_Matrix and News_Matrix
  -  Using KNN to get the similar user or news

- NMF Based
  -  Likely SVD
  
 ### Result
 -  Contented Based
 
 > The test  result for CNN_Topic_Extraction
 ```
 Test Loss:   0.11, Test Acc:  96.85%
Precision, Recall and F1-Score...
              precision    recall  f1-score   support

          体育       0.99      0.99      0.99      1000
          财经       0.95      0.99      0.97      1000
          房产       1.00      1.00      1.00      1000
          家居       0.98      0.91      0.94      1000
          教育       0.95      0.93      0.94      1000
          科技       0.94      0.98      0.96      1000
          时尚       0.98      0.98      0.98      1000
          时政       0.94      0.95      0.94      1000
          游戏       0.98      0.98      0.98      1000
          娱乐       0.98      0.97      0.98      1000

   micro avg       0.97      0.97      0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000
 ```
 
 ## Environment 
 - Python3 
 - `requirements.txt`
 - (For China)To download the dataset you maybe need the internet access to Google Drive
 
 ## Reference
 - [gaussic/text-classification-cnn-rnn](https://github.com/gaussic/text-classification-cnn-rnn)
 - [hankcs/pyhanlp](https://github.com/hankcs/pyhanlp)
 - [NicolasHug/Surprise](https://github.com/NicolasHug/Surprise)
 - ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization
Deqing Li, Honghui Mei, Yi Shen, Shuang Su, Wenli Zhang, Junting Wang, Ming Zu, Wei Chen.
Visual Informatics, 2018 [[PDF]](http://www.cad.zju.edu.cn/home/vagblog/VAG_Work/echarts.pdf)
