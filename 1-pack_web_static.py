#!/usr/bin/python3
"""1-pack_web_static module"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the `web_static` folder."""
    now = datetime.now()
    file_path = f'versions/web_static_{now.strftime("%Y%m%d%H%M%S")}.tgz'
    r = local(f"mkdir -p versions && tar -czvf {file_path} web_static/")

    return file_path if r.succeeded else None


# Modern fabric
# from datetime import datetime
# from fabric import task


# @task
# def do_pack(c):
#     now = datetime.now()
#     file_path = f'versions/web_static_{now.strftime("%Y%m%d%H%M%S")}.tgz'
#     r = c.local(f"mkdir -p versions && tar -czvf {file_path} web_static/",
#                 warn=True)

#     return file_path if r.ok else None
