"""自定义上传存储文件类、连接FDFS"""


from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client, get_tracker_conf

import socket

# Django默认保存文件时，会调用Storage类中的save方法
# Storage类中的save方法会调用DEFAULT_FILE_STORAGE配置项指定的类中_save方法
# _save方法的返回值最终会保存在表的image字段中

# Django保存文件之前，会调用DEFAULT_FILE_STORAGE配置项指定的类中exists方法
# 判断文件在系统中是否存在，防止同名的文件被覆盖


class FDFSStorage(Storage):
    """fast dfs文件存储类"""

    def __init__(self, option=None):
        if not option:
            self.option = settings.CUSTOM_STORAGE_OPTIONS
        else:
            self.option = option

    def _save(self, name, content):
        """
        在FastDFS中保存文件
        :param name: 传入的文件名
        :param content: 文件内容
        :return: 保存到数据库中的FastDFS的文件名
        """
        client_conf_obj = get_tracker_conf(self.option.get('CLIENT_CONF'))
        client = Fdfs_client(client_conf_obj)
        ret = client.upload_by_buffer(content.read())
        if ret.get("Status") != "Upload successed.":
            raise Exception("upload file failed")
        file_name = ret.get("Remote file_id")


        # file_name为bytes类型，只能返回str类型，不然会报错
        return self.option.get('BASE_URL') + file_name.decode()

    def exists(self, name):
        """判断文件是否存在"""
        return False

    def url(self, name):
        """返回可访问到文件的url地址"""
        return name
