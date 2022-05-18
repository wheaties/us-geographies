from usgeo.iops.download import download_to_cls
from collections import namedtuple


def _mtfcc_file(year):
    if year < 2017:
        return 'https://www2.census.gov/geo/pdfs/reference/mtfccs.pdf'
    else:
        return f'https://www2.census.gov/geo/pdfs/reference/mtfccs{year}.pdf'


def _funcstat_file(*args):
    return 'https://www2.census.gov/geo/pdfs/reference/FunctionalStatusCodes.pdf'


def _class_file(*args):
    return 'https://www2.census.gov/geo/pdfs/reference/ClassCodes.pdf'


def _lsad_file(*args):
    return 'https://www2.census.gov/geo/pdfs/reference/LSADCodes.pdf'


ReferenceFiles = namedtuple('ReferenceFiles', ['mtfcc', 'funcstat', 'class_code', 'lsad'])
download_files = download_to_cls(ReferenceFiles, _mtfcc_file, _funcstat_file, _class_file, _lsad_file)
