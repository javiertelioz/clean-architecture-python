from fastapi import APIRouter, Depends, status

from app.infrastructure.exception.utils import get_http_exception
from app.infrastructure.schemas.pydantic.user_schema import UserSchema, UserPostRequestSchema

from app.domain.models.user_entity import UserEntity
from app.domain.services.user_service import UserService
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from app.application.use_cases.user import CreateUserUseCase, GetUserByIdUseCase, UpdateUserUseCase, DeleteUserUseCase

router = APIRouter(prefix="/api/v1/users", tags=["User"])


@router.post(
    "",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    user: UserPostRequestSchema,
    use_case: CreateUserUseCase = Depends(),
) -> UserEntity:
    try:
        return use_case.execute(user)
    except UserAlreadyExistsException as e:
        raise get_http_exception(e)


@router.get(
    "/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    id: str,
    use_case: GetUserByIdUseCase = Depends(),
) -> UserEntity:
    try:
        return use_case.execute(id)
    except UserNotFoundException as e:
        raise get_http_exception(e)


@router.put(
    "/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def update(
    id: str,
    user: UserPostRequestSchema,
    use_case: UpdateUserUseCase = Depends(),
) -> UserEntity:
    try:
        return use_case.execute(id, user)
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
    use_case: DeleteUserUseCase = Depends(),
) -> None:
    try:
        use_case.execute(id)
    except UserNotFoundException as e:
        raise get_http_exception(e)
    except Exception as err:
        raise get_http_exception(err)
