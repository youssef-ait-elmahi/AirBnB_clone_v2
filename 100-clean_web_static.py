from fabric.api import env, local, run
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['52.91.147.26', '100.25.188.140']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """

    number = int(number)

    # Keep at least one version if number <= 1
    if number <= 1:
        number = 2
    else:
        number += 1

    # Delete the files that are not the most recent ones (local)
    local('ls -dt versions/* | tail -n +{} | xargs rm -rf --'.format(number))

    # Delete the files that are not the most recent ones (remote)
    run('ls -dt /data/web_static/\
        releases/* | tail -n +{} | xargs rm -rf --'.format(number))
