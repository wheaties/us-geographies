from itertools import chain
from iops.download import LocalFileDownloader


# issues with 2013, 2014
def _puma_shape_files(year):
    if year < 2012:
        return []

    states = chain([1, 2, 4, 5, 6],
                   range(8, 14),  # 8-13
                   range(15, 43),  # 15-42
                   range(44, 52),  # 44-51
                   [54, 55, 56, 66, 72, 78])
    for state in states:
        if state < 10:
            state = f'0{state}'
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/PUMA/tl_{year}_{state}_puma10.zip'


def download_files(year, root_folder=None):
    downloader = LocalFileDownloader(root_folder)

    return [downloader(url, year) for url in _puma_shape_files(year)]
