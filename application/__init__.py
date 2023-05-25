# Package initialization and configuration

from flask import Flask
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__, template_folder="../website")
app.config.from_object(DevelopmentConfig)

from application import routes