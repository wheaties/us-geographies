from itertools import chain
from iops.download import LocalFileDownloader


def _tract_shape_files(year):
    if year < 2010:
        return []  # someone else can figure this stuff out
    elif year == 2010:
        return ['https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_01_tract10.zip']

    states = chain([1, 2, 4, 5, 6],
                   range(8, 14),  # 8-13
                   range(15, 43),  # 15-42
                   range(44, 52),  # 44-51
                   [54, 55, 56, 66, 72, 78])
    for state in states:
        if state < 10:
            state = f'0{state}'
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/TRACT/tl_{year}_{state}_tract.zip'


def download_files(year, root_folder=None, force=False):
    downloader = LocalFileDownloader(root_folder)

    return [downloader(url, year, force) for url in _tract_shape_files(year)]
