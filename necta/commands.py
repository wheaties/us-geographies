from necta.download import download_files
from necta.necta_cities import load_raw_necta_cities, necta_cities
from necta.necta_combined import load_raw_necta_combined, necta_combined
from necta.necta_shape import load_necta_shapefile, necta_shape_setup


def run_necta(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    necta_cities.setup(connection, year, force)
    load_raw_necta_cities(connection, files.necta_cities, year, force)

    necta_combined.setup(connection, year, force)
    load_raw_necta_combined(connection, files.necta_combined, year, force)

    necta_shape_setup(connection, year, force)
    load_necta_shapefile(connection, files.necta_shape, year, force)
