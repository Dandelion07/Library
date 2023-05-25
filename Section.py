from DatabaseManager import DatabaseManager

class Section:
    def __init__(self, section_id, name) -> None:
        self.section_id = section_id
        self.name = name

    @classmethod
    def get_all_sections(cls) -> list['Section']:
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            SELECT * FROM section
        """)
        sections = list()
        for s in cursor:
            sections.append(Section(int(s[0]), s[1]))
        return sections
