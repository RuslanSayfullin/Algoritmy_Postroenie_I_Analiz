"""
Задав массив целых чисел temperature, представляющих дневные температуры, верните массив answer, такой, 
что answer[i] - это количество дней, которые нужно подождать после i-го дня, чтобы температура стала теплее. 
Если в будущем не существует дня, для которого это возможно, сохраните answer[i] == 0.
"""

# Input: T = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(T):
    n = len(T)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    return answer

if __name__ == "__main__":
    example = dailyTemperatures(T = [73,74,75,71,69,72,76,73])
    print(example)