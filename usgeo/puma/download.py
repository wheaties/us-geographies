from usgeo.iops.download import download_to_list, state_divided_paths


# issues with 2013, 2014
def _puma_shape_files(year):
    if year < 2012:
        return []

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/PUMA/tl_{year}_{state}_puma10.zip'


download_files = download_to_list(_puma_shape_files)
