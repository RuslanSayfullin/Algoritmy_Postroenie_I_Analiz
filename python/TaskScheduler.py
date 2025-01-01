# Вам дан массив задач процессора, каждая из которых представлена буквами от A до Z, и время охлаждения, n. 
# Каждый цикл или интервал позволяет завершить одну задачу. 
# Задачи могут быть выполнены в любом порядке, но есть ограничение: одинаковые задачи должны быть разделены не менее чем n интервалами из-за времени охлаждения.
# Верните минимальное количество интервалов, необходимое для выполнения всех задач.


"""
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
"""

from collections import Counter

def leastInterval(tasks, n):
    task_counts = Counter(tasks)        # подчитываем количество задач
    print("task_counts: ", task_counts)
    max_freq = max(task_counts.values)  # находим max. кол-во вхождений
    print("max_freq: ", max_freq)
    # count_max_freq - количество задач, имеющих max_freq.
    count_max_freq = list(task_counts.values()).count(max.max_freq)
    print("count_max_freq: ", count_max_freq)

    return max(len(tasks), (max_freg - 1) * (n + 1) +  count_max_freq)  # количество интервалов, необходимых для задач с maxFreq

if __name__ == "__main__":
    result = leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
    print(result)