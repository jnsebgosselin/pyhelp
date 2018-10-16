# -*- coding: utf-8 -*-

# Copyright © PyHelp Project Contributors
# https://github.com/jnsebgosselin/pyhelp
#
# This file is part of PyHelp.
# Licensed under the terms of the GNU General Public License.

import os

version_info = (0, 1, 0, 'dev')
__version__ = '.'.join(map(str, version_info))
__appname__ = 'PyHelp'
__namever__ = __appname__ + " " + __version__
__date__ = '29/01/2018'
__project_url__ = "https://github.com/jnsebgosselin/pyhelp"
__releases_url__ = __project_url__ + "/releases"
__releases_api__ = "https://api.github.com/repos/jnsebgosselin/pyhelp/releases"

__rootdir__ = os.path.dirname(os.path.realpath(__file__))


from pyhelp.managers import NetCDFMeteoManager, HelpManager
