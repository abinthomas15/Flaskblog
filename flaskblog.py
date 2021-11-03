from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'Content':'First Post Content',
        'Date_Posted':'April 20,2018'
    },
    {
        'author':'Abin Thomas',
        'title':'Blog Post 2',
        'Content':'Second Post Content',
        'Date_Posted':'April 21,2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug==True)
