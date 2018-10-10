"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from flask import render_template

from app.libs.redprint import Redprint

admin = Redprint('index')


@admin.route('', methods=['GET'])
def index():
    return render_template('admin/index.html')
