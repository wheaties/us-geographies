from cd.download import download_files
from cd.cd_shape import load_cd_shapefile, cd_shapes


def run_cd(connection, year, root_folder=None, force=False):
    sh = download_files(year, root_folder)

    cd_shapes.setup(connection, year, force)
    load_cd_shapefile(connection, sh, year, force)
