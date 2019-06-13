from apps import app
from views import upload

if __name__ == '__main__':

    app.register_blueprint(upload.blue)

    app.run(host='0.0.0.0')