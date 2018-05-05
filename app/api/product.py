# -*- coding: utf-8 -*-
from flask import request
from flask_security import roles_required, login_required,auth_token_required
from app.models import db, User, Product_info, Shop_Info
from . import api


@api.route('/shop/product', methods = ['POST','GET'])
@login_required
@auth_token_required
@roles_required('Shop')
def create_product():
    if request.method == "POST":
        product_name = request.json.get("product_name")
        product_enname = request.json.get("product_enname")
        bar_code = request.json.get("bar_code")
        mass = request.json.get("mass")
        purer = request.json.get("purer")
        price = request.json.get("price")
        category_id = request.json.get("category_id")












