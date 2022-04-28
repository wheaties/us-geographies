from tract.shapes import load_tract_shapefile
from tract.download import download_files


GROUP = 'tract'


def load_files(connection, files, year, force=False):
    for sf in files:
        load_tract_shapefile(connection, sf, year, force)


def register_tract(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
