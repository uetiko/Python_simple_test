from src.Braces.Application.Syntax import Braces
from src.Braces.Domain.Syntax import StringStack


input = [
    '{(})([]}',
    '{}()[]',
    '{({}[])}'
]

test = Braces(input, StringStack())

print(test.validate())