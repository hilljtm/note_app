

"""
Save Notebooks to a file
Add notebooks and clear the file
"""


class NotebookWriter:

    def write_notebook(self, notes):
        self.clear_text_file()
        with open('notes.txt', 'a') as f:
            temp = ''
            for note in notes:
                temp += f'{note.note_id},{note.content}\n'
            f.write(temp)


    def clear_text_file(self):
         open('notes.txt', 'w').close()

class Testing:
    def __init__(self, x):
        self.x = x
