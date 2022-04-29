from iops.download import download_to_file


def _cd_shapefiles(year):
    if year < 2010:
        return None
    else:
        cd = (year-1786)//2
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/CD/tl_{year}_us_cd{cd}.zip'


download_files = download_to_file(_cd_shapefiles)
