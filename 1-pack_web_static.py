#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """do pack"""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
