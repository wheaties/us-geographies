from sld.download import download_files
from sld.shapes import load_sldl_shapefile, load_sldu_shapefile


def run_sld(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder, force)

    for sf in files.sldl:
        load_sldl_shapefile(connection, sf, year, force)

    for sf in files.sldu:
        load_sldu_shapefile(connection, sf, year, force)
