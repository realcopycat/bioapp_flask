from qiniu import Auth, put_data
from base_uploader import BaseUploader

access_key = '自己账号的access key'

secret_key = '自己账号的secret key'

bucket_name = '空间名'


class QiniuUploader(BaseUploader):

    def __init__(self):
        raise NotImplementedError

    def store(self, fileobj, filename):
        raise NotImplementedError

    def upload(self, file_obj, filename):

        token = Auth(access_key=access_key, secret_key=secret_key).upload_token(bucket=bucket_name)
        ret, res = put_data(token, None, data=file_obj)
        ret.get('key')
        print(ret)
        print(res)

        if res.status_code != 200:
            raise Exception("upload failed")
        return ret, res

    def download(self, filename):
        raise NotImplementedError

    def delete(self, filename):
        raise NotImplementedError

    def sync(self):
        raise NotImplementedError
