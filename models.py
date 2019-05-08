"""
Save Notebooks to a file
Create and clear
"""


class Note:
    note_id = 0

    # Creating a note
    def __init__(self, content):
        Note.note_id += 1
        self.note_id = Note.note_id
        self.content = content


class Notebook:

    # Creating a notes list
    def __init__(self):
        self.notes = []

    # Creating a note // And update a list
    def new_note(self, content):
        temp = Note(content)
        self.notes.append(temp)

        # Del a note

    def del_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                x = self.notes.index(note)
                self.notes.pop(x)
                break


