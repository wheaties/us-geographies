from collections import namedtuple
from fileops.download import LocalFileDownloader


# TODO: issue with 2013!
_cbsa_delineation_files = {
    2013: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2013/delineation-files/list1.xls',
    2015: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2015/delineation-files/list1.xls',
    2017: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2017/delineation-files/list1.xls',
    2018: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list1_Sep_2018.xls',
    2020: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2020/delineation-files/list1_2020.xls',
}

_cbsa_shapefiles = {
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/CBSA/tl_2013_us_cbsa.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/CBSA/tl_2015_us_cbsa.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/CBSA/tl_2017_us_cbsa.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/CBSA/tl_2018_us_cbsa.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/CBSA/tl_2019_us_cbsa.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/CBSA/tl_2020_us_cbsa.zip'
}

_csa_shapefiles = {
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/CSA/tl_2013_us_csa.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/CSA/tl_2015_us_csa.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/CSA/tl_2017_us_csa.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/CSA/tl_2018_us_csa.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/CSA/tl_2019_us_csa.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/CSA/tl_2020_us_csa.zip'
}


CBSAFiles = namedtuple('CBSAFiles', ['cbsa_delineation', 'cbsa_shape', 'csa_shape'])


def download_files(year, root_folder=None):
    downloader = LocalFileDownloader(root_folder)

    def retrieve(url):
        return downloader(url, year) if url is not None else None

    return CBSAFiles(retrieve(_cbsa_delineation_files.get(year)),
                    retrieve(_cbsa_shapefiles.get(year)),
                    retrieve(_csa_shapefiles.get(year)))
