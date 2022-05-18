from functools import partial
from usgeo.iops.database import RawDataTable
from usgeo.iops.metadata import single_file_load
from usgeo.parsers.xls import parse_file


GROUP = 'metro'


cbsa_table = RawDataTable('cbsa', GROUP)
cbsa_table.columns = ['cbsa_code TEXT NOT NULL',
                      'metro_division_code TEXT',
                      'csa_code TEXT',
                      'cbsa_title TEXT NOT NULL',
                      'metro_micro_statistical_area TEXT',
                      'metro_division_title TEXT',
                      'csa_title TEXT',
                      'county_equiv TEXT NOT NULL',
                      'state_name TEXT NOT NULL',
                      'fips_state_code TEXT NOT NULL',
                      'fips_county_code TEXT NOT NULL',
                      'central_outlying TEXT NOT NULL']

load_raw_cbsa = single_file_load(cbsa_table,
                                 partial(parse_file, skip_beginning=2, skip_ending=4))

cities_table = RawDataTable('principal_cities', GROUP)
cities_table.columns = ['cbsa_code TEXT NOT NULL',
                        'cbsa_title TEXT NOT NULL',
                        'metro_micro_statistical_area TEXT',
                        'city_name TEXT NOT NULL',
                        'fips_state_code TEXT NOT NULL',
                        'fips_place_code TEXT NOT NULL']

load_raw_cities = single_file_load(cities_table,
                                   partial(parse_file, skip_beginning=2, skip_ending=4))

necta_combined = RawDataTable('necta_combined', GROUP)
necta_combined.columns =['necta_code TEXT NOT NULL',
                         'necta_division_code TEXT',
                         'necta_combined_code TEXT',
                         'necta_title TEXT NOT NULL',
                         'metro_micro_necta TEXT NOT NULL',
                         'necta_division_title TEXT',
                         'necta_combined_title TEXT',
                         'city_name TEXT',
                         'fips_state_code TEXT NOT NULL',
                         'fips_county_code TEXT',
                         'fips_county_subdivision_code TEXT']


load_raw_necta_combined = single_file_load(necta_combined,
                                           partial(parse_file, skip_beginning=2, skip_ending=4))

necta_cities = RawDataTable('necta_cities', GROUP)
necta_cities.columns = ['necta_code TEXT NOT NULL',
                        'necta_title TEXT NOT NULL',
                        'metro_micro_necta TEXT NOT NULL',
                        'principal_city_name TEXT NOT NULL',
                        'fips_state_code TEXT NOT NULL',
                        'fips_place_code TEXT NOT NULL']

load_raw_necta_cities = single_file_load(necta_cities,
                                         partial(parse_file, skip_beginning=2, skip_ending=4))
