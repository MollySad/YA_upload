import requests,os

from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_path = os.path.normpath(file_path)
        HEADERS = {"Authorization" : f'OAuth {self.token}'}
        FILES = {"file" : open(file_path, 'rb')}

        res_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        res = requests.get(res_url, params={'path': file_path}, headers=HEADERS)

        url = res.json().get('href')
        resp = requests.put(url, files=FILES, headers={})

        return print(resp.status_code)
    

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '12/коды.txt'
    
    uploader = YaUploader(token="***")
    result = uploader.upload(path_to_file)

    