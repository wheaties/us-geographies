from puma.shapes import load_puma_shapefile
from puma.download import download_files


GROUP = 'puma'


def load_files(connection, files, year, force=False):
    for sf in files:
        load_puma_shapefile(connection, sf, year, force)


def register_puma(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
