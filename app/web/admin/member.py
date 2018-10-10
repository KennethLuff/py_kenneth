"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from flask import render_template

from app.libs.redprint import Redprint

admin = Redprint('member')


# 添加会员
@admin.route('/member_add', methods=['GET'])
def member_add():
    return render_template('admin/member-add.html')


# 显示会员详细信息
@admin.route('/member_show', methods=['GET'])
def member_show():
    return render_template('admin/member-show.html')

# 会员列表
@admin.route('/member_list', methods=['GET'])
def member_list():
    return render_template('admin/member-list.html')


# 删除的会员
@admin.route('/member_del', methods=['GET'])
def member_del():
    return render_template('admin/member-del.html')


# 会员等级管理
@admin.route('/member_level', methods=['GET'])
def member_level():
    return render_template('admin/member-level.html')


# 积分管理
@admin.route('/member_scoreoperation', methods=['GET'])
def member_scoreoperation():
    return render_template('admin/member-scoreoperation.html')


# 浏览记录
@admin.route('/member_record_browse', methods=['GET'])
def member_record_browse():
    return render_template('admin/member-record-browse.html')


# 下载记录
@admin.route('/member_record_download', methods=['GET'])
def member_record_download():
    return render_template('admin/member-record-download.html')


# 分享记录
@admin.route('/member_record_share', methods=['GET'])
def member_record_share():
    return render_template('admin/member-record-share.html')
