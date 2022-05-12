from itertools import pairwise
import pdfplumber


def parse_file(filename, skip_beginning=0, skip_header=0):
    tables = _read_file(filename)
    tables = list(_skip_rows(tables, skip_beginning, skip_header))
    empty_columns = _index_empty_columns(tables)
    _join_tables(tables, empty_columns)
    output = []
    for table in tables:
        for row in table:
            values = [col for idx, col in enumerate(row) if idx not in empty_columns]
            output.append(values)
    if len(set(len(x) for x in output)) > 1:
        raise Exception(f'Bad parse: {filename} contains incongruent columns.')
    return output


def _read_file(filename):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            yield page.extract_table()


def _skip_rows(tables, skip=0, skip_header=0):
    for table in tables:
        size = len(table)
        if skip > size-skip_header:
            skip -= (size-skip_header)
        else:
            yield table[skip+skip_header:size]
            skip = 0


def _index_empty_columns(tables):
    columns = len(tables[0][0])
    matrix = {}
    for idx in range(columns):
        matrix[idx] = False
        for table in tables:
            matrix[idx] |= any(row[idx] for row in table)
    return [idx for idx in range(columns) if not matrix[idx]]


def _join_tables(tables, empty_columns):
    def illegal_empty_columns(row):
        illegal = []
        for idx,value in enumerate(row):
            if not value and idx not in empty_columns:
                illegal.append(idx)
        return illegal

    for t1, t2 in pairwise(tables):
        row2 = t2[0]
        illegal_columns = illegal_empty_columns(row2)
        if len(illegal_columns):
            row1 = t1[-1]
            for idx, col in enumerate(row1):
                if row2[idx]:
                    row1[idx] = (col or '') + (row2[idx] or '')
            t2.pop(0)
