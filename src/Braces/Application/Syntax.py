from src.Braces.Domain.Syntax import StringStack


class Braces(object):
    __input: list = None
    __validatior: StringStack = None
    __result: str = None

    def __init__(self, intput: list, validation: StringStack):
        self.__input = intput
        self.__validatior = validation
        self.__result = '';

    def __check(self, item: str):
        self.__validatior.setExpresion(item)

        if self.__validatior.validation():
            return "{}: {}\n".format(item, 1)
        else:
            return "{}: {}\n".format(item, 0)

    def __writeResult(self):
        for item in self.__input:
            self.__result += self.__check(item)

    def validate(self):
        self.__writeResult()

        return self.__result