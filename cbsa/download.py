from collections import namedtuple
from iops.download import download_to_cls


# TODO: issue with 2013!
def _cbsa_delineation_files(year):
    if year == 2018:
        return 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list1_Sep_2018.xls'
    return f'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/{year}/delineation-files/list1.xls'


def _cbsa_shapefiles(year):
    if year < 2010:
        return None
    elif year == 2010:
        return 'https://www2.census.gov/geo/tiger/TIGER2010/CBSA/2010/tl_2010_us_cbsa10.zip'
    else:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/CBSA/tl_{year}_us_cbsa.zip'


def _metdiv_shapefiles(year):
    if year < 2010:
        return None
    elif year == 2010:
        return 'https://www2.census.gov/geo/tiger/TIGER2010/METDIV/2010/tl_2010_us_metdiv10.zip'
    else:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/METDIV/tl_{year}_us_metdiv.zip'


def _csa_shapefiles(year):
    if year < 2010:
        return None
    elif year == 2010:
        return 'https://www2.census.gov/geo/tiger/TIGER2010/CSA/2010/tl_2010_us_csa10.zip'
    else:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/CSA/tl_{year}_us_csa.zip'


CBSAFiles = namedtuple('CBSAFiles',
                       ['cbsa_delineation', 'cbsa_shape', 'metdiv_shape', 'csa_shape'])
download_files = download_to_cls(CBSAFiles,
                                 _cbsa_delineation_files,
                                 _cbsa_shapefiles,
                                 _metdiv_shapefiles,
                                 _csa_shapefiles)
