#encoding=utf-8

import jieba.analyse





with open('classification/data/rec_news/news_topic.json','r') as f:
    news_topic = eval(f.read())

news_topic2 = {}
for news_id, news in news_topic.items():
    title = news['title']
    # content = news['content']
    tags = jieba.analyse.extract_tags(title, withWeight=True)
    # tags2 = jieba.analyse.extract_tags(content, withWeight=True)
    # print(tags1)
    news['tags']=tags
    news_topic2[news_id]=news
    # print(news_topic2)
    # break

with open('classification/data/rec_news/news.json','w') as f:
    f.write(str(news_topic2))