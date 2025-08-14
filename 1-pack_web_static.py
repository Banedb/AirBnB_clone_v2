#!/usr/bin/python3
"""1-pack_web_static module"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the `web_static` folder."""
    now = datetime.now()
    tar = f'web_static_{now.strftime("%Y%m%d%H%M%S")}.tgz'
    r = local(f"mkdir -p versions && tar -czvf versions/{tar} web_static/",
              warn=True)

    return tar if r.succeeded else None


# Modern fabric
# from datetime import datetime
# from fabric import task


# @task
# def do_pack(c):
#     now = datetime.now()
#     tar = f'web_static_{now.strftime("%Y%m%d%H%M%S")}.tgz'
#     r = c.local(f"mkdir -p versions && tar -czvf versions/{tar} web_static/",
#                 warn=True)

#     return tar if r.ok else None
