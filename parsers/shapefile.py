import json
import shapefile


def _sub_none_for_empty(value):
    if isinstance(value, str):
        return value if len(value) else None
    return value


def parse_file(filepath):
    output = []
    try:
        # shapefile.Reader says it can handle os.FileLike but can't do PathLib objects. :(
        sf = shapefile.Reader(str(filepath))
        # raise Exception(sf.fields)
        for shp in sf.iterShapeRecords():
            value = [_sub_none_for_empty(v) for v in shp.record]
            value.append(json.dumps(shp.shape.__geo_interface__))
            output.append(value)
    except shapefile.ShapefileException as ex:
        print(f'shapefile {filepath} error: {ex}')
    return output
