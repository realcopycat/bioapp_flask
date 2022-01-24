from file_system_uploader import FilesystemUploader
from qiniu_uploader import QiniuUploader
from upyun_uploader import UpyunUploader
from flask import current_app

uploader: dict = {
    "filesystem": FilesystemUploader,
    "qiniu": QiniuUploader,
    'upyun': UpyunUploader
}


def get_uploader():
    return uploader.get(current_app.config.get("UPLOAD_PROVIDER") or "filesystem")()
