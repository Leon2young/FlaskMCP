from flask import Flask, redirect, url_for

# flask url构建:处理动态URL
# redirect重定向
# url_for函数，基本用法是传入视图函数的名称作为第一个参数。如果视图函数接受参数，那么可以通过关键字参数的形式传递给url_for函数。
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
