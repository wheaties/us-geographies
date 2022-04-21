from cbsa.commands import run_cbsa
from fips.commands import run_fips
from necta.commands import run_necta
from puma.commands import run_puma

#Goals:
# 1. to be able to download different US shapefile datasets
#  d. (optional) ZCTA
#  e. (optional) RUCA (https://www.ers.usda.gov/webdocs/DataFiles/53241/ruca2010revised.xlsx?v=9111.7d)
#  f. (optional) any more from https://www2.census.gov/geo/tiger/
#  g. GNIS (plus FIPS crosswalk)
#  h. LZPS (is this the zip codes? Think it's city state product)
#  i. PUMA
# 2. FIPS shapefiles, gotta figure out which ones are actually important
# 3. to be able to load different US datasets into a DB
#  a. first as 'raw'
#  b. then as 'cleaned up'
# 4. identify dataset dependencies for the "cleaned up" version

# notes: more than just FIPS? https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html
# see: https://www.census.gov/library/reference/code-lists/ansi.html
# see: https://www.nber.org/research/data/ssa-federal-information-processing-series-fips-state-and-county-crosswalk
# see: https://www2.census.gov/geo/docs/reference/codes/files/
# see: https://www.usgs.gov/u.s.-board-on-geographic-names/download-gnis-data
# see: https://www.census.gov/programs-surveys/popest/geographies/reference-files.html
# see: https://www.huduser.gov/portal/datasets/usps_crosswalk.html
# see: https://postalpro.usps.com/address-quality/city-state-product
# see: https://www.census.gov/programs-surveys/geography/guidance/geo-areas/state-legis-dist.html
# see: https://www.census.gov/programs-surveys/geography/guidance/geo-areas/congressional-dist.html
# see: https://www.census.gov/newsroom/blogs/random-samplings/2011/07/what-are-census-blocks.html
# see: https://www2.census.gov/geo/docs/maps-data/data/rel/

#see: https://stackoverflow.com/questions/32812463/setting-schema-for-all-queries-of-a-connection-in-psycopg2-getting-race-conditi
import psycopg2
def connect_db(schema=None):
    conn = psycopg2.connect('postgresql://postgres:admin@localhost:5432')
    with conn.cursor() as cursor:
        cursor.execute('SELECT 1')
    return conn

#notes on CBSA
# 1. made of entire counties
# 2. uses most columns
# 3. a CBSA isn't limited to a single state
def gen_cbsa_view():
    #SELECT DISTINCT(csa_code), csa_title
	#FROM cbsa_2020_raw
	#WHERE csa_code IS NOT NULL

    #cbsa use the micro metro stuff when relating to FIPS counties
    #csa doesn't use them
    #see: https://www.federalregister.gov/documents/2021/07/16/2021-15159/2020-standards-for-delineating-core-based-statistical-areas
    pass


if __name__ == '__main__':
    print('Hello World')
    with connect_db() as db:
        #run_cbsa(db, 2020, force=True)
        #run_fips(db, 2014, force=True)
        #run_necta(db, 2020, force=True)
        #run_puma(db, 2020, force=True)
    print('yo')
