from collections import namedtuple
from usgeo.iops.download import download_us_tiger_pattern, download_to_cls


def _anrc_shapefile(year):
    if year == 2010:
        return f'https://www2.census.gov/geo/tiger/TIGER2010/ANRC/2010/tl_2010_02_anrc10.zip'
    elif year < 2011:
        return None
    else:
        return f'https://www2.census.gov/geo/tiger/TIGER{year}/ANRC/tl_{year}_02_anrc.zip'


_aiannh_shapefile = download_us_tiger_pattern('aiannh')
_aitsn_shapefile = download_us_tiger_pattern('aitsn')
_ttrack_shapefile = download_us_tiger_pattern('ttract')
_tbg_shapefile = download_us_tiger_pattern('tbg')
AIANNHShapes = namedtuple('AIANNHShapes', ['aiannh', 'anrc', 'aitsn', 'ttract', 'tbg'])
download_files = download_to_cls(
    AIANNHShapes, _aiannh_shapefile, _anrc_shapefile, _aitsn_shapefile, _ttrack_shapefile, _tbg_shapefile)
