from flask import Flask, render_template

app = Flask(__name__)

#data를 딕셔너리 형태로 넘겨줌
@app.route("/")
def index():
    data = {  
        'title':'Flask Jinja Template',
        'user':'Emma',
        'is_admin':True,
        'items':['Item1','Item2','Item3']
    }

    title = 'flask Jinja Template'

    # ctrl+함수명 => 힘수에 대한 설명
    # (1) rendering할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=data, title = title, is_admin=True)

if __name__ == "__main__":
    app.run(debug=True)
