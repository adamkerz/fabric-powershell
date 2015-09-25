import base64

from fabric.api import *


def runPowershell(command):
    s=base64.b64encode(command.encode('utf-16le'))
    local('powershell -EncodedCommand {}'.format(s))
