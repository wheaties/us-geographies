import psycopg2


def parse_connection(dbname=None, dbhost=None, dbport=None, dbuser=None, dbpass=None):
    dsn = {}

    def update(name, value):
        if value:
            dsn[name] = value

    update('dbname', dbname)
    update('host', dbhost)
    update('port', dbport)
    update('user', dbuser)
    update('password', dbpass)
    update('dbname', dbname)

    return dsn


def connect_db(dbname=None, dbhost=None, dbport=None, dbuser=None, dbpass=None):
    try:
        conn = psycopg2.connect(dbname)
    except psycopg2.ProgrammingError:
        conn = psycopg2.connect(**parse_connection(dbname, dbhost, dbport, dbuser, dbpass))

    with conn.cursor() as cursor:
        cursor.execute('SELECT 1')
    return conn


# This screams to just use SqlAlchemy
class RawDataTable:
    def __init__(self, name, group=None):
        self.__name = name
        self.__group = group or name.split('_')[0]
        self.columns = []

    def name(self, year):
        return f'{self.__name}_raw_{year}'

    @property
    def group(self):
        return self.__group.upper()

    def setup(self, connection, year, force=False):
        name = self.name(year)
        with connection.cursor() as cursor:
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} ({",".join(self.columns)})')
            if force:
                cursor.execute(f'''DELETE FROM {name}''')

    def populate(self, connection, year, rows):
        with connection.cursor() as cursor:
            stmt = f'INSERT INTO {self.name(year)} VALUES({",".join("%s" for _ in self.columns)})'
            for row in rows:
                cursor.execute(stmt, row)


class ShapeDataTable:
    def __init__(self, name, group=None):
        self.__name = name
        self.__group = group or name.split('_')[0]
        self.columns = []

    def name(self, year):
        return f'{self.__name}_shapes_{year}'

    @property
    def group(self):
        return self.__group.upper()

    def setup(self, connection, year, force=False):
        name = self.name(year)
        with connection.cursor() as cursor:
            columns = ','.join(self.columns) + ',geom GEOMETRY'
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} ({columns})')
            if force:
                cursor.execute(f'''DELETE FROM {name}''')

    def populate(self, connection, year, rows):
        with connection.cursor() as cursor:
            values_stmt = ','.join('%s' for _ in self.columns) + ', ST_GeomFromGeoJSON(%s)'
            stmt = f'INSERT INTO {self.name(year)} VALUES({values_stmt})'
            for row in rows:
                cursor.execute(stmt, row)
