from fabric.api import env, put, run
from os.path import exists

env.hosts = ['52.91.147.26', '100.25.188.140']


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
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
            filename, filename))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(filename))

        # Move the files to the right place
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/\
            releases/{}/".format(filename, filename))

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
