from collections import namedtuple
from fileops.download import LocalFileDownloader


gnis_url = {
    2010: 'https://geonames.usgs.gov/docs/federalcodes/NationalFedCodes.zip'
}

_fips_state = {
    2013: 'https://www2.census.gov/programs-surveys/popest/geographies/2013/state-geocodes-v2013.xls',
    2014: 'https://www2.census.gov/programs-surveys/popest/geographies/2014/state-geocodes-v2014.xls',
    2015: 'https://www2.census.gov/programs-surveys/popest/geographies/2015/state-geocodes-v2015.xls',
    2016: 'https://www2.census.gov/programs-surveys/popest/geographies/2016/state-geocodes-v2016.xls',
    2017: 'https://www2.census.gov/programs-surveys/popest/geographies/2017/state-geocodes-v2017.xlsx',
    2018: 'https://www2.census.gov/programs-surveys/popest/geographies/2018/state-geocodes-v2018.xlsx',
    2019: 'https://www2.census.gov/programs-surveys/popest/geographies/2019/state-geocodes-v2019.xlsx',
    2020: 'https://www2.census.gov/programs-surveys/popest/geographies/2020/state-geocodes-v2020.xlsx'
}

_fips_all = {
    2013: 'https://www2.census.gov/programs-surveys/popest/geographies/2013/all-geocodes-v2013.xls',
    2014: 'https://www2.census.gov/programs-surveys/popest/geographies/2014/all-geocodes-v2014.xls',
    2015: 'https://www2.census.gov/programs-surveys/popest/geographies/2015/all-geocodes-v2015.xlsx',
    2016: 'https://www2.census.gov/programs-surveys/popest/geographies/2016/all-geocodes-v2016.xlsx',
    2017: 'https://www2.census.gov/programs-surveys/popest/geographies/2017/all-geocodes-v2017.xlsx',
    2018: 'https://www2.census.gov/programs-surveys/popest/geographies/2018/all-geocodes-v2018.xlsx',
    2019: 'https://www2.census.gov/programs-surveys/popest/geographies/2019/all-geocodes-v2019.xlsx',
    2020: 'https://www2.census.gov/programs-surveys/popest/geographies/2020/all-geocodes-v2020.xlsx'
}

#holy smokes, shape files...
#https://www2.census.gov/geo/tiger/GENZ2020/shp/
#how to read the name of the shapefile: https://www.census.gov/programs-surveys/geography/technical-documentation/naming-convention/cartographic-boundary-file.html


FIPSFiles = namedtuple('FIPSFiles', ['state_geocodes', 'all_geocodes'])


def download_files(year, root_folder=None):
    downloader = LocalFileDownloader(root_folder)

    def retrieve(url):
        return downloader(url, year) if url is not None else None

    return FIPSFiles(retrieve(_fips_state.get(year)), retrieve(_fips_all.get(year)))
