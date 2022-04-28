# Goals:
# 1. to be able to download different US shapefile datasets
#  d. (optional) ZCTA
#  e. (optional) RUCA (https://www.ers.usda.gov/webdocs/DataFiles/53241/ruca2010revised.xlsx?v=9111.7d)
#  f. (optional) any more from https://www2.census.gov/geo/tiger/
#  g. GNIS (plus FIPS crosswalk)
#  h. LZPS (is this the zip codes? Think it's city state product)
#  i. see: https://www.census.gov/programs-surveys/geography/technical-documentation/records-layout/nlt-record-layouts.html
# 2. FIPS shapefiles, gotta figure out which ones are actually important
# 3. to be able to load different US datasets into a DB
#  a. first as 'raw'
#  b. then as 'cleaned up'
# 4. identify dataset dependencies for the "cleaned up" version
# 5. supporting datasets to understand the content
#  a. MTFCC (https://www.census.gov/library/reference/code-lists/mt-feature-class-codes.html)
#  b. FUNCSTAT (https://www.census.gov/library/reference/code-lists/functional-status-codes.html)
#  c. CLASSFP (https://www.census.gov/library/reference/code-lists/class-codes.html)

# see: https://www.nber.org/research/data/ssa-federal-information-processing-series-fips-state-and-county-crosswalk
# see: https://www.usgs.gov/u.s.-board-on-geographic-names/download-gnis-data
# see: https://www.huduser.gov/portal/datasets/usps_crosswalk.html
# see: https://postalpro.usps.com/address-quality/city-state-product
# see: https://www.census.gov/programs-surveys/geography/guidance/geo-areas/state-legis-dist.html
# see: https://www.census.gov/newsroom/blogs/random-samplings/2011/07/what-are-census-blocks.html
# see: https://www2.census.gov/geo/docs/maps-data/data/rel/
# see: https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries
# see: https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries
#      https://nces.ed.gov/programs/edge/data/EDGESCHOOLDISTRICT_TL21_SY2021.zip

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

# how I want it to look
# us-geo fetch fips --shape
# us-geo fetch fips
# us-geo fetch --dest='
# us-geo load fips --src=''
# us-geo load fips
# us-geo load fips --db=''

import click
from cbsa.commands import register_cbsa
from cd.commands import register_cd
from fips.commands import register_fips
from necta.commands import register_necta
from puma.commands import register_puma
from sld.commands import register_sld
from tract.commands import register_tract


class Registry:
    def __init__(self):
        self.get = {}
        self.load = {}


registry = Registry()
register_cbsa(registry)
register_cd(registry)
register_fips(registry)
register_necta(registry)
register_puma(registry)
register_sld(registry)
register_tract(registry)


@click.command()
@click.option('--path', type=click.Path(), default=None, help='target location to write file(s)')
@click.option('--force', is_flag=True, help='download and overwrite existing file(s)')
@click.argument('dataset', type=click.types.Choice(registry.get.keys(), False), nargs=-1)
@click.argument('year', type=click.types.INT, nargs=1)
def get(dataset, year, path, force):
    for ds in dataset:
        click.echo(f'Fetching {ds} for {year}.')
        registry.get[ds](year, path, force)


@click.command()
@click.option('--path', type=click.Path(), default=None, help='target location to write file(s)')
@click.option('--force', is_flag=True, help='overwrite existing db tables')
@click.argument('dataset', type=click.types.Choice(registry.load.keys(), False), nargs=-1)
@click.argument('year', type=click.types.INT, nargs=1)
def load(dataset, year, path, force):
    for ds in dataset:
        click.echo(f'Reading or obtaining {ds} files for {year}.')
        # if you want to force getting files, force at the 'get' command
        result = registry.get[ds](year, path)
        click.echo(f'Loading {ds} files into db for {year}.')
        with connect_db() as db:
            registry.load[ds](db, result, year, force)


@click.group()
def cli():
    pass


cli.add_command(get)
cli.add_command(load)
if __name__ == '__main__':
    cli()
