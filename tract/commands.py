from tract.tract_shape import load_tract_shapefile, tract_shapes
from tract.download import download_files


def run_tract(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    if len(files):
        tract_shapes.setup(connection, year, force)

    for sf in files:
        load_tract_shapefile(connection, sf, year, force)
