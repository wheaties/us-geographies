from tract.shapes import load_files
from tract.download import download_files


GROUP = 'tract'


def register_tract(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
