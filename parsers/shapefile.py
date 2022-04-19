import json
import shapefile
from itertools import chain


def _sub_none_for_empty(value):
    if isinstance(value, str):
        return value if len(value) else None
    return value


def parse_file(filepath, cls=list):
    output = []
    # shapefile.Reader says it can handle os.FileLike but can't do PathLib objects. :(
    sf = shapefile.Reader(str(filepath))
    for shp in sf.iterShapeRecords():
        geom = json.dumps(shp.shape.__geo_interface__)
        value = cls(chain((_sub_none_for_empty(v) for v in shp.record), [geom]))
        output.append(value)
    return output
