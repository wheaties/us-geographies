from cbsa.cbsa_delineated import cbsa_delineation_setup, load_raw_cbsa
from cbsa.cbsa_shape import cbsa_shape_setup, load_cbsa_shapefile
from cbsa.csa_shape import csa_shape_setup, load_csa_shapefile
from cbsa.download import download_files


def run_cbsa(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    cbsa_delineation_setup(connection, year, force)
    load_raw_cbsa(connection, files.cbsa_delineation, year, force)

    cbsa_shape_setup(connection, year, force)
    load_cbsa_shapefile(connection, files.cbsa_shape, year, force)

    csa_shape_setup(connection, year, force)
    load_csa_shapefile(connection, files.csa_shape, year, force)
