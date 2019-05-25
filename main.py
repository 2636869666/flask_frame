from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["get","post"])
def login():
    if request.method == 'post':
        uname = request.form.get("username")
        pwd = request.form.get("password")
        if uname == 'a' and pwd == 'a':
            response = make_response("登录成功")

            return response
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)