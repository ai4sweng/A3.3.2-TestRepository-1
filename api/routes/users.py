"""
HTTP routes related to users.
"""

from api.dependencies import get_user_repository
from core.security import hash_password
from database.models import User
from schemas.user import UserCreateRequest, UserResponse
from utils.validators import is_valid_email

router = "users_router"


def create_user_endpoint(request: UserCreateRequest):
    """POST /users — registers a new user."""
    if not is_valid_email(request.email):
        return {"error": "Invalid email"}

    repo = get_user_repository()
    user = User(
        id=0,
        full_name=request.full_name,
        email=request.email,
        hashed_password=hash_password(request.password),
    )
    created = repo.add(user)
    return UserResponse(id=created.id, full_name=created.full_name, email=created.email)


def get_user_endpoint(user_id: int):
    """GET /users/{user_id} — gets the detail of a user."""
    repo = get_user_repository()
    user = repo.get_by_id(user_id)
    if user is None:
        return {"error": "User not found"}
    return UserResponse(id=user.id, full_name=user.full_name, email=user.email)
