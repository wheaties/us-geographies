from collections import namedtuple
from usgeo.iops.download import download_to_cls, state_divided_paths


def _base(abbr):
    def shapefiles(year):
        if year < 2010:
            return None
        elif year == 2010:
            for state in state_divided_paths():
                yield f'https://www2.census.gov/geo/tiger/TIGER2010/{abbr.upper()}/2010/tl_2010_{state}_{abbr}10.zip'
        else:
            for state in state_divided_paths():
                yield f'https://www2.census.gov/geo/tiger/TIGER{year}/{abbr.upper()}/tl_{year}_{state}_{abbr}.zip'
    return shapefiles


_elementary_shapefiles = _base('elsd')
_secondary_shapefiles = _base('scsd')
_unified_shapefiles = _base('unsd')

School = namedtuple('School', ['elementary_shapes', 'secondary_shapes', 'unified_shapes'])

download_files = download_to_cls(School, _elementary_shapefiles, _secondary_shapefiles, _unified_shapefiles)
