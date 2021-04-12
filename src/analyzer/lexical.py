import re
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    line: int


def tokenize(code):

    keywords = {'program', 'begin', 'end', 'var',
                'procedure', 'else', 'read', 'write',
                'while', 'if'}

    token_specification = [
        ('REAL', r'\d+(\.\d*)+'),  # re for real number
        ('INTEGER', r'\d+'),  # re for integer number
        ('ID', r'[a-zA-Z][a-zA-Z0-9]*'),  # re for variables name
        ('NEW_LINE', r'\n'),
        ('BOOL_OP', r'[<>\=(<>)(>=)(<=)]'),
        ('ADD_OP', r'[+\-]'),
        ('ASSIGN', r':='),
        ('MUL_OP', r'[*/]'),
        ('OPEN', r'\('),
        ('CLOSE', r'\)'),
        ('TYPING', r':'),
        ('COMMA', r','),
        ('SEMICOLON', r';'),
        ('SKIPP', r'[ \t]+'),
        ('ERROR', r'.')
    ]

    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_count = 0

    list_tokens = []

    for token in re.finditer(token_regex, code):
        type_token = token.lastgroup
        value = token.group()

        if type_token == 'ID' and value in keywords:
            type_token = value.upper()

        elif type_token == 'NEW_LINE':
            line_count += 1
            continue

        elif type_token == 'SKIPP':
            continue

        elif type_token == 'ERROR':
            raise NameError('O nome {} na linha {} é inválidos'.format(value, line_count))

        list_tokens.append(Token(type_token, value, line_count))
    else:
        return list_tokens
