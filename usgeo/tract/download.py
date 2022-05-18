from usgeo.iops.download import download_to_list, state_divided_paths


def _tract_shape_files(year):
    if year < 2010:
        return []  # someone else can figure this stuff out
    elif year == 2010:
        return ['https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_01_tract10.zip']

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/TRACT/tl_{year}_{state}_tract.zip'


download_files = download_to_list(_tract_shape_files)
