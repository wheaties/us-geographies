from sd.download import download_files
from sd.shapes import GROUP, load_elsd_shapefile, load_scsd_shapefile, load_unsd_shapefile


def load_files(connection, files, year, force=False):
    for sf in files.elementary_shapes:
        load_elsd_shapefile(connection, sf, year, force)
    for sf in files.secondary_shapes:
        load_scsd_shapefile(connection, sf, year, force)
    for sf in files.unified_shapes:
        load_unsd_shapefile(connection, sf, year, force)


def register_sd(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
