import time


def get_news():
    with open("classification/data/rec_news/news_topic.json", 'r') as f:
        news_topic = eval(f.readlines()[0])
    return news_topic


def get_topic_news():
    with open("classification/data/rec_news/news_topic.json", 'r') as f:
        news_topic = eval(f.readlines()[0])
    topics_news = {}
    for k, v in news_topic.items():
        news = {
            'id': k,
            'news': v
        }
        if v['topic'] in topics_news:

            topics_news[v['topic']].append(news)
        else:
            topics_news[v['topic']] = [news]
    return topics_news


def get_records():
    records = []
    news_all=get_news()
    format = '%Y-%m-%d %H:%M:%S'
    with open('classification/data/rec_news/user_click_data.txt', 'r') as f:
        for line in f.readlines():
            data = line.split('\t')[:3]
            u_id = data[0]
            news_id = data[1]
            value = time.localtime(int(data[2]))
            click_time = time.strftime(format, value)
            item = {
                'u_id': u_id,
                'news_id': news_id,
                'click_time': click_time,
                'title':news_all[news_id]['title'],
                'topic':news_all[news_id]['topic'],
                'news_time': news_all[news_id]['news_time']
            }
            records.append(item)
    return records


def get_user_records():
    records = {}
    format = '%Y-%m-%d %H:%M:%S'
    news_all = get_news()
    with open('classification/data/rec_news/user_click_data.txt', 'r') as f:
        for line in f.readlines():
            data = line.split('\t')[:3]
            u_id = data[0]
            news_id = data[1]
            value = time.localtime(int(data[2]))
            click_time = time.strftime(format, value)
            item = {
                'u_id': u_id,
                'news_id': news_id,
                'click_time': click_time,
                'title': news_all[news_id]['title'],
                'topic': news_all[news_id]['topic'],
                'news_time': news_all[news_id]['news_time']
            }
            if u_id in records:
                records[u_id].append(item)
            else:
                records[u_id] = [item]
    return records


def get_news_records():
    records = {}
    format = '%Y-%m-%d %H:%M:%S'
    news_all = get_news()
    with open('classification/data/rec_news/user_click_data.txt', 'r') as f:
        for line in f.readlines():
            data = line.split('\t')[:3]
            u_id = data[0]
            news_id = data[1]
            value = time.localtime(int(data[2]))
            click_time = time.strftime(format, value)
            item = {
                'u_id': u_id,
                'news_id': news_id,
                'click_time': click_time,
                'title': news_all[news_id]['title'],
                'topic': news_all[news_id]['topic'],
                'news_time': news_all[news_id]['news_time']
            }
            if news_id in records:
                records[news_id].append(item)
            else:
                records[news_id] = [item]
    return records

def get_news_topic_tag(news_id):
    with open("classification/data/rec_news/news_topic.json", 'r') as f:
        news_topic = eval(f.readlines()[0])
    return news_topic[news_id]['topic'],news_topic[news_id]['tags']

