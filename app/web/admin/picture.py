com_ = """
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from app.libs.redprint import Redprint
from flask import render_template

admin = Redprint('picture')


#图片列表
@admin.route('/picture_list')
def picture_list():
    return render_template('admin/picture-list.html')


#图片展示
@admin.route('/picture_show')
def pictrue_show():
    return render_template('admin/picture-show.html')


#添加图片
@admin.route('/picture_add')
def pictrue_add():
    return render_template('admin/picture-add.html')


