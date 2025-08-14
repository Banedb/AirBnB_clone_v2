#!/usr/bin/python3


"""1-pack_web_static module"""
from fabric.api import env, put, run
import os

env.hosts = ["172.18.0.3", "172.18.0.2"]
env.user = "ubuntu"


def do_deploy(archive_path):
"""Deploys the .tgz archive to the web server."""
if not os.path.exists(archive_path):
return False
file_name = os.path.basename(archive_path)
folder_name = os.path.splitext(file_name)[0]
target_folder = f"/data/web_static/releases/{folder_name}"
run(f"mkdir -p /tmp/ {target_folder}")
r0 = put(archive_path, "/tmp/")
r1 = run(f"tar -xzf /tmp/{file_name} -C {target_folder}")
r2 = run(f"rm /tmp/{file_name}")
r3 = run(f"ln -sf /data/web_static/current {target_folder}")

if all([r.succeeded for r in [r0, r1, r2, r3]]):
return True
else:
return False
