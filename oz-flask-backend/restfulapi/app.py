from flask import Flask
from flask_restful import Api
from resources.item import Item     # resources/item 폴더에서 불러온다


app = Flask(__name__)
api = Api(app)   # initializing 작업

    

api.add_resource(Item, '/item/<string:name>')  # 경로 추가

if __name__ == '__main__':
    app.run(debug=True)


## 주의: 서버를 끄면 데이터도 날라간다.