from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import MCPService
from app.forms import ServiceForm

# MCP服务管理
services_bp = Blueprint('services', __name__)


@services_bp.route('/')
@login_required
def index():
    services = MCPService.query.filter_by(user_id=current_user.id).all()
    return render_template('services/index.html', services=services)


@services_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = MCPService(
            name=form.name.data,
            description=form.description.data,
            service_url=form.url.data,
            is_private=form.is_private.data,
            user_id=current_user.id
        )
        db.session.add(service)
        db.session.commit()
        flash('Service added!', 'success')
        return redirect(url_for('services.index'))
    return render_template('services/add.html', form=form)
