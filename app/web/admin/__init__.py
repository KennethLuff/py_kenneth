"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from flask import Blueprint
from app.web.admin import index, member, article, picture, product, admin,\
    system


def create_blueprint_admin():
    bp_admin = Blueprint('admin', __name__)

    member.admin.register(bp_admin)
    index.admin.register(bp_admin)
    article.admin.register(bp_admin)
    picture.admin.register(bp_admin)
    product.admin.register(bp_admin)
    admin.admin.register(bp_admin)
    system.admin.register(bp_admin)

    return bp_admin
