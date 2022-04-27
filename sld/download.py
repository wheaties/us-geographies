from collections import namedtuple
from iops.download import download_to_cls, state_divided_paths


def _sldu_shapes(year):
    if year < 2011:
        return []

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/SLDU/tl_{year}_{state}_sldu.zip'


def _sldl_shapes(year):
    if year < 2011:
        return []

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/SLDL/tl_{year}_{state}_sldl.zip'


SLDFiles = namedtuple('SLDFiles', ['sldu', 'sldl'])
download_files = download_to_cls(SLDFiles, _sldu_shapes, _sldl_shapes)
