from ua.download import download_files
from ua.shapes import load_files, GROUP


def register_ua(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
