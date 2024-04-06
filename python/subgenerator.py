def subgenerator():
    yield 1
    yield 2
    yield 3

def generator():
    yield "Начало"
    yield from subgenerator()
    yield "Конец"

for element in generator():
    print(element)
