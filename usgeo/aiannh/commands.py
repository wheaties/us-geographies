from usgeo.aiannh.download import download_files
from usgeo.aiannh.shapes import GROUP, load_anrc_shapefile, load_aiannh_shapefile, load_aitsn_shapefile, \
    load_tbg_shapefile, load_ttract_shapefile


def load_files(connection, files, year, force=False):
    load_aiannh_shapefile(connection, files.aiannh, year, force)
    load_aitsn_shapefile(connection, files.aitsn, year, force)
    load_anrc_shapefile(connection, files.anrc, year, force)
    load_tbg_shapefile(connection, files.tbg, year, force)
    load_ttract_shapefile(connection, files.ttract, year, force)


def register_aiannh(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
