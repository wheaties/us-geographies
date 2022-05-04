from iops.download import download_to_list, state_divided_paths


def _blockgroup_shapes(year):
    if year < 2010:
        return []
    elif year == 2010:
        for state in state_divided_paths():
            yield f'https://www2.census.gov/geo/tiger/TIGER2010/BG/2010/tl_2010_{state}_bg10.zip'
    else:
        for state in state_divided_paths():
            yield f'https://www2.census.gov/geo/tiger/TIGER{year}/BG/tl_{year}_{state}_bg.zip'


download_files = download_to_list(_blockgroup_shapes)
