from zcta.download import download_files
#from zcta.shapes import load_zcta_shapefile


GROUP = 'zcta'


# def load_files(connection, shapefile, year, force=False):
#    load_zcta_shapefile(connection, shapefile, year, force)


def register_zcta(registry):
    registry.get[GROUP] = download_files
    # registry.load[GROUP] = load_files
