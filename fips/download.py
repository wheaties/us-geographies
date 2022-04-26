from collections import namedtuple
from iops.download import download_to_cls, state_divided_paths


gnis_url = {
    2010: 'https://geonames.usgs.gov/docs/federalcodes/NationalFedCodes.zip'
}

_fips_state = {
    2013: 'https://www2.census.gov/programs-surveys/popest/geographies/2013/state-geocodes-v2013.xls',
    2014: 'https://www2.census.gov/programs-surveys/popest/geographies/2014/state-geocodes-v2014.xls',
    2015: 'https://www2.census.gov/programs-surveys/popest/geographies/2015/state-geocodes-v2015.xls',
    2016: 'https://www2.census.gov/programs-surveys/popest/geographies/2016/state-geocodes-v2016.xls',
    2017: 'https://www2.census.gov/programs-surveys/popest/geographies/2017/state-geocodes-v2017.xlsx',
    2018: 'https://www2.census.gov/programs-surveys/popest/geographies/2018/state-geocodes-v2018.xlsx',
    2019: 'https://www2.census.gov/programs-surveys/popest/geographies/2019/state-geocodes-v2019.xlsx',
    2020: 'https://www2.census.gov/programs-surveys/popest/geographies/2020/state-geocodes-v2020.xlsx'
}

_fips_all = {
    2013: 'https://www2.census.gov/programs-surveys/popest/geographies/2013/all-geocodes-v2013.xls',
    2014: 'https://www2.census.gov/programs-surveys/popest/geographies/2014/all-geocodes-v2014.xls',
    2015: 'https://www2.census.gov/programs-surveys/popest/geographies/2015/all-geocodes-v2015.xlsx',
    2016: 'https://www2.census.gov/programs-surveys/popest/geographies/2016/all-geocodes-v2016.xlsx',
    2017: 'https://www2.census.gov/programs-surveys/popest/geographies/2017/all-geocodes-v2017.xlsx',
    2018: 'https://www2.census.gov/programs-surveys/popest/geographies/2018/all-geocodes-v2018.xlsx',
    2019: 'https://www2.census.gov/programs-surveys/popest/geographies/2019/all-geocodes-v2019.xlsx',
    2020: 'https://www2.census.gov/programs-surveys/popest/geographies/2020/all-geocodes-v2020.xlsx'
}

# TODO: issue with 2011 files
_fips_state_shapes = {
    2011: 'https://www2.census.gov/geo/tiger/TIGER201/STATE/tl_2011_us_state.zip',
    2012: 'https://www2.census.gov/geo/tiger/TIGER2012/STATE/tl_2012_us_state.zip',
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/STATE/tl_2013_us_state.zip',
    2014: 'https://www2.census.gov/geo/tiger/TIGER2014/STATE/tl_2014_us_state.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/STATE/tl_2015_us_state.zip',
    2016: 'https://www2.census.gov/geo/tiger/TIGER2016/STATE/tl_2016_us_state.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/STATE/tl_2017_us_state.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/STATE/tl_2018_us_state.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/STATE/tl_2019_us_state.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/STATE/tl_2020_us_state.zip',
    2021: 'https://www2.census.gov/geo/tiger/TIGER2021/STATE/tl_2021_us_state.zip'
}

# TODO: issue with 2012
_fips_county_shapes = {
    2011: 'https://www2.census.gov/geo/tiger/TIGER2011/COUNTY/tl_2011_us_county.zip',
    2012: 'https://www2.census.gov/geo/tiger/TIGER2012/COUNTY/tl_2012_us_county.zip',
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/COUNTY/tl_2013_us_county.zip',
    2014: 'https://www2.census.gov/geo/tiger/TIGER2014/COUNTY/tl_2014_us_county.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/COUNTY/tl_2015_us_county.zip',
    2016: 'https://www2.census.gov/geo/tiger/TIGER2016/COUNTY/tl_2016_us_county.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/COUNTY/tl_2017_us_county.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/tl_2018_us_county.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/tl_2019_us_county.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/tl_2020_us_county.zip',
    2021: 'https://www2.census.gov/geo/tiger/TIGER2021/COUNTY/tl_2021_us_county.zip'
}


def _fips_county_sub(year):
    if year < 2011:
        yield []  # more complicated, see https://www2.census.gov/geo/tiger/TIGER2010/COUSUB/2010/

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/COUSUB/tl_{year}_{state}_cousub.zip'


def _fips_place(year):
    if year < 2011:
        yield []

    for state in state_divided_paths():
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/PLACE/tl_{year}_{state}_place.zip'


def _fips_city(year):
    if year < 2011:
        yield []

    for state in ['09', 13, 18, 20, 21, 30, 47]:
        yield f'https://www2.census.gov/geo/tiger/TIGER{year}/CONCITY/tl_{year}_{state}_concity.zip'


FIPSFiles = namedtuple('FIPSFiles',
                       ['state_geocodes',
                        'state_shapes',
                        'all_geocodes',
                        'county_shapes',
                        'county_subdiv_shapes',
                        'place_shapes',
                        'city_shapes'])
download_files = download_to_cls(FIPSFiles,
                                 _fips_state,
                                 _fips_state_shapes,
                                 _fips_all,
                                 _fips_county_shapes,
                                 _fips_county_sub,
                                 _fips_place,
                                 _fips_city)
