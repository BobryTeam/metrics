import json


class Metrics:
    PROMQL_REQUESTS = lambda target_job: [
        f'sum(rate(node_cpu_seconds_total{{mode!="idle", job="{target_job}"}}[1m]))/ \
        count(rate(node_cpu_seconds_total{{mode!="idle", job="{target_job}"}}[1m]) > bool 0.05)',

        f'1 - ((avg(avg_over_time(node_memory_MemFree_bytes{{job="{target_job}"}}[1m])) + \
        avg(avg_over_time(node_memory_Cached_bytes{{job="{target_job}"}}[1m])) + \
        avg(avg_over_time(node_memory_Buffers_bytes{{job="{target_job}"}}[1m]))) / \
        avg(avg_over_time(node_memory_MemTotal_bytes{{job="{target_job}"}}[1m])))',

        f'avg(rate(node_network_receive_bytes_total{{job="{target_job}"}}[1m])) * 8 / 1024 / 1024',
        f'avg(rate(node_network_transmit_bytes_total{{job="{target_job}"}}[1m])) * 8 / 1024 / 1024', 
    ]

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
                float(data['cpu_load']),
                float(data['ram_load']),
                float(data['net_in_load']),
                float(data['net_out_load']),
            )
        except:
            return super().__init__(
                0, 0, 0, 0
            )