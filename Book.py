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
        if status == BookStatus.Available:
            return BookStatus.Available
        elif  status == BookStatus.Loaned:
            return BookStatus.Loaned
        elif status == BookStatus.Reserved:
            return BookStatus.Reserved

class Book:
    def __init__(self, book_id: int = None,
                 name: str = None, 
                 publication_name: str = None, 
                 release_date: date = None, 
                 status: BookStatus = BookStatus.Available, 
                 section: Section = None, 
                 reserved_by: Member = None,
                 authors: str = None,
                 translators: str = None) -> None:
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
    def get_book_from_section(cls, section_id: int = 0) -> list['Book']:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # query = """
        #             SELECT b.book_id, b.name, b.publication_name, b.release_date, b.status, s.section_id, s.name
        #                 STRING_AGG(CONCAT(a.first_name, ' ', a.last_name), ', ') AS authors,
        #                 STRING_AGG(CONCAT(t.first_name, ' ', t.last_name), ', ') AS translators
        #             FROM book AS b"""
        # if section_id != 0:
        #     query += """\nWHERE b.section_id = ?\n"""
        # query += """
        #     INNER JOIN section AS s ON b.section_id = s.section_id
        #     INNER JOIN book_authors AS ba ON b.book_id = ba.book_id
        #     INNER JOIN author AS a ON ba.author_id = a.author_id
        #     INNER JOIN book_translators AS bt ON b.book_id = bt.book_id
        #     INNER JOIN translator AS t ON bt.translator_id = t.translator_id
        #     GROUP BY b.book_id, b.name, b.piblication_name, b.release_date
        # """
        # cursor.execute(query, section_id)
        # books = list()
        # for b in cursor:
        #     books.append(Book(
        #         b[0], b[1], b[2], date(b[3]), b[4], Section(b[5], b[6]), None, b[7], b[8]
        #     ))
        # return books

        return list()

    @classmethod
    def search(cls, book_id: int = None, 
               name: str = None, 
               publication_name: str = None, 
               release_date: date = None, 
               status: BookStatus = None, 
               section_name: str = None, 
               authors: str = None, 
               translators: str = None) -> list['Book']:
        # TODO Uncomment
        # query = """SELECT b.book_id, b.name, b.publication_name, b.release_date, b.status, s.section_id, s.name
        #             STRING_AGG(CONCAT(a.first_name, ' ', a.last_name), ', ') AS authors,
        #             STRING_AGG(CONCAT(t.first_name, ' ', t.last_name), ', ') AS translators
        #         FROM book AS b
        #         INNER JOIN section AS s ON b.section_id = s.section_id
        #         INNER JOIN book_authors AS ba ON b.book_id = ba.book_id
        #         INNER JOIN author AS a ON ba.author_id = a.author_id
        #         INNER JOIN book_translators AS bt ON b.book_id = bt.book_id
        #         INNER JOIN translator AS t ON bt.translator_id = t.translator_id\n"""
        # conditions = list()
        # values = list()

        # if book_id is not None:
        #     conditions.append("b.book_id = ?")
        #     values.append(book_id)
        # if name is not None:
        #     conditions.append("b.name LIKE N'%?%'")
        #     values.append(name)
        # if publication_name is not None:
        #     conditions.append("b.publication_name LIKE N'%?%'")
        #     values.append(publication_name)
        # if release_date is not None:
        #     conditions.append("b.release_date = '?'")
        #     values.append(release_date)
        # if status is not None:
        #     conditions.append("b.status = N'?'")
        #     values.append(status.value)
        # if section_name is not None:
        #     conditions.append("s.name = N'?'")
        #     values.append(section_name)
        # if authors is not None:
        #     conditions.append("b.authors LIKE N'%?%'")
        #     values.append(authors)
        # if translators is not None:
        #     conditions.append("b.translators LIKE N'%?%'")
        #     values.append(translators)

        # if len(conditions) > 0:
        #     query += "WHERE " + "\n".join(conditions) + "\n"
        
        # query += "GROUP BY b.book_id, b.name, b.piblication_name, b.release_date, b.status, s.name"
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute(query, values)

        # books = list()
        # for item in cursor:
        #     books.append(Book(item[0], item[1], item[2], date.fromisoformat(item[3]), BookStatus.set(item[4]), Section(item[5], item[6]), None, item[7], item[8]))
        # return books

        return [Book(1, "کتاب1", "مهر", date(2008,12,24), BookStatus.Available, Section(1, "رمان"), None, "علیرضا محمدی", None),
                Book(2, "کتاب2", "مهر", date(2008,12,24), BookStatus.Loaned, Section(1, "رمان"), None, "علیرضا محمدی", None),
                Book(3, "کتاب3", "مهر", date(2008,12,24), BookStatus.Reserved, Section(1, "رمان"), None, "علیرضا محمدی", None)]
