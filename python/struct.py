import struct

# Создаём структуру с двумя элементами: байтом и целым числом
struct_format = "bh"
struct = struct.Struct(struct_format)

# Сохраняем данные в структуре
struct_data = struct.pack(struct_format, 1, 255)

# Извлекает данные из структуры
byte_value, integer_value = struct.unpack(struct_format, struct_data)
print(byte_value, integer_value)
