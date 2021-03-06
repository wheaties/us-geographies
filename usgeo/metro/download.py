from collections import namedtuple
from usgeo.iops.download import download_to_cls, download_us_tiger_pattern


# TODO: issue with 2013!
def _cbsa_delineation_files(year):
    if year in (2013, 2015, 2017):
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list1.xls'
    elif year == 2018:
        return 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list1_Sep_2018.xls',
    else:
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list1_{year}.xls'


def _principal_cities_files(year):
    if year in (2013, 2015, 2017):
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list2.xls'
    elif year == 2018:
        return 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list2_Sep_2018.xls',
    else:
        return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list2_{year}.xls'


_cbsa_shapefiles = download_us_tiger_pattern('cbsa')
_metdiv_shapefiles = download_us_tiger_pattern('metdiv')
_csa_shapefiles = download_us_tiger_pattern('csa')


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

MetroFiles = namedtuple('MetroFiles',
                        ['cbsa_delineation',
                         'cities_delineation',
                         'cbsa_shape',
                         'metdiv_shape',
                         'csa_shape',
                         'necta_combined',
                         'necta_cities',
                         'necta_combined_shapes',
                         'necta_division_shapes',
                         'necta_city_shapes'])

download_files = download_to_cls(MetroFiles,
                                 _cbsa_delineation_files,
                                 _principal_cities_files,
                                 _cbsa_shapefiles,
                                 _metdiv_shapefiles,
                                 _csa_shapefiles,
                                 _necta_combined_files,
                                 _necta_cities_files,
                                 _necta_combined_shapefiles,
                                 _necta_division_shapefiles,
                                 _necta_shapefiles)
