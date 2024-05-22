import json


class Metrics:
    def __init__(self, cpu_load: float, ram_load: float, avg_received_bytes: int, avg_transmitted_bytes: int):
        '''
        Инициализация класса
        `cpu_load` - общий процент загруженности ЦП за 1 минуту
        `ram_load` - общий процент загруженности ОЗУ за 1 минуту
        `avg_received_bytes` - среднее по репликам количество байтов считанных за 5 минут
        `avg_transmitted_bytes` - среднее по репликам количество байтов отправленных за 5 минут
        '''

        self.cpu_load = cpu_load
        self.ram_load = ram_load
        self.avg_received_bytes = avg_received_bytes
        self.avg_transmitted_bytes = avg_transmitted_bytes

    def __str__(self) -> str:
        '''
        Сериализует метрики в строку
        '''

        data = {
            'cpu_load': self.cpu_load,
            'ram_load': self.ram_load,
            'avg_received_bytes': self.avg_received_bytes,
            'avg_transmitted_bytes': self.avg_transmitted_bytes
        }

        return json.dumps(data)

class MetricsFromStr(Metrics):
    def __init__(self, string_data: str):
        '''
        Инициализация класса из строки
        '''

        try:
            data = json.loads(string_data)

            return super().__init__(
                data['cpu_load'],
                data['ram_load'],
                data['avg_received_bytes'],
                data['avg_transmitted_bytes'],
            )
        except:
            return super().__init__(
                0, 0, 0, 0
            )
