"""
  Created by Kenneth Luff
  Email: kennethluff@outlook.com
"""

from flask import render_template
from app.libs.redprint import Redprint

admin = Redprint('product')


#品牌管理
@admin.route('/product-brand')
def product_brand():
    return render_template('admin/product-brand.html')

#编辑品牌
@admin.route('/product-codeing')
def product_codeing():
    render_template('admin/codeing.html')


#分类管理
@admin.route('product-category')
def product_category():
    return render_template('admin/product-category.html')


#添加分类
@admin.route('product-category-add')
def product_category_add():
    return render_template('admin/product-category-add.html')


#产品列表
@admin.route('product-list')
def product_list():
    return render_template('admin/product-list.html')


#添加产品
@admin.route('product-add')
def product_add():
    return render_template('admin/product-add.html')

