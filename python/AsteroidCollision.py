"""
Нам дан массив asteroids, состоящий из целых чисел, представляющих астероиды в ряд. 
Для каждого астероида абсолютное значение обозначает его размер, а знак - направление движения (положительное - вправо, отрицательное - влево). 
Каждый астероид движется с одинаковой скоростью. Определите состояние астероидов после всех столкновений. 
Если два астероида столкнутся, меньший из них взорвется. Если оба одинакового размера, то взорвутся оба. 
Два астероида, движущиеся в одном направлении, никогда не встретятся.
"""

# Input: asteroids = [1, 6 , -3, 2, -1]
# Output: [1, 6, 2]

def asteroidCollision(asteroids):
    # Используйте стек для отслеживания движущихся вправо астероидов.
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack

if __name__ == "__main__":
    example = asteroidCollision(asteroids = [1, 6 , -3, 2, -1])
    print(example)