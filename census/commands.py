from census.download import download_files
from census.reference import GROUP, load_mtfcc_table


def load_files(connection, files, year, force=False):
    load_mtfcc_table(connection, files, year, force)


def register_census(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
