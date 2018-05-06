from flask import flash
from . import AppModelView
from flask_admin.actions import action
from app.models.shop_info import Shop_Info
from app.models.user import User
from app.models.role import Role
from app.models import db
from security import user_datastore
class ShopModelView(AppModelView):

    column_searchable_list = ['link_man', 'country','state','city','address']

    column_labels = {
        'create_datetime': u'创建时间',
        'update_datetime':u'更新时间',
        'shop_code':u'店铺编码',
        'shop_type':u'店铺类型',
        'link_man':u'联系人',
        'phone_number':u'手机号',
        'country':u'国家',
        'state':u'省',
        'city':u'市',
        'address':u'详细地址',
        'status':u'店铺状态',
        'users':u'所属用户'
    }

    column_list = ('users','create_datetime','update_datetime',
                   'shop_code','shop_type','link_man',
                   'phone_number','country','state',
                   'city', 'address', 'status')

    # column_select_related_list = True
    can_delete = False
    can_edit =  False
    can_create = False
    can_view_details = True
    @action('approvey', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = Shop_Info.query.filter(Shop_Info.id.in_(ids))

            for shop in query.all():
                if shop.status == 0:
                    user = shop.users
                    user.shop_status = u'已通过'
                    user_datastore.add_role_to_user(user,'Shop')
                    shop.status= 1
                    user.save()
                    shop.save()
                    # db.session.commit()
                    flash(u'店铺开通成功')
                else:
                    flash(u'请选择未许可店铺')

        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash('Failed to approve users. %(error)s')
