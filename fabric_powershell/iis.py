from . import Powershell


def createAppPool(hostname,name):
    with Powershell(hostname) as ps:
        ps('Import-Module WebAdministration')
        ps(r'cd IIS:\AppPools')
        ps(r'if (!(Test-Path "%s" -pathType container)){'%name)
        ps(r'    $appPool=New-Item "%s"'%name)
        ps(r'    $appPool | Set-ItemProperty -Name "managedRuntimeVersion" -Value "v4.0"')
        ps('}')


def createApplication(hostname,siteName,name,path,appPoolName):
    with Powershell(hostname) as ps:
        ps('Import-Module WebAdministration')
        ps(r'cd "IIS:\Sites\%s"'%siteName)
        ps(r'if (!(Test-Path "%s" -pathType container)){'%name)
        ps(r'    New-Item "%s" -type Application -physicalPath "%s"'%(name,path))
        ps(r'    Set-ItemProperty "%s" -name applicationPool -value "%s"'%(name,appPoolName))
        ps('}')


def createVirtualDirectory(hostname,siteName,name,path):
    with Powershell(hostname) as ps:
        ps('Import-Module WebAdministration')
        ps(r'cd "IIS:\Sites\%s"'%siteName)
        ps(r'if (!(Test-Path "%s" -pathType container)){'%name)
        ps(r'    New-Item "%s" -type VirtualDirectory -physicalPath "%s"'%(name,path))
        ps('}')
