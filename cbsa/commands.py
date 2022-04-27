from cbsa.cbsa_delineated import load_raw_cbsa
from cbsa.shapes import load_cbsa_shapefile, load_csa_shapefile
from cbsa.download import download_files


def run_cbsa(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    load_raw_cbsa(connection, files.cbsa_delineation, year, force)
    load_cbsa_shapefile(connection, files.cbsa_shape, year, force)
    load_csa_shapefile(connection, files.csa_shape, year, force)
