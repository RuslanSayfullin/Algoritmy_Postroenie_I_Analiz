# Имеется n различных онлайн-курсов, пронумерованных от 1 до n.
# Вам дан массив courses, где courses[i] = [durationi, lastDayi] указывает, что i-й курс должен быть пройден непрерывно в течениеi дней и должен быть закончен до или в lastDayi. 
# Вы начинаете в 1-й день и не можете проходить два или более курсов одновременно. Верните максимальное количество курсов, которые вы можете пройти.

"""
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
"""

import heapq

def scheduleCoutse(courses):
    # Отсортируйте курсы по их конечным датам (lastDay). 
    # Это позволяет проходить курсы как можно ближе к их крайним срокам.
    courses.sort(key=lambda x: x[1])
    # Используйте приоритетную очередь (max-heap) 
    # для отслеживания продолжительности пройденных курсов.
    total_time = 0
    max_heap = []

    # Для каждого курса: Добавьте его продолжительность 
    # в приоритетную очередь и обновите общее время 
    # прохождения курсов. 
    # Если общее время превышает крайний срок текущего курса, 
    # удалите самый длительный курс из очереди и 
    # скорректируйте общее время.
    for duration, last_day in courses:
        heapq.heappush(max_heap, -duration)
        total_time += duration

        if total_time > last_day:
            total_time += heapq.heappop(max_heap)

    return len(max_heap)


if __name__ == "__main__":
    result = scheduleCoutse(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]])
    print(result)