from src.Algorithm.Domain.Algorithm import BinaryGrap


class BinaryGapRages(object):

    __rangeNumber: int = None
    __result = None

    def __init__(self, range: int):
        self.__rangeNumber = range

    def run(self):
        gap = BinaryGrap()
        for number in range(self.__rangeNumber):
            gap.setNumber(number)
            yield "number {}: gap {}".format(number, gap.getBinaryGap())