from base_uploader import BaseUploader


class UpyunUploader(BaseUploader):
    def __init__(self):
        raise NotImplementedError

    def store(self, fileobj, filename):
        raise NotImplementedError

    def upload(self, file_obj, filename):
        raise NotImplementedError

    def download(self, filename):
        raise NotImplementedError

    def delete(self, filename):
        raise NotImplementedError

    def sync(self):
        raise NotImplementedError
