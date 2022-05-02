from metro.delineation import load_raw_cbsa, load_raw_cities
from metro.shapes import load_cbsa_shapefile, load_csa_shapefile, load_metdiv_shapefile
from metro.download import download_files


GROUP = 'metro'


def load_files(connection, files, year, force=False):
    load_raw_cbsa(connection, files.cbsa_delineation, year, force)
    load_cbsa_shapefile(connection, files.cbsa_shape, year, force)
    load_metdiv_shapefile(connection, files.metdiv_shape, year, force)
    load_csa_shapefile(connection, files.csa_shape, year, force)
    load_raw_cities(connection, files.cities_delineation, year, force)


def register_metro(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
