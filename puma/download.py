from iops.download import LocalFileDownloader, state_divided_paths


# issues with 2013, 2014
def _puma_shape_files(year):
    if year < 2012:
        return []

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/PUMA/tl_{year}_{state}_puma10.zip'


def download_files(year, root_folder=None, force=False):
    downloader = LocalFileDownloader(root_folder)

    return [downloader(url, year, force) for url in _puma_shape_files(year)]
