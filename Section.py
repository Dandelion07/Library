from DatabaseManager import DatabaseManager

class Section:
    def __init__(self, section_id, name) -> None:
        self.section_id = section_id
        self.name = name

    @classmethod
    def get_all_sections(cls) -> list['Section']:
        # TODO Uncomment
        # cursor = DatabaseManager.get_cursor()
        # cursor.execute("""
        #     SELECT * FROM section
        # """)
        # sections = list()
        # for s in cursor:
        #     sections.append(Section(s[0], s[1]))
        # return sections

        return [Section(1, "تاریخی"), Section(2, "رمان"), Section(3, "جنایی"), Section(4, "تخیلی"), Section(5, "علمی")]