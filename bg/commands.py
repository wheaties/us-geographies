from bg.download import download_files
from bg.shapes import load_blockgroup_shapefile


GROUP = 'bg'


# TODO: blockgroup files are missing .dbf
# def load_files(connection, files, year, force=False):
#    for sf in files:
#        load_blockgroup_shapefile(connection, sf, year, force)


def register_bg(registry):
    registry.get[GROUP] = download_files
    # registry.load[GROUP] = load_files
