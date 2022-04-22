from fileops.download import LocalFileDownloader

_cd_shapefiles ={
    2012: 'https://www2.census.gov/geo/tiger/TIGER2012/CD/tl_2012_us_cd112.zip',
    2013: 'https://www2.census.gov/geo/tiger/TIGER2013/CD/tl_2013_us_cd113.zip',
    2014: 'https://www2.census.gov/geo/tiger/TIGER2014/CD/tl_2014_us_cd114.zip',
    2015: 'https://www2.census.gov/geo/tiger/TIGER2015/CD/tl_2015_us_cd114.zip',
    2016: 'https://www2.census.gov/geo/tiger/TIGER2016/CD/tl_2016_us_cd115.zip',
    2017: 'https://www2.census.gov/geo/tiger/TIGER2017/CD/tl_2017_us_cd115.zip',
    2018: 'https://www2.census.gov/geo/tiger/TIGER2018/CD/tl_2018_us_cd116.zip',
    2019: 'https://www2.census.gov/geo/tiger/TIGER2019/CD/tl_2019_us_cd116.zip',
    2020: 'https://www2.census.gov/geo/tiger/TIGER2020/CD/tl_2020_us_cd116.zip',
    2021: 'https://www2.census.gov/geo/tiger/TIGER2021/CD/tl_2021_us_cd116.zip'
}


def download_files(year, root_folder=None):
    downloader = LocalFileDownloader(root_folder)
    url = _cd_shapefiles.get(year)

    return downloader(url, year) if url is not None else None
