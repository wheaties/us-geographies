from census.download import download_files
from census.reference import GROUP, load_mtfcc_table, load_funcstat_table


def load_files(connection, files, year, force=False):
    load_funcstat_table(connection, files.funcstat, year, force)
    load_mtfcc_table(connection, files.mtfcc, year, force)


def register_census(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
