from .category import router as category_router
from .auth import router as auth_router


def get_routers():
    return [auth_router, category_router]
