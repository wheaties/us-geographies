from iops.download import download_to_list


def _ua_shapes(year):
    if year == 2010:
        return ['https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_60_uac10.zip',
                'https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_66_uac10.zip',
                'https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_69_uac10.zip',
                'https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_72_uac10.zip',
                'https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_78_uac10.zip',
                'https://www2.census.gov/geo/tiger/TIGER2010/UA/2010/tl_2010_us_uac10.zip']
    elif year < 2012:
        return []
    else:
        return [f'https://www2.census.gov/geo/tiger/TIGER{year}/UAC/tl_{year}_us_uac10.zip']


download_files = download_to_list(_ua_shapes)
