from collections import namedtuple
from fileops.download import LocalFileDownloader


# index out of range for 2013, header/footer offset different?
_necta_combined_files = {
    2013: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2013/delineation-files/list3.xls',
    2015: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2015/delineation-files/list3.xls',
    2017: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2017/delineation-files/list3.xls',
    2018: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list3_Sep_2018.xls',
    2020: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2020/delineation-files/list3_2020.xls'
}

_necta_cities_files = {
    2013: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2013/delineation-files/list4.xls',
    2015: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2015/delineation-files/list4.xls',
    2017: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2017/delineation-files/list4.xls',
    2018: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2018/delineation-files/list4_Sep_2018.xls',
    2020: 'https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2020/delineation-files/list4_2020.xls'
}

_necta_shape_files = {
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/CNECTA/tl_2013_us_cnecta.zip',
    2014: 'https://www2.census.gov/geo/tiger/TIGER2014/CNECTA/tl_2014_us_cnecta.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/CNECTA/tl_2015_us_cnecta.zip',
    2016: 'https://www2.census.gov/geo/tiger/TIGER2016/CNECTA/tl_2016_us_cnecta.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/CNECTA/tl_2017_us_cnecta.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/CNECTA/tl_2018_us_cnecta.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/CNECTA/tl_2019_us_cnecta.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/CNECTA/tl_2020_us_cnecta.zip',
    2021: 'https://www2.census.gov/geo/tiger/TIGER2021/CNECTA/tl_2021_us_cnecta.zip'
}


NECTAFiles = namedtuple('NECTAFiles', ['necta_combined', 'necta_cities', 'necta_shape'])


#ok, we've done this 3x so it's time to refactor
def download_files(year, root_folder=None):
    downloader = LocalFileDownloader(root_folder)

    def retrieve(url):
        return downloader(url, year) if url is not None else None

    return NECTAFiles(retrieve(_necta_combined_files.get(year)),
                      retrieve(_necta_cities_files.get(year)),
                      retrieve(_necta_shape_files.get(year)))
