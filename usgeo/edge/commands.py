from usgeo.edge.download import download_file
# from edge.shapes import load_file


GROUP = 'edge'


def register_edge(registry):
    registry.get[GROUP] = download_file
#    registry.load[GROUP] = load_file
