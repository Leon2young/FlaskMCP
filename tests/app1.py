from flask import Flask

# Flask路由
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'  # put application's code here


@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


@app.route('/flask')
def flask():
    return 'Hello flask'


@app.route('/python/')
def python():
    return 'Hello python'


# 对比route(/flask和/python/)，/flask是精确匹配，/python/是模糊匹配

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
# Flask 默认是单进程，单线程阻塞的任务模式；threaded : 多线程支持，默认为False，即不开启多线程
