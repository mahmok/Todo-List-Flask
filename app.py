from flask import Flask


def create_app():
    from models import init as ModelsInit
    from routes import init as RoutesInit
    flask_app = Flask(__name__)
    flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
    ModelsInit(flask_app)
    RoutesInit(flask_app)
    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
