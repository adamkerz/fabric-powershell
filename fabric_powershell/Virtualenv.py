
class Virtualenv(object):
    """A context manager that runs all commands within the specified virtualenv."""
    def __init__(self,venvPath,powershell):
        self.venvPath=venvPath
        self.powershell=powershell


    # allow the instance to be called to add to commands
    def __call__(self,cmd):
        self.powershell(r'cmd /c "{}\Scripts\activate.bat && {}"'.format(self.venvPath,cmd))


    # make this a context manager
    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        # the surrounding powershell context manager does the execution
        pass
