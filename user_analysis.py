with open('classification/data/rec_news/news.json', 'r') as f:
    news = eval(f.read())


def pre_train():
    users = {}
    with open('classification/data/rec_news/train.data', 'r') as f:
        train_set = eval(f.read())
    for item in train_set:
        u_id = item[0]
        news_id = item[1]
        click_time = int(item[2])
        news_cur = news[news_id]
        if 'click' in news_cur:
            news_cur['click'].append((u_id, click_time))
        else:
            news_cur['click'] = [(u_id, click_time)]
        news[news_id] = news_cur
        news_tags = []
        for tag, _ in news[news_id]['tags']:
            news_tags.append((tag, click_time))
        if u_id in users:
            if 'topics' in users[u_id]:
                users[u_id]['topics'].append((news[news_id]['topic'], click_time))
            else:
                users[u_id]['topics'] = [(news[news_id]['topic'], click_time)]
            if 'tags' in users[u_id]:
                users[u_id]['tags'] += news_tags
            else:
                users[u_id]['tags'] = news_tags
            if 'click' in users[u_id]:
                users[u_id]['click'].append((news_id, click_time))
            else:
                users[u_id]['click'] = [(news_id, click_time)]
        else:
            users[u_id] = {}
            users[u_id]['topics'] = [(news[news_id]['topic'], click_time)]
            users[u_id]['tags'] = news_tags
            users[u_id]['click'] = [(news_id, click_time)]

    with open('classification/data/rec_news/news_train.data', 'w') as f:
        f.write(str(news))
    with open('classification/data/rec_news/user_train.data', 'w') as f:
        f.write(str(users))


def pre_test():
    users = {}
    with open('classification/data/rec_news/test.data', 'r') as f:
        train_set = eval(f.read())

    for item in train_set:
        u_id = item[0]
        news_id = item[1]
        click_time = int(item[2])
        news_cur = news[news_id]
        if 'click' in news_cur:
            news_cur['click'].append((u_id, click_time))
        else:
            news_cur['click'] = [(u_id, click_time)]
        news[news_id] = news_cur
        news_tags = []
        for tag, _ in news[news_id]['tags']:
            news_tags.append((tag, click_time))
        if u_id in users:
            if 'topics' in users[u_id]:
                users[u_id]['topics'].append((news[news_id]['topic'], click_time))
            else:
                users[u_id]['topics'] = [(news[news_id]['topic'], click_time)]
            if 'tags' in users[u_id]:
                users[u_id]['tags'] += news_tags
            else:
                users[u_id]['tags'] = news_tags
            if 'click' in users[u_id]:
                users[u_id]['click'].append((news_id, click_time))
            else:
                users[u_id]['click'] = [(news_id, click_time)]
        else:
            users[u_id] = {}
            users[u_id]['topics'] = [(news[news_id]['topic'], click_time)]
            users[u_id]['tags'] = news_tags
            users[u_id]['click'] = [(news_id, click_time)]

    with open('classification/data/rec_news/news_test.data', 'w') as f:
        f.write(str(news))
    with open('classification/data/rec_news/user_test.data', 'w') as f:
        f.write(str(users))

pre_test()