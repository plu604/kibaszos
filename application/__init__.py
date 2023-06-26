# Package initialization and configuration

from flask import Flask
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__, template_folder="../website", static_folder="../website/static", static_url_path="/static")
app.config.from_object(ProductionConfig)

from application import routes