from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from app.models import MCPService, APIKey
from app.utils.decorators import api_key_required

# API调用与认证
api_bp = Blueprint('api', __name__)
rest_api = Api(api_bp)


class MCPServiceResource(Resource):
    @api_key_required
    def get(self, service_id):
        service = MCPService.query.get_or_404(service_id)
        if service.is_private and service.user_id != current_user.id:
            return {'error': 'Permission denied'}, 403
        return {
            'id': service.id,
            'name': service.name,
            'url': service.service_url
        }


rest_api.add_resource(MCPServiceResource, '/services/<int:service_id>')
