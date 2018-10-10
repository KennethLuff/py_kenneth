"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""

from flask import render_template
from app.libs.redprint import Redprint

admin = Redprint('system')


#基本设置
@admin.route('/system-base')
def system_base():
    return render_template('admin/system-base.html')


#栏目管理
@admin.route('/system-category')
def system_category():
    return render_template('admin/system-category.html')


#添加栏目
@admin.route('/system-category-add')
def system_category_add():
    return render_template('admin/system-category-add.html')


#数据字典
@admin.route('/system-data')
def system_data():
    return render_template('admin/system-data.html')


#屏蔽词
@admin.route('/system-shielding')
def system_shielding():
    return render_template('admin/system-shielding.html')


#系统日志
@admin.route('/system-log')
def system_log():
    return render_template('admin/system-log.html')
