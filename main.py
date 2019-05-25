from flask import Flask, render_template, request, make_response, url_for, redirect
from werkzeug.routing import BaseConverter

import json_demo
app = Flask(__name__)

class MyConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super().__init__(url_map)
        self.regex = args[0]
    def to_python(self, value):
        value = "aaaaaa"
        return value
    def to_url(self, value):
        value = "bbbbbb"
        return value
# 作为字典存入url_map方便取用
app.url_map.converters["re"]= MyConverter

@app.route('/')
def index():
    # 模板渲染，在此处渲染后返回给浏览器,并可以在后面自定义状态码
    return render_template('index.html'),666

@app.route('/login',methods=["get","post"])
def login():
    # 在同一页面进行登录和校验
    if request.method == 'post':
        # 利用request获取相应的值
        uname = request.form.get("username")
        pwd = request.form.get("password")
        if uname == 'a' and pwd == 'a':
            response = make_response("登录成功")
            response.cookie.set = uname
            response.cookie.set = pwd
            return response
    # 此处渲染的页面是以输入地址而发起的请求，所以为GET请求
    return render_template('login.html')

@app.route('/check/<name>/<age>')
def check(name,age):
    return"姓名为%s,年龄为%s"%(name,age)

@app.route('/demo')
def demo():
    return redirect(url_for(json_demo.str_json))
    # return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)