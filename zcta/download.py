from iops.download import download_to_file


def _zcta_files(year):
    if year < 2010 or year == 2011:
        return None  # it doesn't exist prior to 2012 in this format except 2010
    elif year == 2010:
        return 'https://www2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/tl_2010_us_zcta510.zip'
    elif year < 2020:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/ZCTA5/tl_{year}_us_zcta510.zip'
    else:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/ZCTA520/tl_{year}_us_zcta520.zip'


download_files = download_to_file(_zcta_files)
