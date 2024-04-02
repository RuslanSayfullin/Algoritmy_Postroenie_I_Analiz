import cmath

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Пример использования
x = [0, 1, 2, 3]  # Входной сигнал
X = fft(x)        # Применение быстрого преобразования Фурье

print("Входной сигнал:", x)
print("FFT:", X)
