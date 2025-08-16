#!/usr/bin/python3
"""100-clean_web_static module"""
from fabric.api import env, local, run

env.hosts = ["3.85.20.10", "107.23.44.113"]
env.user = "ubuntu"


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number(int): Number of archives to keep.
    """
    keep = 2 if int(number) == 0 else int(number) + 1

    local(
        f'ls -1t versions | grep "^web_static_" | tail -n +{keep} | '
        'xargs -I ar rm -f versions/ar'
    )
    run(
        'ls -1t /data/web_static/releases | grep "^web_static_" | '
        f'tail -n +{keep} | xargs -I ar rm -rf /data/web_static/releases/ar'
    )
