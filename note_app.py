"""
Notebook that holds strings
we want a menu that can:
Note:
    Add
    Print
    remove
Quit

note a note has an ID
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


class Menu:

    def __init__(self):
        self.notebook = Notebook()

       # TODO: Finish dict
        self.choices = {
            '1': self.show_notes,
            '2': self.add_note,
            '3': self.del_by_id,
            '4': self.quit,
        }

    def display_menu(self):
        print(
            'Notebook Menu:'
            '\n1. Show all notes'
            '\n2. Add note'
            '\n3. Delete note'
            '\n4. Quit'
        )

    def run(self):

        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'\n{choice} is not a valid choice')

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'\n{note.note_id}: {note.content}')

    def add_note(self):
        content = input('Enter a note: ')
        self.notebook.new_note(content)
        print('Added a note!')

    def del_by_id(self):
        n_id = int(input('Enter a note id to delete'))
        self.notebook.del_note(n_id)

    def quit(self):
        exit()


if __name__ == '__main__':
    a = Menu()
    a.run()
