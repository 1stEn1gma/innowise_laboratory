from sqlalchemy import Table, Column, Integer, String

from books.database import metadata

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("author", String, nullable=False),
    Column("year", Integer)
)
