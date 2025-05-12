from flask import Flask, render_template

# Flask 模板

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index21.html')


if __name__ == '__main__':
    app.run(debug=True)



