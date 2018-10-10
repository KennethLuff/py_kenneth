"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from flask import Blueprint
from app.web.main import index


def create_blueprint_main():
    bp_main = Blueprint('main', __name__)

    index.main.register(bp_main)

    return bp_main
