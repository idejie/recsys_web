with open('classification/data/rec_news/news.json', 'r') as f:
    news = eval(f.read())
with open('classification/data/rec_news/user_train.data', 'r') as f:
    users_train = eval(f.read())

import math
import datetime

def get_top_news(news_id):
    tags_cur = news[news_id]['tags']

    tags_set = set()

    news_score = {}
    for tag, _ in tags_cur:
        tags_set.add(tag)
    print(tags_set)
    for k, n in news.items():

        if k != news_id:
            if news[news_id]['topic'] == news[k]['topic']:
                score = 5
            else:
                score = 0
            tags_tmp = news[k]['tags']
            for tag, _ in tags_tmp:
                if tag in tags_set:
                    score += 1
            news_score[k] = score
            # print('ss', score)
    score_sorted = sorted(news_score.items(), key=lambda x: x[1], reverse=True)
    return score_sorted


def get_user_core(user_id):
    user_info = users_train[user_id]
    tags_cur = user_info['tags']
    topics_cur = user_info['topics']
    tags_score_cur = {}
    topics_score_cur = {}
    for tag, _ in tags_cur:
        if tag in tags_score_cur:
            tags_score_cur[tag] += 1
        else:
            tags_score_cur[tag] = 1
    for topic, _ in topics_cur:
        if topic in topics_score_cur:
            topics_score_cur[topic] += 1
        else:
            topics_score_cur[topic] = 1
    return tags_score_cur, topics_score_cur


def X(tags_core, topics_score):
    x = 0
    for tag, score in tags_core.items():
        x += score ** 2
    for topics, score in topics_score.items():
        x += score ** 2
    x = float(math.sqrt(x))
    # print(x)
    return x


def XY(x1, x2, y1, y2):
    xy = 0
    for tagx, scorex in x1.items():
        if tagx in y1:
            xy += scorex * y1[tagx]
    for topicx, scorex in x2.items():
        if topicx in y2:
            xy += scorex * y2[topicx]
    return xy


def get_top_users(user_id):
    tags_cur_core, topics_cur_score = get_user_core(user_id)
    # 余弦相似度
    # |X|=?
    x = X(tags_cur_core, topics_cur_score)
    score = {}
    if x != 0:
        for k, _ in users_train.items():
            if k != user_id and len(users_train[user_id]['click']) > 1:
                tags_tmp_core, topics_tmp_score = get_user_core(user_id)
                y = X(tags_tmp_core, topics_tmp_score)
                if y != 0:
                    xy = XY(tags_cur_core, topics_cur_score, tags_tmp_core, topics_tmp_score)
                    score[k] = float(xy) / float(x * y)
    # print(score)
    score = sorted(score,key=lambda x:x[1],reverse=True)[:10]

    return score


def get_user_history(user_id):
    click = users_train[user_id]['click']
    history = []
    for n_id,t in click:
        title = news[n_id]['title']
        news_time = news[n_id]['news_time']
        topic = news[n_id]['topic']

        times = datetime.datetime.fromtimestamp(int(t))

        history.append([n_id,title,topic,news_time.strip(),times.strftime('%Y-%m-%d %H:%M:%S')])

    return history


def user_count(user_id):
    info = users_train[user_id]
    topic_count = {}
    for topic, click_time in info['topics']:
        times = datetime.datetime.fromtimestamp(int(click_time))
        month = int(str(times).split('-')[0]) * 10000 + int(str(times).split('-')[1]) * 100 + int(
            str(times).split('-')[2].split(' ')[0])
        if month in topic_count:
            if topic in topic_count[month]:
                topic_count[month][topic] += 1
            else:
                topic_count[month][topic] = 1
        else:
            topic_count[month] = {topic: 1}
    topic_sum = {}
    for month, v in topic_count.items():
        for topic, c in v.items():
            if topic in topic_sum:
                topic_sum[topic] += c
            else:
                topic_sum[topic] = c
    tags_sum = {}
    for tag, _ in info['tags']:
        if tag in tags_sum:
            tags_sum[tag] += 1
        else:
            tags_sum[tag] = 1
    return topic_sum, tags_sum


def get_hot_news():
    with open('classification/data/rec_news/train.data') as f:
        latest_news = eval(f.read())[-1000:-1]
    news_count = {}
    for line in latest_news:
        if line[1] in news_count:
            news_count[line[1]] += 1
        else:
            news_count[line[1]] = 1
    news_sorted = sorted(news_count.items(), key=lambda x: x[1], reverse=True)[:10]
    hot_news = []
    for id, _ in news_sorted:
        title = news[id]['title']
        topic = news[id]['topic']
        tags = ''
        for tag, _ in news[id]['tags']:
            tags = tags + ' ' + tag
        news_time = news[id]['news_time'].replace('\n', '')
        hot_news.append([title, topic, tags.strip(), news_time, id])
    return hot_news


def get_top_n_user(user_id, n):
    users = get_top_users(user_id)
    user_top_n = sorted(users.items(), key=lambda x: x[1], reverse=True)[:n]
    return user_top_n


def get_top_user_news(user_id):
    print(user_id)
    news_hist = get_user_history(user_id)
    news_score = {}
    for i in news_hist:
        top_news = get_top_news(i[0])
        for t in top_news:
            id= t[0]
            if id in news_score:
                news_score[id] += 1
            else:
                news_score[id] = 1

    news_sorted = sorted(news_score,key=lambda x:x[1],reverse=True)[:10]
    # print(news_sorted)
    top_news = []
    for id in news_sorted:
        title = news[id]['title']
        topic = news[id]['topic']
        tags = ''
        for tag, _ in news[id]['tags']:
            tags = tags + ' ' + tag
        news_time = news[id]['news_time'].replace('\n', '')
        top_news.append([title, topic, tags.strip(), news_time, id])
    return top_news

# print(get_hot_news())
# print(user_count('5218791'))
# print(get_top_users('52550'))
# print(get_user_history('52550'))