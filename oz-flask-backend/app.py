from flask import Flask, request, Response
# import test

app =  Flask(__name__)

# host = '127.0.0.1'
# port = '5000'

@app.route('/')
def home():
    return "Hello, this is Main Page"

# http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return "Hello, this is About Page"

# http://127.0.0.1:5000/compnay
@app.route('/company')
def company():
    return "Hello, this is Company Page"

# 코드 복사 키
# Windows: alt + shift + 화살표 위/아래
# Mac: option + shift + 화살표 위/아래

# 동적으로 URL 파라미터 값을 받아서 처리해준다.

# http://127.0.0.1:5000/user/inseop
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

# http://127.0.0.1:5000/user/inseop
@app.route('/number/<int:number>')
def number(number):
    return f'Number : {number}'



# post 요청 날리는 법
# 1. postman
# 2. requests
import requests  #pip install requests
app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response


# http://127.0.0.1:5000/submit
@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print("GET method")
    if request.method == 'POST':
        print("***POST method***", request.data)
    return Response("Success", status=200)

if __name__ == "__main__":
    # print("__name__ :", __name__)
    app.run()