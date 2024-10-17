from flask import Flask
from flask_smorest import Api
from api import blp  # api라는 파일에서 blp import시킨다

app = Flask(__name__)

# OpenAPI 관련 설정 (GPT와 관련 없는 tool)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)



# 디버깅 기능 활용해서 스텝 바이 스텝 확인 (왼쪽 빨간점 찍어주기)