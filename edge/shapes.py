from iops.database import ShapeDataTable
from iops.metadata import single_file_load
from parsers.shapefile import parse_file


edge_locale = ShapeDataTable('edge_locale')
edge_locale.columns =[]

# There is no .dbf file to reference...
load_file = single_file_load(edge_locale, parse_file)