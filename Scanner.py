from SymbolTable import SymbolTable
import re
from enum import Enum
from FiniteAutomata import FiniteAutomata

class ConstantType(Enum):
    NUMBER = 0
    CHAR = 1
    STRING = 2
    NOTHING = 3


class PifElement(Enum):
    CONSTANT = 'constant'
    IDENTIFIER = 'identifier'


class Scanner:
    def __init__(self, file_string):
        self._file = file_string
        self._symbolTable = SymbolTable()
        self._programInternalForm = []
        self._tokens = ['+', '-', '*', '/', '%', '<>', '<<', '>>', '!=', '<-', '<=', '>=', 'zoo', 'cat', 'cow', 'dog',
                        'wolf', 'owl', 'penguin', 'cheetah', 'bee', 'wasp', '(', ')', '{', '}', '[', ']', ';', '>', '<']
        self._operators = ['+', '-', '*', '/', '%', '<>', '<<', '>>', '!=', '<-', '<=', '>=']
        self._fa_integer = FiniteAutomata('integer_fa.in')
        self._fa_identifier = FiniteAutomata('identifier_fa.in')
        try:
            self.scan()
            print("lexically correct")
        except ValueError as err:
            print(err)

    def scan(self):
        elements = re.split('[\n]', self._file)
        elements = [el for el in elements if el != '' and el != ' ']

        for element in elements:
            tokens = self.detect_tokens(element)
            for token in tokens:
                if token in self._tokens:
                    self.gen_pif(token, 0)
                else:
                    if self.detect_identifier(token):
                        self.gen_pif(PifElement.IDENTIFIER.value, self._symbolTable.add(token))
                    else:
                        constant_type = self.detect_constant(token)
                        if constant_type != ConstantType.NOTHING:
                            if constant_type == ConstantType.NUMBER:
                                self.gen_pif(PifElement.CONSTANT.value, self._symbolTable.add(int(token)))
                            elif constant_type == ConstantType.CHAR:
                                self.gen_pif(PifElement.CONSTANT.value, self._symbolTable.add(token))
                            else:
                                self.gen_pif(PifElement.CONSTANT.value, self._symbolTable.add(token))
                        else:
                            raise ValueError('Lexical Error on line ' + str(elements.index(element)) + ' at token ' + token)
        print(self._symbolTable)
        print(self._programInternalForm)
        self.write_files(self._symbolTable, self._programInternalForm)

    def write_files(self, symbol_table, pif):
        with open('PIF.out', 'w') as file:
            file.write(str(pif))
        with open('ST.out', 'w') as file:
            file.write(str(symbol_table))

    def detect_tokens(self, string):
        line_data = re.split('("[^a-zA-Z0-9\"\']")|([^a-zA-Z0-9\"\'])', string)
        elements = [el for el in line_data if el is not None and el != '' and el != ' ']
        n = len(elements) - 1
        for i in range(n):
            if i > n:
                break
            if elements[i] == '<':
                if elements[i + 1] in ['>', '=', '<', '-']:
                    elements[i] += elements[i + 1]
                    del elements[i + 1]
                    n -= 1
                    continue

            if elements[i] == '>':
                if elements[i + 1] in ['>', '=', '<']:
                    elements[i] += elements[i + 1]
                    del elements[i + 1]
                    n -= 1
                    continue

            if elements[i] == '!':
                elements[i] += elements[i + 1]
                del elements[i + 1]
                n -= 1
                continue
            if elements[i] == '+' or elements[i] == '-':
                if i == 0 or elements[i - 1] in self._operators:
                    elements[i + 1] = elements[i] + elements[i + 1]
                    del elements[i]
                    n -= 1
                    continue
        return elements

    def detect_identifier(self, string):
        # match = re.match('^[a-zA-Z][a-zA-Z0-9_]*$', string)
        # return match is not None
        return self._fa_identifier.verify(string)

    def detect_constant(self, string):
        match_string = re.match('^\"[a-zA-Z0-9-_ ]+\"$', string)
        if match_string is None:
            match_char = re.match('^\'[a-zA-Z0-9\-_ ]\'$', string)
            if match_char is None:
                # match_number = re.match('^(\+|-)?[1-9][0-9]*$|^0$', string)
                # if match_number is None:
                if not self._fa_integer.verify(string):
                    return ConstantType.NOTHING
                return ConstantType.NUMBER
            return ConstantType.CHAR
        return ConstantType.STRING



    def gen_pif(self, element, value):
        self._programInternalForm.append((element, value))

