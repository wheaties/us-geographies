from cd.download import download_files
from cd.shapes import load_cd_shapefile


GROUP = 'cd'


def register_cd(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_cd_shapefile
