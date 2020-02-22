from flask import Blueprint
from flask_login import current_user, login_required

from app.forms.upload import UploadForm
from app.forms.login import LoginForm
from app.models.user import User
from app.libs.auth import admin_only

from flask import render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    form = UploadForm()
    return render_template('index.html',
                           form=form,
                           user=current_user)


@bp.route('/lists')
def lists():
    content = []
    data = User.search()
    for i in data['data']:
        content.append([i.studentId,
                        i.nickname,
                        ['普通用户', '管理员'][i.permission],
                        i.update_time])

    return render_template('list.html',
                           count=data['count'],
                           labels=['学号', '姓名', '权限', '时间'],
                           content=content,
                           user=current_user)


@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',
                           form=form,
                           user=current_user)


@bp.route('/admin')
@login_required
@admin_only
def admin():
    return render_template('admin.html',
                           user=current_user)
