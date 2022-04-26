from functools import partial
from iops.database import RawDataTable
from metadata.methods import single_file_load
from parsers.xls import parse_file


necta_cities = RawDataTable('necta_cities')
necta_cities.columns = ['necta_code TEXT NOT NULL',
                        'necta_title TEXT NOT NULL',
                        'metro_micro_necta TEXT NOT NULL',
                        'principal_city_name TEXT NOT NULL',
                        'fips_state_code TEXT NOT NULL',
                        'fips_place_code TEXT NOT NULL']

load_raw_necta_cities = single_file_load(necta_cities,
                                         partial(parse_file, skip_beginning=2, skip_ending=4))
