import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DIR_OUTPUT = 'results'
DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}
        self.results_dir = BASE_DIR / DIR_OUTPUT
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        file_dir = self.results_dir / FILE_NAME.format(
            time=TIME_NOW)
        with open(file_dir, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, val in self.results.items():
                f.write(f'{key},{val}\n')
            f.write(f'Total,{sum(self.results.values())}\n')
