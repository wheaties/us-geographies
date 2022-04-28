from sld.download import download_files
from sld.shapes import load_sldl_shapefile, load_sldu_shapefile


GROUP = 'sld'


def load_files(connection, files, year, force):
    for sf in files.sldl:
        load_sldl_shapefile(connection, sf, year, force)

    for sf in files.sldu:
        load_sldu_shapefile(connection, sf, year, force)


def register_sld(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
