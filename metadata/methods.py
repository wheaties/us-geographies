import contextlib
import hashlib


def create_metadata_table(connection):
    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS file_metadata (
            file_name TEXT NOT NULL,
            dataset TEXT NOT NULL,
            file_checksum TEXT NOT NULL,
            created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            UNIQUE(file_checksum, dataset))''')


setup = create_metadata_table


def exists_in_metadata_table(connection, dataset, md5):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT COUNT(1) 
            FROM file_metadata
            WHERE dataset=%s AND file_checksum=%s''',
                       (dataset, md5))
        return sum(res[0] for res in cursor) > 0


def md5_checksum(filepath):
    with filepath.open('rb') as f:
        return hashlib.md5(f.read()).hexdigest()


@contextlib.contextmanager
def file_metadata(connection, filepath, dataset, force=False):
    md5 = md5_checksum(filepath)
    create_metadata_table(connection) #TODO: this should be done once for all, not every time
    flag = exists_in_metadata_table(connection, dataset, md5)
    try:
        yield flag
    finally:
        if force or not flag: #what if a "dry run?" I'd have too many booleans.
            record_file(connection, filepath, dataset, md5)


def record_file(connection, filepath, dataset, md5):
    with connection.cursor() as cursor:
        cursor.execute(
            '''INSERT INTO file_metadata (file_name, dataset, file_checksum)
            VALUES (%s, %s, %s)
            ON CONFLICT (file_checksum, dataset)
            DO UPDATE SET file_name=%s, updated=now()''',
            (filepath.name, dataset, md5, filepath.name))
