"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""

from flask import render_template
from app.libs.redprint import Redprint

admin = Redprint('admin')


#角色管理
@admin.route('admin_role')
def admin_role():
    return render_template('admin/admin-role.html')


#添加角色
@admin.route('admin_role_add')
def admin_role_add():
    return render_template('admin/admin-role-add.html')


#权限管理
@admin.route('admin_permission')
def admin_permission():
    return render_template('admin/admin-permission.html')


#管理员列表
@admin.route('admin_list')
def admin_list():
    return render_template('admin/admin-list.html')

#添加管理员
@admin.route('admin_add')
def admin_add():
    return render_template('admin/admin-add.html')