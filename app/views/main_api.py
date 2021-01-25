from enum import Enum

from flask_restful import Resource, request
from flask import Blueprint

from app.models import User

main_api = Blueprint('main_api', __name__, url_prefix='/api')

class UserOrderBy(Enum):
    """Enum class for ordering options in UsersList class"""
    id = 1
    username = 2


class UserList(Resource):
    """
    Retrieve a list of users
    :queryparam page: page to retrieve from the query of users, default is 1
    :queryparam page_size: amount of users per page, default is 25
    :queryparam order_by: choices are id and username, by default is id
    :queryparam order: orders the results ascending(asc) or descending(desc), default is ascending
    :return: json object of users and paging data
    """
    def get(self):
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 25))
        order_by = request.args.get('order_by', 'id')
        order = request.args.get('order', 'asc')

        if order_by == UserOrderBy.username.name:
            users = User.order_by_username(order)
        else:
            users = User.order_by_id(order)
        users = users.paginate(page, per_page=page_size, error_out=False)
        return {'total': users.total,
                'pages': users.pages,
                'actual_page': users.page,
                'users': list(map(lambda x: x.json(), users.items))
                }
