from flask import Flask
from flask import render_template, redirect
from flask import request,json
from dataproc import get_news as get_news_from_file
from dataproc import get_topic_news as get_topic_news_from_file
from dataproc import get_records
import  predict_news
app = Flask(__name__, static_folder='static/assets', static_url_path='/assets')
hot_news = predict_news.get_hot_news()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        u_id = request.form['id']
        return redirect('/user/id/' + u_id)


@app.route("/sign")
def sign():
    return "注册"


@app.route("/news")
def news():
    return "新闻"


@app.route("/news/id/<news_id>")
def get_news(news_id):
    news_topic = get_news_from_file()
    if news_id in news_topic:
        news = news_topic[news_id]
        sim_news = predict_news.get_top_news(news_id)
        top_user=predict_news.get_users_for_news(news_id)
        readers =predict_news.get_news_history(news_id)
        return render_template('news.html', news=news, id=news_id,hot_news=hot_news,sim_news=sim_news,top_user=top_user,readers=readers)
    else:
        return "404"


@app.route("/news/topic/<topic>")
def get_topic_news(topic):
    topics_news = get_topic_news_from_file()
    if topic in topics_news:
        news = topics_news[topic]
        return render_template('topic.html', news=news, topic=topic)
    else:
        return "404"


@app.route("/record/add/<user_id>/<news_id>")
def add_record(user_id, news_id):
    return "user:" + user_id + " has read news:" + news_id


@app.route("/record/get_all")
def get_all_record():
    return "all Records"


@app.route("/record/user/<user_id>")
def get_user_record(user_id):
    return "user:" + user_id + " records"


@app.route("/record/news/<news_id>")
def get_news_record(news_id):
    return "news:" + news_id + " records"


@app.route("/user/id/<user_id>")
def get_user(user_id):
    topic_sum,tags_sum = predict_news.user_count(user_id)
    tags=[]
    for tag,c in tags_sum.items():
        tags.append({"name":tag,"value":c})
    topics=[]

    for topic,c in topic_sum.items():
        topics.append({"name":topic,"value":c})
    history = predict_news.get_user_history(user_id)
    top_news= predict_news.get_top_user_news(user_id)
    top_user = predict_news.get_top_users(user_id)
    return render_template('user.html', id=user_id,tags=json.dumps(tags),topics=json.dumps(topics),hot_news=hot_news,history=history,top_news=top_news,top_user=top_user)


@app.route("/dashboard")
def dashboard():
    news_topic = get_news_from_file()
    # records = get_records()[:1000]
    # print(news_topic)
    return render_template('dashboard.html', news_topic=news_topic)


@app.route("/dashboard2")
def dashboard2():
    # news_topic = get_news_from_file()
    records = get_records()[:6000]
    # print(news_topic)
    return render_template('dashboard2.html', records=records)


if __name__ == '__main__':
    app.run(port=8888)
