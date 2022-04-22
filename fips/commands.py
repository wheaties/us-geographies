from fips.download import download_files
from fips.fips_stategeocodes import fips_stategeocodes, load_raw_fips_stategeocodes
from fips.fips_allgeocodes import fips_allgeocodes, load_raw_fips_allgeocodes


def run_fips(connection, year, root_folder=None, force=False):
    files = download_files(year, root_folder)

    fips_stategeocodes.setup(connection, year, force)
    load_raw_fips_stategeocodes(connection, files.state_geocodes, year, force)

    fips_allgeocodes.setup(connection, year, force)
    load_raw_fips_allgeocodes(connection, files.all_geocodes, year, force)