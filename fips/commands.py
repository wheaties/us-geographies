from fips.download import download_files
from fips.delineation import load_raw_fips_stategeocodes, load_raw_fips_allgeocodes
from fips.shapes import load_fips_county_shapefile, load_fips_state_shapefile, \
    load_fips_county_subdivision_shapefile, load_fips_place_shapefile, \
    load_fips_city_shapefile


GROUP = 'fips'


def load_files(connection, files, year, force=False):
    load_raw_fips_stategeocodes(connection, files.state_geocodes, year, force)
    load_fips_state_shapefile(connection, files.state_shapes, year, force)
    load_fips_county_shapefile(connection, files.county_shapes, year, force)
    load_fips_county_subdivision_shapefile(connection, files.county_subdiv_shapes, year, force)
    load_fips_place_shapefile(connection, files.place_shapes, year, force)
    load_fips_city_shapefile(connection, files.city_shapes, year, force)
    load_raw_fips_allgeocodes(connection, files.all_geocodes, year, force)


def register_fips(registry):
    registry.get[GROUP] = download_files
    registry.load[GROUP] = load_files
