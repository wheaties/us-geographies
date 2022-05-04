from iops.download import download_to_list, state_divided_paths


def _places_shapefiles(year):
    if year < 2010:
        return None
    elif year == 2010:
        for state in state_divided_paths():
            yield f'https://www2.census.gov/geo/tiger/TIGER2010/PLACE/2010/tl_2010_{state}_place10.zip'
    else:
        for state in state_divided_paths():
            yield f'https://www2.census.gov/geo/tiger/TIGER{year}/PLACE/tl_{year}_{state}_place.zip'


download_files = download_to_list(_places_shapefiles)
