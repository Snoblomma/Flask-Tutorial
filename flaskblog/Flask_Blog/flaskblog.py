from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Kate',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 28, 2019'
    },
    {
        'author': 'Kate',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 29, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)