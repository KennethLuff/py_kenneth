"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""
from app.libs.redprint import Redprint
from flask import render_template

main = Redprint('index')


@main.route('', methods=['GET'])
def index():
    return render_template('main/index.html')


