from flask import session
from flask import jsonify, request, flash
from flask_security import auth_token_required, login_required, current_user
# from sqlalchemy.ext.serializer import Serializer
from . import api
from app.models.user import User
from app.models import db
from app.models.cart_master import Cart_master
from app.models.cart_detail import Cart_detail
from app.models.sku_price import Sku_price
from app.models.product_info import Product_info
@api.route('/cart', methods = ['POST'])
@auth_token_required
@login_required
def add_cart():

    sku_id = request.json.get("sku_id")
    quantity = request.json.get("quantity")
    # product_name = request.json.get("product_name")


    user = current_user._get_current_object()
    cart = Cart_master.query.filter_by(users = user).first()
    sku = Sku_price.query.filter_by(id = sku_id).first()
    # product_info = Product_info.query.filter_by(sku_price = sku).first()
    if cart is None:
        cart = Cart_master(user)
        cart.save()
        cart_detail = Cart_detail(cart, sku,quantity,
                                  sku.product_info.product_name)
        cart_detail.price = cart_detail.update_price()
        cart_detail.save()
        # cart.update_total_price()
        # cart.save()
    else:
        user_cart = Cart_master.query.filter_by(users = user).first()
        cart_detail = Cart_detail.query.filter_by(cart_master = user_cart).all()
        # cart_detail = Cart_detail.query.join(Cart_master,Cart_master.users==user)\
        #     .filter(Cart_detail.cart_master == )

        item_dict = {item.sku.id: item for item in cart_detail}
        # item_dict = cart_detail.item_dict()
        if sku.id in item_dict:
            item_dict[sku.id].quantity += quantity
            item_dict[sku.id].price = item_dict[sku.id].update_price()
            item_dict[sku.id].save()
            # user_cart.update_total_price()
            # user_cart.save()
        else:
            cart_detail = Cart_detail(cart, sku, quantity,sku.product_info.product_name)
            cart_detail.price = cart_detail.update_price()
            cart_detail.save()
            # user_cart.update_total_price()
            # user_cart.save()

    # cart.total = Cart_detail.query.filter_by(cart_master = cart).count()

    cart.update_total_price()
    cart.save()
    dict = cart.to_dict(depth=3, include=['cart_detail','sku'])
    # serializer = Serializer(cart, many=True)
    # data = serializer.data

    return jsonify(
        {
            "code":200,
            "message":"ok",
            "data":dict

            # "name":sku.product_info.product_name
        }
    )

@api.route('/cart',methods = ['DELETE'])
@auth_token_required
@login_required
def delete_item():
    sku_id = request.json.get('sku_id')
    user = current_user._get_current_object()
    cart = Cart_master.query.filter_by(users = user).first()
    Cart_detail.query.filter((Cart_detail.cart_master == cart) \
                             & (Cart_detail.sku_id==sku_id)).delete()
    # session.query(Cart_detail)
    # if cart_detail.sku_id ==
    # del_item = Cart_detail.query.filter_by(sku_id = sku_id ).first()
    # db.session.delete(del_item)
    db.session.commit()

    cart.update_total_price()
    cart.save()

    dict = cart.to_dict(depth=3, include=['cart_detail','sku'])

    return jsonify({
        "code": 204,
        "message":"ok",
        "data":dict

    })





