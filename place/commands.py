from place.download import download_files
from place.shapes import load_places_shapefile


GROUP = 'place'


def load_files(connection, files, year, force=False):
    for sf in files:
        load_places_shapefile(connection, sf, year, force)


def register_place(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
