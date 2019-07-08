class StringStack(object):
    __brackets: list = None
    __expresion: str = None

    def __init__(self):
        self.__brackets = ['()', '{}', '[]']

    def setExpresion(self, expresion: str):
        self.__expresion = expresion

    def validation(self):
        while any(term in self.__expresion for term in self.__brackets):
            for term in self.__brackets:
                self.__expresion = self.__expresion.replace(term, '')

        return not self.__expresion
