import pickle as p
import os


class Database:
    '''Database class.'''

    def __init__(self, db_path=os.path.join(os.getcwd(), 'test')):
        self.db_path = db_path+'.db'

    def create(self):
        '''Creating a database.'''
        default = f'This is a {self.db_path}'
        try:
            with open(self.db_path, 'wb') as w:
                p.dump(default, w)
            return '[True] database created'
        except:
            return f'[False] failed to create database in {self.db_path}'

    def read(self):
        '''Opens a database.'''
        with open(self.db_path, 'rb') as w:
            object = p.load(w)
        return object

    def modify(self, dic):
        '''Modify a database.'''
        with open(self.db_path, 'ab') as w:
            # modifier = db(self.db_path).read()
            modifier = p.dump(dic, w)
        return modifier

    def clear(self):
        '''Clear a database.'''
        with open(self.db_path, 'wb') as w:
            p.dump('', w)
        return '[True]'

    def insert(self):
        pass

    def __str__(self):
        return 'Database class.'

