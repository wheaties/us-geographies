from fips.download import download_files
from fips.fips_stategeocodes import load_raw_fips_stategeocodes
from fips.fips_state import load_fips_county_shapefile, load_fips_state_shapefile
from fips.fips_allgeocodes import load_raw_fips_allgeocodes


def run_fips(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder, force)

    load_raw_fips_stategeocodes(connection, files.state_geocodes, year, force)
    load_fips_state_shapefile(connection, files.state_shapes, year, force)
    load_fips_county_shapefile(connection, files.county_shapes, year, force)
    load_raw_fips_allgeocodes(connection, files.all_geocodes, year, force)
