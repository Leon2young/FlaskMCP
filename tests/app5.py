from flask import Flask, render_template, request
from werkzeug.wrappers.response import ResponseStream

app = Flask(__name__)


# Flask 将表单数据发送到模板

@app.route('/')
def student():
    return render_template('index5.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        rst = request.form
        return render_template("result5.html", result=rst)


if __name__ == '__main__':
    app.run(debug=True)
