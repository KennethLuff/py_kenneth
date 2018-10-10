"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from app.libs.redprint import Redprint
from flask import render_template

admin = Redprint('article')


# 资讯列表
@admin.route('/article_list')
def article_list():
    return render_template('admin/article-list.html')


# 添加资讯
@admin.route('/article_add')
def article_add():
    return render_template('admin/article-add.html')