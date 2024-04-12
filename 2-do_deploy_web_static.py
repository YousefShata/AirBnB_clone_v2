#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
"""
Pack web static
"""


env.hosts = ['54.146.89.31', '100.25.0.160']


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


def do_deploy(archive_path):
    """
    Deploy data
    """

    if archive_path is None:
        return False

    try:
        filename = archive_path.split("/")[-1]
        folder_name = filename.split(".")[0]
        full_path = "/data/web_static/releases/{}/".format(folder_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(full_path))
        run("tar -xzf /tmp/{} -C {}".format(filename, full_path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(full_path, full_path))
        run("rm -rf {}web_static".format(full_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(full_path))
        return True
    except Exception as e:
        return False
