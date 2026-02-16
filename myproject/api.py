from ninja import NinjaAPI

from users.api import user_router


api = NinjaAPI(title="Technical Test Requirement")

api.add_router('users', user_router)