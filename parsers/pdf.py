import pdfplumber


def parse_file(filename):
    output = []
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            for row in table:
                output.append([x for x in row if x is not None and x != ''])
    if len(set(len(x) for x in output)) > 1:
        raise Exception(f'Bad parse: {filename} contains incongruent columns.')
    return output
