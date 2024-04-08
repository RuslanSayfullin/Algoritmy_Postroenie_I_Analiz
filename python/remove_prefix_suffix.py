text = "Hello, World"
prefix = "Hello, "
suffix = "World"

# Используем .removeprefix() для удаления префикса
result = text.removeprefix(prefix)
print(result)

# Используем .removesuffix(suffix)
result = text.removesuffix(suffix)
print(result)

# Если строка не начинается с указанного префикса, суффикса  ничего не изменит
result = text.removeprefix("Hi, ")
print(result)

result = text.removesuffix(", Everyone")
print(result)
