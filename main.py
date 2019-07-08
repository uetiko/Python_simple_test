from src.Braces.Application.Syntax import Braces
from src.Braces.Domain.Syntax import StringStack
from src.Algorithm.Application.Algorithm import BinaryGapRages


input = [
    '{(})([]}',
    '{}()[]',
    '{({}[])}'
]

test = Braces(input, StringStack())

print(test.validate())

algorithm = BinaryGapRages(500)

for item in algorithm.run():
    print(item)