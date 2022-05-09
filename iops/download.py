from itertools import chain
import os
import requests
from pathlib import Path


# Assumes that the file name is part of the URL path...
class LocalFileDownloader:
    def __init__(self, target_directory=None):
        self.target_directory = target_directory or Path.cwd()
        self.path = Path(self.target_directory)
        self.path.mkdir(parents=True, exist_ok=True)

    def __call__(self, file_url, file_folder=None, force=False):
        return self.download(file_url, file_folder, force)

    def download(self, file_url, file_folder=None, force=False):
        filepath = Path(self._destination(file_url, file_folder))
        self._create_if_not_exists(filepath)
        if force or not filepath.exists():
            self._download_and_save(file_url, filepath)

        return filepath

    def _destination(self, file_url, file_folder=None):
        file_name = file_url.split("/")[-1]
        if file_folder:
            return f'{self.target_directory}{os.sep}{file_folder}{os.sep}{file_name}'
        else:
            return f'{self.target_directory}{os.sep}{file_name}'

    def _create_if_not_exists(self, filepath):
        if not filepath.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)

    def _download_and_save(self, file_url, filepath):
        response = requests.get(file_url)
        response.raise_for_status()
        with filepath.open('wb') as f:
            f.write(response.content)


def download_to_cls(cls, *lookup):
    def download_files(year, root_folder=None, force=False):
        downloader = LocalFileDownloader(root_folder)
        args = []
        for fn in lookup:
            result = fn(year)
            if isinstance(result, str):
                args.append(downloader(result, year, force) if result is not None else None)
            else:
                args.append([downloader(url, year, force) for url in result])

        return cls(*args)
    return download_files


def download_to_file(lookup):
    def download_file(year, root_folder=None, force=False):
        downloader = LocalFileDownloader(root_folder)
        url = lookup(year)

        return downloader(url, year, force) if url is not None else None
    return download_file


def download_to_list(lookup):
    def download_files(year, root_folder=None, force=False):
        downloader = LocalFileDownloader(root_folder)

        return [downloader(url, year, force) for url in lookup(year)]
    return download_files


def state_divided_paths():
    states = chain([1, 2, 4, 5, 6],
                   range(8, 14),  # 8-13
                   range(15, 43),  # 15-42
                   range(44, 52),  # 44-51
                   [54, 55, 56, 66, 72, 78])
    for state in states:
        if state < 10:
            state = f'0{state}'
        yield state


def download_us_tiger_pattern(abbr, cutoff=2011):
    def download_file(year):
        if year == 2010:
            return f'https://www2.census.gov/geo/tiger/TIGER2010/{abbr.upper()}/2010/tl_2010_us_{abbr}10.zip'
        elif year < cutoff:
            return None
        else:
            return f'https://www2.census.gov/geo/tiger/TIGER{year}/{abbr.upper()}/tl_{year}_us_{abbr}.zip'
    return download_file
