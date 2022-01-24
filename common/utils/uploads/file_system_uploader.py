import os
import posixpath
from pathlib import PurePath
from shutil import copyfileobj, rmtree

from PIL.features import codecs
from flask import current_app, send_file
from werkzeug.utils import safe_join, secure_filename

from common.utils.uploads.base_uploader import BaseUploader


def hexencode(s):
    if isinstance(s, (str,)):
        s = s.encode("utf-8")
    encoded = codecs.encode(s, "hex")
    try:
        encoded = encoded.decode("utf-8")
    except UnicodeDecodeError:
        pass
    return encoded


class FilesystemUploader(BaseUploader):
    def __init__(self, base_path=None):
        super(BaseUploader, self).__init__()
        self.base_path = base_path or current_app.config.get("UPLOAD_FOLDER")

    def store(self, fileobj, filename):
        location = os.path.join(self.base_path, filename)
        directory = os.path.dirname(location)

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(location, "wb") as dst:
            copyfileobj(fileobj, dst, 16384)

        return filename

    def upload(self, file_obj, filename):
        if len(filename) == 0:
            raise Exception("Empty filenames cannot be used")

        filename = secure_filename(filename)
        md5hash = hexencode(os.urandom(16))
        file_path = posixpath.join(md5hash, filename)

        return self.store(file_obj, file_path)

    def download(self, filename):
        return send_file(safe_join(self.base_path, filename), as_attachment=True)

    def delete(self, filename):
        if os.path.exists(os.path.join(self.base_path, filename)):
            file_path = PurePath(filename).parts[0]
            rmtree(os.path.join(self.base_path, file_path))
            return True
        return False

    def sync(self):
        pass
