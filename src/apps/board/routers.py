from fastapi import APIRouter

from src.apps.board.endpoint import category, toolkit, project


board_router = APIRouter()

board_router.include_router(category.category_router, prefix='/category')
# board_router.include_router(category.tookit_router, prefix='/toolkit')
# board_router.include_router(category.project_router, prefix='/project')