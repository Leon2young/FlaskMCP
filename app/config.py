import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    # 基础配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///cloud_mcp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # - SECRET_KEY : Flask应用的安全密钥，用于加密会话等。优先从环境变量获取，如果没有则使用默认值
    # - SQLALCHEMY_DATABASE_URI : 数据库连接字符串， 默认使用SQLite数据库，文件名为 cloud_mcp.db
    # - SQLALCHEMY_TRACK_MODIFICATIONS : 禁用SQLAlchemy的修改跟踪以提升性能
    # 权限配置
    MCP_API_KEY_EXPIRES = 3600  # API密钥有效期（秒）3600s=1h