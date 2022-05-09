from collections import namedtuple
from iops.download import download_to_cls, download_us_tiger_pattern


# index out of range for 2013, header/footer offset different?
def _necta_combined_files(year):
    if year in (2013, 2015, 2017):
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list3.xls'
    elif year == 2018:
        return 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list3_Sep_2018.xls',
    else:
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list3_{year}.xls'


def _necta_cities_files(year):
    if year in (2013, 2015, 2017):
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list4.xls'
    elif year == 2018:
        return 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list4_Sep_2018.xls',
    else:
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list4_{year}.xls'


_necta_combined_shapefiles = download_us_tiger_pattern('cnecta')
_necta_division_shapefiles = download_us_tiger_pattern('nectadiv')
_necta_shapefiles = download_us_tiger_pattern('necta')

NECTAFiles = namedtuple('NECTAFiles',
                        ['combined', 'cities', 'combined_shapes', 'division_shapes', 'city_shapes'])
download_files = download_to_cls(NECTAFiles,
                                 _necta_combined_files,
                                 _necta_cities_files,
                                 _necta_combined_shapefiles,
                                 _necta_division_shapefiles,
                                 _necta_shapefiles)
