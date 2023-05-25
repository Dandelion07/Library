from Section import Section
from datetime import date
from enum import Enum
from Member import Member
from DatabaseManager import DatabaseManager

class BookStatus(Enum):
    Available = "موجود"
    Loaned = "امانت"
    Reserved = "رزروشده"

    @classmethod
    def set(cls, status):
        if status == BookStatus.Available.value:
            return BookStatus.Available
        elif  status == BookStatus.Loaned.value:
            return BookStatus.Loaned
        elif status == BookStatus.Reserved.value:
            return BookStatus.Reserved

class Book:
    def __init__(self, book_id: int = None,
                 name: str = None,
                 authors: str = None,
                 translators: str = None,
                 publication_name: str = None, 
                 release_date: date = None, 
                 status: BookStatus = BookStatus.Available, 
                 section: Section = None, 
                 reserved_by: Member = None) -> None:
        self.book_id: int = book_id
        self.name: str = name
        self.publication_name: str = publication_name
        self.release_date: date = release_date
        self.status: BookStatus = status
        self.section: Section = section
        self.reserved_by: Member = reserved_by
        self.authors: str = authors
        self.translators: str = translators

    @classmethod
    def search(cls, book_id: int = None, 
               name: str = None, 
               authors: str = None, 
               translators: str = None,
               publication_name: str = None, 
               release_date: date = None, 
               status: BookStatus = None, 
               section_name: str = None) -> list['Book']:
        query = "SELECT b.book_id, b.name, b.authors, b.translators, b.publication_name, b.release_date, b.status, s.section_id, s.name "
        query += " FROM book AS b "
        query += " INNER JOIN section AS s ON b.section_id = s.section_id "
        conditions = list()
        values = list()

        if book_id is not None:
            conditions.append(" b.book_id = ? ")
            values.append(book_id)
        if name is not None:
            conditions.append(" b.name LIKE ? ")
            values.append(f"%{name}%")
        if authors is not None:
            conditions.append(" b.authors LIKE ? ")
            values.append(f"%{authors}%")
        if translators is not None:
            conditions.append(" b.translators LIKE ? ")
            values.append(f"%{translators}%")
        if publication_name is not None:
            conditions.append(" b.publication_name LIKE ? ")
            values.append(f"%{publication_name}%")
        if release_date is not None:
            conditions.append(" b.release_date = '?' ")
            values.append(release_date.isoformat())
        if status is not None:
            conditions.append(" b.status = ? ")
            values.append(status.value)
        if section_name is not None:
            conditions.append(" s.name = ? ")
            values.append(section_name)

        if len(conditions) > 0:
            query += " WHERE " + " AND ".join(conditions)

        cursor = DatabaseManager.get_cursor()
        cursor.execute(query, values)

        books = list()
        for item in cursor:
            books.append(Book(int(item[0]), item[1], item[2], item[3], item[4], date.fromisoformat(item[5]), BookStatus.set(item[6]), Section(int(item[7]), item[8])))
        return books

        # TODO Remove
        # return [Book(1, "کتاب1", "مهر", date(2008,12,24), BookStatus.Available, Section(1, "رمان"), None, "علیرضا محمدی", None),
        #         Book(2, "کتاب2", "مهر", date(2008,12,24), BookStatus.Loaned, Section(1, "رمان"), None, "علیرضا محمدی", None),
        #         Book(3, "کتاب3", "مهر", date(2008,12,24), BookStatus.Reserved, Section(1, "رمان"), None, "علیرضا محمدی", None)]

    @classmethod
    def add_book(cls, name: str, authors: str, translators: str = None, publication_name: str = None, release_date: date = None, section_id: int = None):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            INSERT INTO book (name, authors, translators, publication_name, release_date, status, section_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, name, authors, translators, publication_name, release_date.isoformat(), BookStatus.Available.value, section_id)
        cursor.commit()
    
    @classmethod
    def delete_books(cls, book_id_list: list[int]):
        cursor = DatabaseManager.get_cursor()
        for book_id in book_id_list:
            cursor.execute("""DELETE FROM book WHERE book_id = ?""", book_id)
            cursor.commit()
    
    @classmethod
    def delete_old_books(cls):
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            WITH book_view (book_id, book_name, loan_count) AS (
                SELECT b.book_id, b.name, ISNULL(COUNT(l.loan_id), 0) as loan_count
                FROM book AS b
                LEFT JOIN loan AS l ON b.book_id = l.book_id
                WHERE (l.borrow_date IS NULL OR DATEDIFF(year, l.borrow_date, GETDATE()) < 1) AND DATEDIFF(year, b.release_date, GETDATE()) > 15
                GROUP BY b.book_id, b.name
            )
            DELETE FROM book
            WHERE book_id IN (
                SELECT book_id FROM book_view
                WHERE loan_count < 5
            )
        """)
        cursor.commit()
