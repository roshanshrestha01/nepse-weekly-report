import urllib3
import shutil


class HttpRequest:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get(self, url):
        return self.http.request('GET', url)

    def download(self, url, path):
        response = self.http.request('GET', url, preload_content=False)

        with open(path, 'wb') as out:
            shutil.copyfileobj(response, out)

        response.release_conn()