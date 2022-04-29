from cbsa.delineation import load_raw_cbsa
from cbsa.shapes import load_cbsa_shapefile, load_csa_shapefile, load_metdiv_shapefile
from cbsa.download import download_files


GROUP = 'cbsa'


def load_files(connection, files, year, force=False):
    load_raw_cbsa(connection, files.cbsa_delineation, year, force)
    load_cbsa_shapefile(connection, files.cbsa_shape, year, force)
    load_metdiv_shapefile(connection, files.metdiv_shape, year, force)
    load_csa_shapefile(connection, files.csa_shape, year, force)


def register_cbsa(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
