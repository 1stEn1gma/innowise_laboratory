from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from book_api.books.schemas import BookCreate, ResponseForBooks, BaseResponse
from book_api.books.usefull_moduls import get_books, delete_book_by_id, change_book_by_id, found_books, add_book
from book_api.books.database import get_async_session


router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post(
    "/",
    response_model=BaseResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Item created successfully"},
    }
)
async def router_add_book(
        new_operation: BookCreate,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        status = await add_book(session, new_operation)

        return {
            "status": status,
            "data": None,
            "details": None
        }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=None
        )


@router.get("/", response_model=ResponseForBooks)
async def router_get_books(
        session: AsyncSession = Depends(get_async_session)
):
    try:
        status, all_books = await get_books(session)

        return {
            "status": status,
            "data": all_books,
            "details": None
        }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=None
        )


@router.delete("/", response_model=BaseResponse)
async def router_delete_book_by_id(
        book_id: int,
        session: AsyncSession = Depends(get_async_session)):
    status = 200

    try:
        status = await delete_book_by_id(session, book_id)

        if status != 200:
            raise Exception

        return {
            "status": status,
            "data": None,
            "details": None
        }
    except Exception as error:
        if status == 404:
            raise HTTPException(
                status_code=status,
                detail=None
            )
        else:
            raise HTTPException(
                status_code=500,
                detail=None
            )


@router.put("/", response_model=BaseResponse)
async def router_update_book(
        book_id: int,
        new_operation: BookCreate,
        session: AsyncSession = Depends(get_async_session)
):
    status = 200

    try:
        status = await change_book_by_id(session, book_id, new_operation)

        if status != 200:
            raise Exception

        return {
            "status": status,
            "data": None,
            "details": None
        }
    except Exception as error:
        if status == 404:
            raise HTTPException(
                status_code=status,
                detail=None
            )
        else:
            raise HTTPException(
                status_code=500,
                detail=None
            )


@router.get(
    "/search/",
    response_model=ResponseForBooks,
    responses={
        204: {"description": "No Content"}
    }
)
async def router_search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    session: AsyncSession = Depends(get_async_session)
):
    status = 200

    try:
        status, founded_books = await found_books(session, title, author, year)

        return {
            "status": status,
            "data": founded_books,
            "details": None
        }
    except Exception as error:
        if status == 404:
            raise HTTPException(
                status_code=status,
                detail=None
            )
        else:
            raise HTTPException(
                status_code=500,
                detail=None
            )
