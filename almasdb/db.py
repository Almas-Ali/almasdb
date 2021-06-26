import pickle as p
import os


class Database:
    '''Database class.'''

    def __init__(self, db_path=os.path.join(os.getcwd(), 'test')):
        self.db_path = db_path+'.db'

    def create(self):
        '''Creating a database.'''

        default = f'This database located at {self.db_path}'
        try:
            with open(self.db_path, 'wb') as w:
                p.dump(default, w)
            return '[True]'
        except:
            return '[False]'

    def read(self):
        '''Opens a database.'''

        with open(self.db_path, 'rb').read() as w:
            object = p.load(w)
        return object

    def modify(self):
        '''Modify a database.'''

        modifier = open(self.db_path, 'ab')
        file_path = self.db_path
        # modifier = db(self.db_path).read()
        # modifier = p.dump(dic, w)
        return (modifier, file_path)

    def clear(self):
        '''Clear a database.'''

        with open(self.db_path, 'wb') as w:
            p.dump('', w)
        return '[True]'

    def insert(self):
        pass

    def __str__(self):
        return self.db_path

    def __repr__(self):
        return self.db_path

    class Table:
        '''Table for database class.'''

        def __init__(self, name):
            self.name = name

        def __find(list, value):
            '''Finding table location.'''
            i = 0
            for z in list:
                i += 1
                print(z)
                try:
                    y = z.index(value)
                    return (i, y)
                except:
                    pass

        def create(self, db_obj):
            '''To create a new table.'''
            db_obj = str(db_obj)
            code = [self.name, ]
            with open(db_obj, 'r+b') as w:
                # p.dump(exec('%s =[]' % self.name), w)
                p.dump(code, w)
            return '[True]'

        def clear(self):
            '''To clear a table.'''
            pass

        def all(self):
            '''To get all tables in the database.'''

            pass

        def get(self):
            '''To get a spacific row in a table.'''

            pass

        def select(self):
            '''To select a spacific row in a table.'''

            pass

        def insert(self, db_obj, obj):
            '''Insert new data to table.'''
            db_obj = str(db_obj)
            with open(db_obj, 'rb') as ww:
                list = p.load(ww.read())
                location = Database.Table.__find(list, self.name)
                val = list[location[0]]
                print(val)

            with open(db_obj, 'r+b') as w:
                # list = p.load(w)
                # location = Database.Table.__find(list, self.name)
                # val = list[location[0]]
                # print(val)
                p.dump(obj, w)

            return '[True]'

    class Query:
        '''Searching class for database.'''
        pass

        def __init__(self):
            pass

        def count(self):
            '''To count a data in a table.'''
            pass
