import models as models
from notebook_writer import NotebookWriter,  Testing


class Menu:

    def __init__(self):
        self.notebook = models.Notebook()
        self.writer = NotebookWriter()

        # TODO: Finish Dict
        self.choices = {
            "1": self.show_notes,
            "2": self.add_note,
            "3": self.del_by_id,
            "4": self.quit
        }

    def save_notes(self):
        self.writer.write_notebook(self.notebook.notes)


    def clear_notes(self):
        self.writer.clear_text_file()

    def display_menu(self):
        print(
            "Notebook Menu:"
            "\n1. Show all notes"
            "\n2. Add note"
            "\n3. Delete note"
            "\n4. Save notes"
            "\n5. Clear notes file"
            "\n6. Quit"
        )

    def run(self):

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"\n{choice} is not a valid choice")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"\n{note.note_id}: {note.content}")

    def add_note(self):
        content = input("Enter a note: ")
        self.notebook.new_note(content)
        print("Added a note!")

    def del_by_id(self):
        n_id = int(input("Enter a note id to delete: "))
        self.notebook.del_note(n_id)

    def quit(self):
        exit()


if __name__ == "__main__":
    a = Menu()
    a.run()
