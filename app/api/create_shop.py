from flask import request,url_for, jsonify
from flask_security import auth_token_required, login_required, current_user
from app.models import User, Role, Shop_Info
from . import api


@api.route('/shop',methods = ['POST'])
@login_required
@auth_token_required
def create_shop():
    user = current_user._get_current_object()
    if current_user.has_role('Shop') :
        return url_for('api.get_shop')
    if user.shop_status == 1 :
        return jsonify(
            {
                "code":200,
                "message":u"审核中，请稍等"
            }
        )
    shop_name = request.json.get("shop_name")
    shop_type = request.json.get("shop_type")
    link_man = request.json.get("link_man")
    phone_number = request.json.get("phone_number")
    country = request.json.get("country")
    state = request.json.get("state")
    city = request.json.get("city")
    address = request.json.get("address")
    # if phone_number.isdigit() is not True:
    #     return jsonify(
    #         {
    #             "code": 406,
    #             "message":u"请输入正确手机号"
    #         }
    #     )
    user.shop_status = 1
    shop = Shop_Info(user, shop_name, shop_type, link_man, phone_number,
                     country, state, city, address)
    shop.save()
    user.save()

    dict = shop.to_dict(depth=1)
    return jsonify(
        {
            "code" : 202,
            "message":u"等待审核",
            "data":dict
        }
    )





@api.route('/shop',methods = ['GET'])
@login_required
@auth_token_required
def get_shop():
    if current_user.has_role('Shop') is False:
        return url_for('api.create_shop')
    return 'za'
