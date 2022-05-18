from usgeo.census.download import download_files
from usgeo.census.reference import GROUP, load_funcstat_table, load_class_table, load_mtfcc_table, \
    load_lsad_table


def load_files(connection, files, year, force=False):
    load_funcstat_table(connection, files.funcstat, year, force)
    load_mtfcc_table(connection, files.mtfcc, year, force)
    load_class_table(connection, files.class_code, year, force)
    load_lsad_table(connection, files.lsad, year, force)


def register_census(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
