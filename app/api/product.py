# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask_security import roles_required, login_required,auth_token_required, current_user
from app.models import db, User, Product_info, Shop_Info, sku_price
from app.models.sku_price import Sku_price
from app.models.product_category import Product_Category
from app.models.brand_info import Brand_info
from app.models.shop_info import Shop_Info
from app.models.warehouse_product import Warehouse_Product
from . import api


@api.route('/shop/product', methods = ['POST','GET'])
@login_required
@auth_token_required
@roles_required('Shop')
def create_product():
    if request.method == "POST":
        shop = Shop_Info.query.filter_by(users = current_user).first()
        product_name = request.json.get("product_name")
        product_enname = request.json.get("product_enname")
        # bar_code = request.json.get("bar_code")
        publish_status = request.json.get("publish_status")
        mass = request.json.get("mass")
        purer = request.json.get("purer")
        price = request.json.get("price")
        category_id = request.json.get("category_id")
        brand_name = request.json.get("brand_name")
        brand_desc = request.json.get("publish_status")
        current_cnt = request.json.get("current_cnt")

        sku = Sku_price(mass, purer, price)
        sku.save()
        category = Product_Category.query.get_or_404(category_id)
        warehouse = Warehouse_Product(current_cnt)
        warehouse.save()
        brand = Brand_info(brand_name, brand_desc)
        brand.save()

        items = Product_info(product_name, product_enname,
                             publish_status, brand,category,shop,sku, warehouse)

        items.save()
        # return items.to_dict(depth=2)
        # return items.to_dict(depth=1)
        dict = items.to_dict(depth=2,include=['sku_price', 'warehouse_info',
                                               'brand_info', 'category'])
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": dict
        })

    if request.method =="GET":
        shop = Shop_Info.query.filter_by(users = current_user).first()
        items = Product_info.query.filter_by(shop = shop).all()
        # for item in items:
        #     res = item.to_dict(depth=2, include=['sku_price'])
        res = [item.to_dict(depth=2, include=['sku_price','category','brand_info', 'warehouse_info']) \
               for item in items]
        return jsonify({
            "code": 200,
            "message":"ok",
            "data": res
        })













