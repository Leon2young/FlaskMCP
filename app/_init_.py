from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
#- 导入了Flask核心和主要扩展(SQLAlchemy, LoginManager, Migrate)，并创建了这些扩展的全局实例

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #- create_app 是标准的Flask应用工厂模式，使用 `Config` 类作为默认配置
    
    # 初始化插件
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    #- 将全局扩展实例与当前应用绑定,特别注意 migrate 需要同时传入 db 实例
    
    # 注册蓝图
    from app.routes.auth import auth_bp
    from app.routes.services import services_bp
    from app.routes.api import api_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(services_bp, url_prefix='/services')
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    # - 从不同模块导入蓝图
    # - 为每个蓝图指定了URL前缀
    # - 认证(/auth)、服务(/services)和API(/api/v1)路由分离
    return app