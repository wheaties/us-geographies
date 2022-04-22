from puma.puma_shape import load_puma_shapefile, puma_shapes
from puma.download import download_files


def run_puma(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    if len(files):
        puma_shapes.setup(connection, year, force)

    for sf in files:
        load_puma_shapefile(connection, sf, year, force)
