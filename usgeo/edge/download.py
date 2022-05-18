from usgeo.iops.download import download_to_file


def _locale_files(year):
    if year < 2014:
        return None
    elif year == 2014:
        return 'https://nces.ed.gov/programs/edge/data/EDGE_LOCALE14_NCES_ALL_US.zip'
    elif year == 2020:
        return 'https://nces.ed.gov/programs/edge/data/edge_locale20_nces_all_us.zip'
    else:
        return f'https://nces.ed.gov/programs/edge/data/EDGE_LOCALE{str(year)[2:4]}_US.zip'


download_file = download_to_file(_locale_files)
