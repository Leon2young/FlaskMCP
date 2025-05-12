from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader #- 这是Flask-Login要求的回调函数，根据用户ID从数据库加载用户对象
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    mcp_services = db.relationship('MCPService', backref='owner', lazy=True)
    api_keys = db.relationship('APIKey', backref='user', lazy=True)
# - 继承 UserMixin 提供Flask-Login需要的默认方法，包含基本用户信息字段
# - 定义了两个一对多关系：
# - mcp_services : 用户创建的MCP服务
# - api_keys : 用户生成的API密钥

class MCPService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    service_url = db.Column(db.String(200), nullable=False)  # 服务部署地址
    is_private = db.Column(db.Boolean, default=False)        # 是否私有
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# - 存储MCP服务信息
# - 包含服务名称、描述、URL和隐私设置
# - 通过 user_id 外键关联到用户表

class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
# - 存储API密钥信息
# - 包含密钥值、所属用户和过期时间
# - 通过 user_id 外键关联到用户表