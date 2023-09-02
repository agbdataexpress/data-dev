from flask import Flask
from config import config
from views import views
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['dev'])
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = app.config['GOOGLE_CREDENTIALS_PATH']
    app.register_blueprint(views)
    app.run()
    