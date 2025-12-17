from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from book_api.books.models import books
from book_api.books.schemas import BookCreate


async def add_book(session: AsyncSession, new_operation) -> int:
    """
    Add a new book to database.

    :param session: Async session to database
    :param new_operation: instance of the BookCreate class

    :return: response status 201 if book added
    """

    new_operation.title = new_operation.title.upper()
    new_operation.author = new_operation.author.upper()

    stmt = (
        insert(books).
        values(**new_operation.model_dump())
    )

    await session.execute(stmt)
    await session.commit()

    return 201


async def get_books(session: AsyncSession) -> (int, list):
    """
    Get all books from database.
    :return: response status, list of books
    """

    smtp = select(books)

    res = await session.execute(smtp)

    res_list = [{"id": row[0], "title": row[1], "author": row[2], "year": row[3]} for row in res]

    return 200, res_list


async def delete_book_by_id(session: AsyncSession, book_id: int):
    """
    Delete book from database by id.
    :return: response status
    """

    smtp = delete(books).where(books.c.id == book_id).returning("*")

    res = await session.execute(smtp)
    await session.commit()

    deleted_book = [book for book in res]
    if deleted_book:
        return 200
    else:
        return 404


async def change_book_by_id(session: AsyncSession, book_id: int, new_operation: BookCreate) -> int:
    """
    Change book from database by id.
    :return: response status
    """

    new_operation.title = new_operation.title.upper()
    new_operation.author = new_operation.author.upper()

    smtp = update(books).where(books.c.id == book_id).values(**new_operation.model_dump()).returning("*")

    res = await session.execute(smtp)
    await session.commit()

    updated_book = [book for book in res]

    if updated_book:
        return 200
    else:
        return 404


async def found_books(session: AsyncSession, title, author, year) -> (int, list):
    """
    Found books from database by title, author or year.
    :return: response status, list of books
    """

    if title is not None:
        title = title.upper()

    if author is not None:
        author = author.upper()

    smtp = (
        select(books)
        .where(title is None or books.c.title == title)
        .where(author is None or books.c.author == author)
        .where(year is None or books.c.year == year)
    )

    res = await session.execute(smtp)

    res_list = [{"id": row[0], "title": row[1], "author": row[2], "year": row[3]} for row in res]

    if res_list:
        return 200, res_list
    else:
        return 204, res_list
