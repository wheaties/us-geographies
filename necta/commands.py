from necta.download import download_files
from necta.necta_cities import load_raw_necta_cities
from necta.necta_combined import load_raw_necta_combined
from necta.necta_shape import load_necta_shapefile, load_necta_combined_shapefile, \
    load_necta_division_shapefile


def run_necta(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    load_raw_necta_cities(connection, files.cities, year, force)
    load_raw_necta_combined(connection, files.combined, year, force)
    load_necta_shapefile(connection, files.city_shapes, year, force)
    load_necta_combined_shapefile(connection, files.combined_shapes, year, force)
    load_necta_division_shapefile(connection, files.division_shapes, year, force)
