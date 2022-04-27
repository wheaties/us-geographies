from collections import namedtuple
from iops.download import download_to_cls


# index out of range for 2013, header/footer offset different?
_necta_combined_files = {
    2013: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2013/delineation-files/list3.xls',
    2015: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2015/delineation-files/list3.xls',
    2017: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2017/delineation-files/list3.xls',
    2018: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list3_Sep_2018.xls',
    2020: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2020/delineation-files/list3_2020.xls'
}

_necta_cities_files = {
    2013: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2013/delineation-files/list4.xls',
    2015: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2015/delineation-files/list4.xls',
    2017: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2017/delineation-files/list4.xls',
    2018: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list4_Sep_2018.xls',
    2020: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2020/delineation-files/list4_2020.xls'
}

_necta_combined_shapefiles = {
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/CNECTA/tl_2013_us_cnecta.zip',
    2014: 'https://www2.census.gov/geo/tiger/TIGER2014/CNECTA/tl_2014_us_cnecta.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/CNECTA/tl_2015_us_cnecta.zip',
    2016: 'https://www2.census.gov/geo/tiger/TIGER2016/CNECTA/tl_2016_us_cnecta.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/CNECTA/tl_2017_us_cnecta.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/CNECTA/tl_2018_us_cnecta.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/CNECTA/tl_2019_us_cnecta.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/CNECTA/tl_2020_us_cnecta.zip',
    2021: 'https://www2.census.gov/geo/tiger/TIGER2021/CNECTA/tl_2021_us_cnecta.zip'
}

_necta_division_shapefiles = {
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/NECTADIV/tl_2020_us_nectadiv.zip'
}

_necta_shapefiles = {
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/NECTA/tl_2020_us_necta.zip'
}


NECTAFiles = namedtuple('NECTAFiles',
                        ['combined', 'cities', 'combined_shapes', 'division_shapes', 'city_shapes'])
download_files = download_to_cls(NECTAFiles,
                                 _necta_combined_files,
                                 _necta_cities_files,
                                 _necta_combined_shapefiles,
                                 _necta_division_shapefiles,
                                 _necta_shapefiles)
