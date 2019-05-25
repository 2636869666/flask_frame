import json

from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/json')
def str_json():
# 将字典转换为json格式的字符串
    data ={'name':'zhangsan','age':18}
    json_data1 = json.dumps(data)
    print(type(json_data1))
# 将字符串格式的字典先转换为字典再转换为json格式的字符串
    data2 = """{"name":"zhangsan","age":18}"""
    json_dict = json.loads(data2)
    json_data2 = json.dumps(json_dict)
    print(type(json_data2))
# 将字典转为json格式的数据
    data3 = {'name':'zhangsan','age':18}
    json_data3 = jsonify(data3)
    print(type(json_data3))
    return json_data1

if __name__ == '__main__':
    app.run(debug=True)