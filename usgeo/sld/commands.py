from usgeo.sld.download import download_files
from usgeo.sld.shapes import load_sldl_shapefile, load_sldu_shapefile


GROUP = 'sld'


def load_files(connection, files, year, force):
    load_sldl_shapefile(connection, files.sldl, year, force)
    load_sldu_shapefile(connection, files.sldu, year, force)


def register_sld(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
