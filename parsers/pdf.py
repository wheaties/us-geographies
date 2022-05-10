import pdfplumber


def parse_file(filename):
    output = []
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            output.extend(page.extract_table())
    print(f'columns in tables({ set(len(x) for x in output) })')
    print(f'rows {len(output)}')
    raise Exception('yo')
    return output
