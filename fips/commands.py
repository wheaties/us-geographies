from fips.download import download_files
from fips.fips_stategeocodes import fips_stategeocode_setup, load_raw_fips_stategeocodes
from fips.fips_allgeocodes import fips_allgeocode_setup, load_raw_fips_allgeocodes


def run_fips(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    fips_stategeocode_setup(connection, year, force)
    load_raw_fips_stategeocodes(connection, files.state_geocodes, year, force)

    fips_allgeocode_setup(connection, year, force)
    load_raw_fips_allgeocodes(connection, files.all_geocodes, year, force)