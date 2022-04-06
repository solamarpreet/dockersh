from prompt_toolkit.completion import Completer, Completion
from commands import completer_commands


class DockershellCompleter(Completer):

    def __init__(self):
        self.original_dict = completer_commands()
        self.root_keys = self.original_dict.keys()
        self.flat_dict = self.flatten(self.original_dict)

    def calculate_completions(self, line, is_word_before):
        current_tokens = line.split()
        word_before_cursor = ''
        if not is_word_before:
            word_before_cursor = current_tokens.pop(-1)
        if not current_tokens:
            return self.root_keys, word_before_cursor
        else:
            current_key = []
            for i in current_tokens:
                if not i[0] == '-':
                    current_key.append(i)
            try:
                return self.flat_dict['.'.join(current_key)], word_before_cursor
            except:
                return [], word_before_cursor
        
    def flatten(self, input_dict, separator='.', prefix=''):
        output_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, dict) and value:
                output_dict[prefix+key] = tuple(value.keys())
                deeper = self.flatten(value, separator, prefix+key+separator)
                output_dict.update({key2: val2 for key2, val2 in deeper.items()})
            # For generating None value endpoints for meta display later uncomment below
            # else:
            #     output_dict[prefix+key] = value
        return output_dict
 
    def get_completions(self, document, complete_event):
        is_word_before_cursor = document._is_word_before_cursor_complete()
        words, word_before_cursor = self.calculate_completions(document.text, is_word_before=is_word_before_cursor)
        for word in words:
            if word.startswith(word_before_cursor):
                yield Completion(word, start_position=-len(word_before_cursor))