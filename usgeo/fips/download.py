from collections import namedtuple
from usgeo.iops.download import download_to_cls, state_divided_paths, download_us_tiger_pattern


def _fips_state(year):
    if year < 2017:
        return f'https://www2.census.gov/programs-surveys/popest/geographies/{year}/state-geocodes-v{year}.xls'
    else:
        return f'https://www2.census.gov/programs-surveys/popest/geographies/{year}/state-geocodes-v{year}.xlsx'


def _fips_all(year):
    if year < 2015:
        return f'https://www2.census.gov/programs-surveys/popest/geographies/{year}/all-geocodes-v{year}.xls'
    else:
        return f'https://www2.census.gov/programs-surveys/popest/geographies/{year}/all-geocodes-v{year}.xlsx'


# TODO: issue with 2011 files
_fips_state_shapes = download_us_tiger_pattern('state')
# TODO: issue with 2012
_fips_county_shapes = download_us_tiger_pattern('county')


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
