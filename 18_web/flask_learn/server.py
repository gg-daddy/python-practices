from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return f'Hello World! @ {datetime.now()}'


@app.route('/index.html')
def index():
    '''
    Render a template, see: https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

    使用的是 Jinja2 模板引擎
    '''
    return render_template("index.html")


# Variable rules, see: https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
@app.route('/blog/<user_name>/<int:post_id>')
def blog(user_name=None, post_id=None):
    kwargs = {
        "name": user_name,
        "post": post_id
    }
    return render_template("blog_post.html", **kwargs)
