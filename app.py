from flask import Flask
from flask import render_template,redirect
from flask import request
from dataproc import get_news as get_news_from_file
from dataproc import get_topic_news as get_topic_news_from_file
from dataproc import get_records
app = Flask(__name__, static_folder='static/assets', static_url_path='/assets')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        u_id = request.form['id']
        return redirect('/user/id/'+u_id)


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
        return render_template('news.html', news=news, id=news_id)
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
    return render_template('user.html')


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
