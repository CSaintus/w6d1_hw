from flask import Flask
from .blueprints.site.routes import site

bip = Flask(__name__)


bip.register_blueprint(site)