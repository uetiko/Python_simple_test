class BinaryGrap(object):
    __number: int = None

    def setNumber(self, number: int):
        self.__number = number

    def getBinaryGap(self):
        return len(
            max(
                format(self.__number, 'b').strip('0').split('1')
            )
        )