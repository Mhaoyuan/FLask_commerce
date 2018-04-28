from . import AppModelView
from flask_admin.form import rules
from flask_admin.actions import action
from app.models.user import User
from flask import flash
class UserModelView(AppModelView):
    column_exclude_list = ['password','create_datetime', 'update_datetime']
    form_create_rules = ('username', rules.Text('Foobar'),'email', 'phone', 'supplier_info')
    form_columns = ['username','email','phone', 'supplier_info']

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