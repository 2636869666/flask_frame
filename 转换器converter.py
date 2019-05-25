from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class MyConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(MyConverter, self).__init__(url_map)
        self.regex = args[0]
# 此处用于取出url中的值传入此方法然后经过处理后再传入视图函数中
    def to_python(self, value):
        value+=value
        return value

# 此处用于redirect重定向中重定向到目标url时传入前先将可变属性传入本方法经过处理后再传入目标url中
    def to_url(self, value):
        value="222222"
        return value

# 此处为Myconverter设置一个名为re的键将其存储于url_map中，方便以后取用
app.url_map.converters["re"] = MyConverter


@app.route('/check/<re(r"\w{6}"):name>/<re(r"\d{6}"):age>')
def check(name, age):
    return "姓名：%s,年龄：%s" % (name, age)

@app.route('/regist')
def regist():
    return redirect(url_for("check",name ="aaaaaa",age = "123456"))
if __name__ == '__main__':
    app.run(debug=True)
