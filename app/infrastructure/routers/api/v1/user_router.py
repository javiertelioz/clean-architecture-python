from fastapi import APIRouter, Depends, status

from app.infrastructure.exception.utils import get_http_exception
from app.infrastructure.schemas.pydantic.user_schema import UserSchema, UserPostRequestSchema

from app.domain.models.user_entity import UserEntity
from app.domain.services.user_service import UserService
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException

router = APIRouter(
    prefix="/api/v1/users", tags=["User"]
)


@router.post(
    "",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    user: UserPostRequestSchema,
    userService: UserService = Depends(),
) -> UserEntity:
    try:
        return userService.create(user).normalize()
    except UserAlreadyExistsException as e:
        raise get_http_exception(e)


@router.get(
    "/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def get(
    id: str,
    userService: UserService = Depends(),
) -> UserEntity:
    return userService.get(id).normalize()


@router.put(
    "/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def update(
    id: str,
    user: UserPostRequestSchema,
    userService: UserService = Depends(),
) -> UserEntity:

    try:
        return userService.update(id, user).normalize()
    except UserNotFoundException as e:
        raise get_http_exception(e)
    except Exception as err:
        raise get_http_exception(err)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    id: str,
    userService: UserService = Depends(),
) -> None:
    try:
        userService.delete(id)
    except UserNotFoundException as e:
        raise get_http_exception(e)
    except Exception as err:
        raise get_http_exception(err)
