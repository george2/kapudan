import warnings
import functools
import re
import os


class Daemon(object):
    _matcher = re.compile("(en|dis)abled")

    def __init__(self, name=None):
        if name is None:
            warnings.warn("Using  Daemon this way is deprecated")
        self.name = name
        self.has_changed = False

    def isEnabled(self, name):
        if self.name:
            raise Warning("Using the old API, but name is not None! Aborting")
        self.name = name
        result = self.is_enabled()
        self.name = None
        return result

    def isInstalled(self, name):
        if self.name:
            raise Warning("Using the old API, but name is not None! Aborting")
        self.name = name
        result = self.is_installed()
        self.name = None
        return result

    def is_enabled(self):
        result = os.popen("systemctl show --property=UnitFileState %s" % self.name)
        match = re.search(Daemon._matcher, result.read())
        result.close()
        if match:
            return "enabled" == match.group()
        return False

    def is_installed(self):
        result = os.path.exists("/usr/lib/systemd/system/%s.service" % self.name)
        return result
