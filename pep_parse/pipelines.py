import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DIR_OUTPUT = 'results'
DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)


class PepParsePipeline:
    def __init__(self):
        self.results = defaultdict(int)

    def open_spider(self, spider):
        self.results_dir = BASE_DIR / DIR_OUTPUT
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_dir = self.results_dir / FILE_NAME.format(
            time=TIME_NOW)
        data = [['Статус', 'Количество']]
        for key, val in self.results.items():
            data.append([key, val])
        data.append(['Всего', sum(self.results.values())])
        with open(file_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(data)
