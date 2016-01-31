#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, words
from pygments.token import *


class GrepLexer(RegexLexer):
    """
    Lexer for Structured Function Language.
    """
    name = 'wiki'
    tokens = {
            'root': [
                (r'\s+', Text),
                (r'/\*', Comment.Multiline),
                (words((
                    'SEARCH', 'SETREGEX', 'EXIT', 'QUIT', 'HELP',
                    'GETLABELS', 'GETREGEX', 'GETPATH',  'CLEAR', 'SETLABELS',

                    'search', 'setregex', 'exit', 'quit', 'help',
                    'getlabels', 'getregex', 'getpath',  'clear', 'setlabels'
                ),
                    suffix=r'\b'), Keyword)
                ]}
