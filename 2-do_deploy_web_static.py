#!/usr/bin/python3
"""Script to deploy web static"""
from fabric.api import *
from os.path import exists, splitext


env.hosts = ["52.91.147.26", "100.25.188.140"]


@task
def do_deploy(archive_path):
    """ Function that deply archive"""

    # Checking if path exists
    if not exists(archive_path):
        return False
    # Spliting the files
    arch_name = archive_path.split('/')[1]
    file_name = splitext(arch_name)[0]
    tmp_path = "/tmp/{}".format(arch_name)
    data_path = "/data/web_static/releases/{}".format(file_name)
    # Fabric commands
    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(data_path))
    run('tar -xzf {}  -C {}'.format(tmp_path, data_path))
    run('rm {}'.format(tmp_path))
    run('mv {}/web_static/* {}/'.format(data_path, data_path))
    run('rm -rf {}/web_static'.format(data_path))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(data_path))
    print("New version deployed!")
    return True
