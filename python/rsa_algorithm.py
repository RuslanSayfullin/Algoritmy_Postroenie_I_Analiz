import random
import math

def generate_keypair(p, q):
    # Шаг 1: Выбор двух простых чисел p и q
    # Шаг 2: Вычисление n = p * q
    n = p * q

    # Шаг 3: Вычисление функции Эйлера (phi)
    phi = (p - 1) * (q - 1)

    # Шаг 4: Выбор целого числа e, такого что 1 < e < phi и e взаимно просто с phi
    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Шаг 5: Вычисление числа d, такого что (d * e) % phi = 1
    d = pow(e, -1, phi)

    # Возвращение открытого и закрытого ключей
    return ((e, n), (d, n))

def encrypt(public_key, message):
    # Распаковка открытого ключа
    e, n = public_key

    # Шифрование сообщения с помощью открытого ключа
    encrypted_message = [pow(ord(char), e, n) for char in message]

    # Возвращение зашифрованного сообщения
    return encrypted_message

def decrypt(private_key, encrypted_message):
    # Распаковка закрытого ключа
    d, n = private_key

    # Расшифровка сообщения с помощью закрытого ключа
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]

    # Объединение расшифрованных символов в строку
    return ''.join(decrypted_message)

# Пример использования
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

message = "Hello, RSA!"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Исходное сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
