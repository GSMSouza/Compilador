from typing import List

from ..analyzer.lexical import Token


def rule_programa(list_of_tokens: List[Token]):
    if list_of_tokens[0].type == 'PROGRAM':
        list_of_tokens.remove(0)
        if list_of_tokens[0].type == 'IDENT':
            list_of_tokens.remove(0)
            rule_corpo(list_of_tokens)
    else:
        raise SyntaxError('')


def rule_corpo(list_of_tokens: List[Token]):
    pass
