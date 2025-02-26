import pandas as pd
import os, threading, multiprocessing

class Keeper:
    def __init__(self, path: str = r'./data/backup.csv') -> None:
        self.path = path
        manager = multiprocessing.Manager()
        self.register_queue = manager.Queue()
        self.change_queue = manager.Queue()
        self.process = threading.Thread(target=self.main, daemon=True, name='Keeper')
        self.process.start()
    
    def load(self, separator: str = '|') -> pd.DataFrame:
        if not os.path.exists(self.path):
            return pd.DataFrame({
                'task_id': [0],
                'component': [''],
                'description': [''],
                'task_state': ['']
            }).iloc[0:0]

        else:
            return pd.read_csv(self.path, sep=separator)
    
    def save(self, df: pd.DataFrame, separator: str = '|') -> None:
        df.to_csv(self.path, sep=separator, index=False)
        
    def add_record(self, record: dict) -> None:
        df: pd.DataFrame = self.load()
        df: pd.DataFrame = pd.concat([df, pd.DataFrame(record, index=[None])], ignore_index=True, axis=0)
        self.save(df)
    
    def change_record_state(self, task_id: int, state: str) -> None:
        df: pd.DataFrame = self.load()
        df.loc[df['task_id'] == task_id, 'task_state'] = state
        self.save(df)
        
    def main(self) -> None: 
        while True:
            if not self.change_queue.empty():
                record: tuple = self.change_queue.get()
                self.change_record_state(record[0], record[1])
                
            if not self.register_queue.empty():
                record: dict = self.register_queue.get()
                self.add_record(record)