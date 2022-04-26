from iops.download import LocalFileDownloader, state_divided_paths


def _tract_shape_files(year):
    if year < 2010:
        return []  # someone else can figure this stuff out
    elif year == 2010:
        return ['https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_01_tract10.zip']

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/TRACT/tl_{year}_{state}_tract.zip'


def download_files(year, root_folder=None, force=False):
    downloader = LocalFileDownloader(root_folder)

    return [downloader(url, year, force) for url in _tract_shape_files(year)]
