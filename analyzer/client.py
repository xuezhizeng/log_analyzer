from __future__ import unicode_literals
from prompt_toolkit import prompt
from completer import CustomCompleter
from prompt_toolkit.history import InMemoryHistory
from pygments.style import Style
from pygments.token import Token
from GrepLexer import GrepLexer
from CommandManager import CommandManager, CONFIG_PATH
from pygments.styles.default import DefaultStyle
import os

grep_completer = CustomCompleter([
    'search', 'setregex', 'exit', 'quit', 'help',
    'getlabels', 'getregex', 'getpath',  'clear', 'setlabels'],
    meta_dict={
        'search': 'used to get search keyword in logs',\
        'set regex': 'used to set regex ',\
        }, ignore_case=True, only_directories=False, expanduser=True)


class DocumentStyle(Style):
        styles = {
                Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
                Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
                Token.Menu.Completions.ProgressButton: 'bg:#003333',
                Token.Menu.Completions.ProgressBar: 'bg:#00aaaa',
                }
        styles.update(DefaultStyle.styles)


def main():
    history = InMemoryHistory()
    manager = CommandManager()

    while True:
        try:
            input = prompt('>>> ', lexer=GrepLexer,
                           completer=grep_completer,
                           style=DocumentStyle,
                           history=history,
                           display_completions_in_columns=True)

            if not input \
                    or input.lower() == 'quit'\
                    or input.lower() == 'exit':
                print 'See you.'
                break
            elif os.path.exists(input):
                manager.setpath(input)
            else:
                func, args = input.split()[0].lower(), \
                             input.split()[1:]
                try:
                    getattr(manager, func)(args)
                except AttributeError as error:
                    print 'No function: %s' % func

        except KeyboardInterrupt as stop:
            print 'See you.'
            break


if __name__ == '__main__':
    main()
