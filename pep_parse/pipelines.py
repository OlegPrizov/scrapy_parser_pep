import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'


class PepParsePipeline:

    def __init__(self) -> None:
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / FILE_NAME.format(
            time=dt.datetime.now().strftime(DT_FORMAT))
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(
                [('Статус', 'Количество'),
                *self.results.items(),
                ('Всего', sum(self.results.values()))]
            )
