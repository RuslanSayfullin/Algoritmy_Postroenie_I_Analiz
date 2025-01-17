"""
Вам дается несколько журналов, где каждый журнал содержит уникальный идентификатор и временную метку. 
Временная метка - это строка, имеющая следующий формат: Год:Месяц:День:Час:Минута:Секунда, например, 2017:01:01:23:59:59. 
Все домены - десятичные числа с нулевым добавлением. Реализация класса LogSystem: LogSystem() Инициализирует объект LogSystem. void put(int id, string timestamp) 
Сохраняет заданный журнал (id, timestamp) в вашей системе хранения.
int[] retrieve(string start, string end, string granularity) Возвращает идентификаторы журналов, временные метки которых находятся в диапазоне от start до end включительно. 
start и end имеют тот же формат, что и timestamp, а granularity означает, насколько точным должен быть диапазон (т. е. с точностью до дня, минуты и т. д.). 
Например, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", а granularity = "Day" означает, 
что нам нужно найти журналы в диапазоне от 1 января 2017 года до 2 января 2017 года включительно, а час, минуту и секунду для каждой записи журнала можно игнорировать.
"""

"""
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
Output
[null, null, null, null, [3, 2, 1], [2, 1]]
"""

class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> [int]:
        index = {
            'Year': 4,
            'Month': 7,
            'Day': 10,
            'Hour': 13,
            'Minute': 16,
            'Second': 19
        }[granularity]
        
        start = start[:index]
        end = end[:index]
        
        result = []
        for id, timestamp in self.logs:
            if start <= timestamp[:index] <= end:
                result.append(id)
        return result

if __name__ == "__main__":
    example = Solution()
    result = example.retrieve(["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]])
    print(result)