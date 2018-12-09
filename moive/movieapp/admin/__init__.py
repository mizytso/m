from flask import Blueprint

admin = Blueprint("admin", __name__)
import movieapp.admin.views
