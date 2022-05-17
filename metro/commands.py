from metro.delineation import load_raw_cbsa, load_raw_cities, load_raw_necta_cities, load_raw_necta_combined
from metro.shapes import GROUP, load_cbsa_shapefile, load_csa_shapefile, load_metdiv_shapefile, load_necta_shapefile, \
    load_necta_combined_shapefile, load_necta_division_shapefile
from metro.download import download_files


def load_files(connection, files, year, force=False):
    load_raw_cbsa(connection, files.cbsa_delineation, year, force)
    load_cbsa_shapefile(connection, files.cbsa_shape, year, force)
    load_metdiv_shapefile(connection, files.metdiv_shape, year, force)
    load_csa_shapefile(connection, files.csa_shape, year, force)
    load_raw_cities(connection, files.cities_delineation, year, force)
    load_raw_necta_cities(connection, files.necta_cities, year, force)
    load_raw_necta_combined(connection, files.necta_combined, year, force)
    load_necta_shapefile(connection, files.necta_city_shapes, year, force)
    load_necta_combined_shapefile(connection, files.necta_combined_shapes, year, force)
    load_necta_division_shapefile(connection, files.necta_division_shapes, year, force)


def register_metro(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
