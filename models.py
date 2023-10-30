from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Stock(Base):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_book: Mapped[int] = mapped_column(ForeignKey("book.id"))
    id_shop: Mapped[int] = mapped_column(ForeignKey("shop.id"))
    count: Mapped[int] = mapped_column()


class Sale(Base):
    __tablename__ = "sale"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[int] = mapped_column(Float)
    date_sale: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    id_stock: Mapped[int] = mapped_column(ForeignKey("stock.id"))


class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[int] = mapped_column(Integer)
    id_publisher: Mapped[int] = mapped_column(ForeignKey("publisher.id"))


class Publisher(Base):
    __tablename__ = "publisher"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)