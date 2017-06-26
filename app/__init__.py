from flask import Flask, redirect, session
from app.mod_tables.models import TableBuilder


flask_app = Flask(__name__)

table_builder = TableBuilder()


from app.common.routes import main
from app.mod_tables.controllers import tables


# Register the different blueprints
flask_app.register_blueprint(main)
flask_app.register_blueprint(tables)
