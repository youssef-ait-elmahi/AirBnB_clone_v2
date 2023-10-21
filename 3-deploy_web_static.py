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

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)

    # Use the tar command to create a .tgz archive of the web_static directory
    result = local("tar -cvzf {} web_static".format(filename))

    # If the command was successful, return the name of the file.
    # Otherwise, return None.
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    # Check if the file at the path archive_path doesn’t exist
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Get the filename without the .tgz extension
        filename = archive_path.split("/")[-1][:-4]

        # Create the directory to uncompress the archive if it doesn't exist
        run("mkdir -p /data/web_static/releases/{}/".format(filename))

        # Uncompress the archive to the folder on the web server
        run("tar -xzf /tmp/{}.tgz -C /data/\
            web_static/releases/{}/".format(filename, filename))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(filename))

        # Move the files to the right place
        run("mv /data/web_static/releases/{}/web_static/* /data/\
            web_static/releases/{}/".format(filename, filename))

        # Remove the now empty folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link on the web server
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
