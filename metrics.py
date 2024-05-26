import json


class Metrics:
    def __init__(self, cpu_load: float, ram_load: float, net_in_load: float, net_out_load: float):
        '''
        Инициализация класса
        `cpu_load` - значение от 0 до 1 - процент загруженности ЦП за 1 минуту
        `ram_load` - значение от 0 до 1 - процент загруженности ОЗУ за 1 минуту
        `net_in_load` - значение >0 - средняя скорость входящего трафика в мбит/сек
        `net_out_load` - значение >0 - средняя скорость исходящего трафика в мбит/сек
        '''

        self.cpu_load = cpu_load
        self.ram_load = ram_load
        self.net_in_load = net_in_load
        self.net_out_load = net_out_load

    def __str__(self) -> str:
        '''
        Сериализует метрики в строку
        '''

        data = {
            'cpu_load': self.cpu_load,
            'ram_load': self.ram_load,
            'net_in_load': self.net_in_load,
            'net_out_load': self.net_out_load
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
                data['net_in_load'],
                data['net_out_load'],
            )
        except:
            return super().__init__(
                0, 0, 0, 0
            )
