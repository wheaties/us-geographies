from xlrd import open_workbook


def _sub_none_for_empty(value):
    if isinstance(value, str):
        return value if len(value) else None
    return value


def parse_file(filename, skip_beginning=0, skip_ending=0):
    values = []
    sheet = open_workbook(filename, ragged_rows=True).sheet_by_index(0)
    for indx, row in enumerate(sheet.get_rows()):
        if skip_beginning < indx < sheet.nrows - skip_ending:
            values.append([_sub_none_for_empty(col.value) for col in row])
    print(f'Read {len(values)} records from {filename}')
    return values
