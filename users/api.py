from ninja import Router
from django.contrib.auth.models import User
from typing import List

from users.schemas.user_schema import UserRequest, UserResponse
from users.services.user_service import create_user, get_users

user_router = Router()

@user_router.get("/view", response=List[UserResponse])
def view(request):
    return get_users()


@user_router.post("register")
def register(request, data: UserRequest):
   return create_user(data)
