from flask import redirect,request,url_for

from flask.ext.admin.base import MenuLink

from app.models import db
from app.models.user import User
from app.models.shop_info import Shop_Info

# class AuthShopMenulik(MenuLink):

