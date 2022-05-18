import click
from usgeo.aiannh.commands import register_aiannh
from usgeo.bg.commands import register_bg
from usgeo.cd.commands import register_cd
from usgeo.census.commands import register_census
from usgeo.edge.commands import register_edge
from usgeo.fips.commands import register_fips
from usgeo.iops.database import connect_db
from usgeo.metro.commands import register_metro
from usgeo.puma.commands import register_puma
from usgeo.sd.commands import register_sd
from usgeo.sld.commands import register_sld
from usgeo.tract.commands import register_tract
from usgeo.ua.commands import register_ua
from usgeo.zcta.commands import register_zcta


class _Registry:
    def __init__(self):
        self.get = {}
        self._register_all(self.get)
        self.load = {}
        self._register_all(self.load)

    def _register_all(self, lookup):
        def all_fn(*args):
            output = {}
            for k in lookup:
                if k != 'all':
                    output[k] = lookup[k](*args)
            return output
        lookup['all'] = all_fn(lookup)


registry = _Registry()
register_aiannh(registry)
register_bg(registry)
register_cd(registry)
register_census(registry)
register_edge(registry)
register_fips(registry)
register_metro(registry)
register_puma(registry)
register_sd(registry)
register_sld(registry)
register_tract(registry)
register_ua(registry)
register_zcta(registry)


@click.command()
@click.option('--path', type=click.Path(), default=None, help='target location to write file(s)')
@click.option('--force', is_flag=True, help='download and overwrite existing file(s)')
@click.argument('dataset', type=click.types.Choice(registry.get.keys(), False), nargs=-1)
@click.argument('year', type=click.types.INT, nargs=1)
def get(dataset, year, path, force):
    """Retrieves various shapefiles and stores them locally.

    \b
    DATASET may be one or more of the following:
         * aiannh - American Indian, Alaskan Native, and Native Hawaiian geographies, Census TIGER/Line shapefiles
         * bg - Census Block Groups, TIGER/Line shape files
         * cd - Congressional Districts, Census TIGER/Line shape files
         * census - supporting documentation to identify codes within Census TIGER/Line shapefiles
         * edge - NCES Locale Classifications
         * fips - Federal Information Processing Series, Census TIGER/Line shape files
         * metro - Metro/Micropolitan statical areas, Census TIGER/Line shape files
         * puma - Public Use Microdata Area, Census TIGER/Line shape files
         * sd - School Districts, Census TIGER/Line shape files
         * sld - State Legislative Districts, Census TIGER/Line shape files
         * tract - Census Tracts, TIGER/Line shape files
         * ua - Urban Areas, Census TIGER/Line shape files
         * zcta - Zip Code Tabulation Areas, Census TIGER/Line shape files

        \b
    YEAR may be any year from 2010 and above"""
    for ds in dataset:
        click.echo(f'Fetching {ds} for {year}.')
        registry.get[ds](year, path, force)


@click.command()
@click.option('--path', type=click.Path(), default=None, help='target location to search for file(s).')
@click.option('--force', is_flag=True, help='overwrite existing db tables.')
@click.option('--dbname', default=None, help='db name, can be a connection string.')
@click.option('--dbhost', default=None, help='db host, will be overridden if contained in dbname param.')
@click.option('--dbport', default=5432, type=click.INT, help='db port, will be overridden if contained in dbname param.')
@click.option('--dbuser', default=None, help='db user, will be overridden if contained in dbname param.')
@click.option('--dbpass', default=None, help='db password, will be overridden if contained in dbname param.')
@click.argument('dataset', type=click.types.Choice(registry.load.keys(), False), nargs=-1)
@click.argument('year', type=click.types.INT, nargs=1)
def load(dataset, year, path, force, dbname, dbhost, dbport, dbuser, dbpass):
    """Loads the queried datasets into a PostgreSQL database using the supplied parameters.

    \b
    DATASET may be one or more of the following:
     * aiannh - American Indian, Alaskan Native, and Native Hawaiian geographies, Census TIGER/Line shapefiles
     * cd - Congressional Districts, Census TIGER/Line shape files
     * census - supporting documentation to identify codes within Census TIGER/Line shapefiles
     * fips - Federal Information Processing Series, Census TIGER/Line shape files
     * metro - Metro/Micropolitan statical areas, Census TIGER/Line shape files
     * puma - Public Use Microdata Area, Census TIGER/Line shape files
     * sd - School Districts, Census TIGER/Line shape files
     * sld - State Legislative Districts, Census TIGER/Line shape files
     * tract - Census Tracts, TIGER/Line shape files
     * ua - Urban Areas, Census TIGER/Line shape files

    \b
    YEAR may be any year from 2010 and above"""
    for ds in dataset:
        click.echo(f'Reading or obtaining {ds} files for {year}.')
        # if you want to force getting files, force at the 'get' command
        result = registry.get[ds](year, path)
        click.echo(f'Loading {ds} files into db for {year}.')
        with connect_db(dbname, dbhost, dbport, dbuser, dbpass) as db:
            registry.load[ds](db, result, year, force)


@click.group()
def cli():
    pass


cli.add_command(get)
cli.add_command(load)
