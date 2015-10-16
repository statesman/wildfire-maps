import time
import requests

INTERVAL = 1 * 900
FILE_URL = 'http://activefiremaps.fs.fed.us/data_viirs_iband/kml/conus_hist/conus_20151019.kmz'
DESTINATION_FOLDER = 'viirs-19'

def download_file():
    r = requests.get(FILE_URL)
    if r.status_code == 200:
        file_name = '%s/%s.kml' % (DESTINATION_FOLDER, int(time.time()))
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print('[%s] - Saved updated map to %s.' % (int(time.time()),
                                                   file_name))
    else:
        print('[%s] - %s error downloading the file.' % (
            int(time.time()),
            r.status_code)
        )

if __name__ == "__main__":
    download_file()
    while True:
        print('[%s] - Sleeping for %s minutes' % (
            int(time.time()),
            INTERVAL // 60)
        )
        time.sleep(INTERVAL)
        download_file()