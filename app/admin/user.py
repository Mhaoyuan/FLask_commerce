# -*- coding: utf-8 -*-
from . import AppModelView
from flask_admin.form import rules
from flask_admin.actions import action
from app.models.user import User
from flask import flash
class UserModelView(AppModelView):
    column_exclude_list = ['password']
    form_columns = ['username','email','phone']
    column_editable_list = ['confirmed']
    column_searchable_list = ['username', 'email','phone']
    column_details_exclude_list = ['password']

    column_labels = {
        'create_datetime': u'注册时间',
        # 'update_datetime': u'登录时间',
        'username': u'用户名',
        'email': u'邮箱',
        'phone': u'手机号',
        'confirmed':u'认证',
        'confirmed_at':u'认证时间',
        'current_login_at':u'登录时间',
        'current_login_ip':u'登录ip',
        'last_login_ip':u'下线ip',
        'login_count':u'登录次数',
        'roles':u'用户权限'
    }
    column_list = ('create_datetime','username','email','phone',
                    'confirmed','confirmed_at','current_login_at',
                    'current_login_ip','last_login_ip','login_count','roles')

    column_auto_select_related = True
    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True



    @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = User.query.filter(User.id.in_(ids))

            count = 0
            for user in query.all():
                if user.approve():
                    count +=1
            flash('successfuly')

        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise