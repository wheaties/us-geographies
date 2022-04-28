from functools import partial
from iops.database import RawDataTable
from metadata.methods import single_file_load
from parsers.xls import parse_file


necta_combined = RawDataTable('necta_combined')
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

necta_cities = RawDataTable('necta_cities')
necta_cities.columns = ['necta_code TEXT NOT NULL',
                        'necta_title TEXT NOT NULL',
                        'metro_micro_necta TEXT NOT NULL',
                        'principal_city_name TEXT NOT NULL',
                        'fips_state_code TEXT NOT NULL',
                        'fips_place_code TEXT NOT NULL']

load_raw_necta_cities = single_file_load(necta_cities,
                                         partial(parse_file, skip_beginning=2, skip_ending=4))
