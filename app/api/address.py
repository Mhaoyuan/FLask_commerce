# -*- coding: utf-8 -*-
import traceback
from flask import jsonify, request, current_app, abort
from flask_security import auth_token_required
from . import api
from app.models import User, Addr, db
@api.route('/user/<int:id>/address', methods = ['POST', 'GET'])
@auth_token_required
def address(id):
    # request_json = request.get_json(force=1)
    # print(request_json)
    user = User.query.get_or_404(id)
    if request.method =="GET":
        dict = user.to_dict(depth= 2, include='addr')
        return jsonify(dict)
    name = request.json.get("name")
    telephone = request.json.get("telephone")
    country = request.json.get("country")
    state = request.json.get("state")
    city = request.json.get("city")
    area = request.json.get("area")
    street = request.json.get("street")
    default = request.json.get('default')
    zip = request.json.get("zip")
    user_id = user.id
    address=Addr.query.filter_by(user_id = user.id, default = 1).first()
    if default and address:
        address.default = 0
        db.session.add(address)
        db.session.commit()
    try:
        current_address = Addr(name, telephone, country, state, city, area,
                               street, default, zip,user_id)
        db.session.add(current_address)
        db.session.commit()
        return jsonify({"code": 200, "message": "ok"}),200
    except:
        db.session.rollback()
        current_app.logger.error(traceback.format_exc())
        abort(500, traceback.format_exc())

@api.route('/address/<int:id>',methods = ['DELETE', 'PATCH'])
def address_(id):
    addr = Addr.query.get_or_404(id)
    if request.method == 'DELETE':
        try:
            db.session.delete(addr)
            db.session.commit()
            return jsonify({"code": 200, "message": "ok"}), 200
        except:
            db.session.rollback()
            current_app.logger.error(traceback.format_exc())
            abort(500, traceback.format_exc())





