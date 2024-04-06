#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
"""
Pack web static
"""


def do_pack():
    """
    compressing data
    """

    local("mkdir -p versions")
    time_now = datetime.now()
    time = time_now.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)

    final = local("tar -cvzf {} web_static".format(file_name))

    if final.failed:
        return None
    else:
        return file_name
