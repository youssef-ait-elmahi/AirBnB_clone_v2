#!/usr/bin/python3
"""Script that creates and distributes an archive to your web servers"""
from fabric.api import env, put, run, local
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['52.91.147.26', '100.25.188.140']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf {} web_static".format(filename))

    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        filename = archive_path.split("/")[-1][:-4]

        run("mkdir -p /data/web_static/releases/{}/".format(filename))

        run("tar -xzf /tmp/{}.tgz -C /data/\
            web_static/releases/{}/".format(filename, filename))

        run("rm /tmp/{}.tgz".format(filename))

        # Move the files to the right place
        run("mv /data/web_static/releases/{}/web_static/* /data/\
            web_static/releases/{}/".format(filename, filename))

        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/\
            web_static/current".format(filename))

        return True

    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers
    """

    path = do_pack()

    if path is None:
        return False

    return do_deploy(path)
