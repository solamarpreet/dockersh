from prompt_toolkit.completion import Completer, Completion
from commands import completer_commands

class DockershellCompleter(Completer):

    def __init__(self):
        self.current_dict = completer_commands()
        self.prev_tokens = []

    def calculate_completions(self, line, is_word_before):
        word_before_cursor = ''
        key_tokens = []
        current_tokens = line.split()
        if not is_word_before:
            word_before_cursor = current_tokens.pop(-1)
        for i in current_tokens:
            if not i[0] == '-':
                key_tokens.append(i)
        if key_tokens == self.prev_tokens:
            return self.current_dict.keys(), word_before_cursor
        self.prev_tokens = []
        self.current_dict = completer_commands()
        while key_tokens:
            key = key_tokens.pop(0)
            self.prev_tokens.append(key)
            val = self.current_dict.get(key)
            if val:
                self.current_dict = val
            else:
                self.current_dict = {}
        return self.current_dict.keys(), word_before_cursor


    def get_completions(self, document, complete_event):
        is_word_before_cursor = document._is_word_before_cursor_complete()
        words, word_before_cursor = self.calculate_completions(document.text, is_word_before=is_word_before_cursor)
        for word in words:
            if word.startswith(word_before_cursor):
                yield Completion(word, start_position=-len(word_before_cursor))