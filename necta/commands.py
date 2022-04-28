from necta.download import download_files
from necta.delineation import load_raw_necta_cities, load_raw_necta_combined
from necta.shapes import load_necta_shapefile, load_necta_combined_shapefile, \
    load_necta_division_shapefile


GROUP = 'necta'


def load_files(connection, files, year, force=False):
    load_raw_necta_cities(connection, files.cities, year, force)
    load_raw_necta_combined(connection, files.combined, year, force)
    load_necta_shapefile(connection, files.city_shapes, year, force)
    load_necta_combined_shapefile(connection, files.combined_shapes, year, force)
    load_necta_division_shapefile(connection, files.division_shapes, year, force)


def register_necta(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
