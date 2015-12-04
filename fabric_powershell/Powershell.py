import base64
import shutil

from fabric.api import *
from fabric.utils import puts


class Powershell(object):
    def __init__(self,hostname=None):
        self.hostname=hostname
        self.commands=[]


    # allow the instance to be called to add to commands
    def __call__(self,cmd):
        self.commands.append(cmd)


    def execute(self):
        # build the command
        if self.hostname is None:
            cmd='\n'.join(self.commands)
        else:
            cmd='''\
$ErrorActionPreference="Stop"
$s=New-PSSession -ComputerName %s

Invoke-Command -Session $s -ScriptBlock {
%s
}
    '''%(self.hostname,'\n'.join(['    '+c for c in self.commands]))

        # and run it
        puts('Executing powershell code:\n'+cmd)
        s=base64.b64encode(cmd.encode('utf-16le'))
        local('powershell -EncodedCommand {}'.format(s))


    @classmethod
    def put(cls,srcPath,destPath):
        """Convenience method to upload files - TODO: (if possible) currently not tied to the hostname parameter."""
        shutil.copy(srcPath,destPath)


    # make this a context manager
    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is None:
            self.execute()
        else:
            puts('An error occurred, not running powershell commands')
