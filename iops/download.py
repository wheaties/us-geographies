import os
import requests
from pathlib import Path


#Assumes that the file name is part of the URL path...
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
        for item in lookup:
            url = item.get(year)
            args.append(downloader(url, year, force) if url is not None else None)

        return cls(*args)
    return download_files

