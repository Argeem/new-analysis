from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/sentiment')
def sentiment():
    return render_template("sentiment.html")

@views.route('/summary-articles')
def summaryArticles():
    return render_template("summary-article.html")
