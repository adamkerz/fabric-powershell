from . import Powershell


def configureScheduledTask(hostname,folder,name,command,arguments,workingDir,username,password,scheduledTaskTriggerArguments):
    with Powershell(hostname) as ps:
        ps('$action = New-ScheduledTaskAction -Execute "%s" -Argument "%s" -WorkingDirectory "%s"'%(command,arguments,workingDir))
        ps('$trigger = New-ScheduledTaskTrigger %s'%(scheduledTaskTriggerArguments,))
        ps('$settingsSet = New-ScheduledTaskSettingsSet -Compatibility Win8')

        ps('$task = Get-ScheduledTask -ErrorAction Ignore -TaskPath "%s" -TaskName "%s"'%(folder,name))
        ps('''If($task -ne $Null){
            $task.Actions = $action
            $task.Triggers = $trigger
            $task.Settings = $settingsSet
            Set-ScheduledTask -InputObject $task -User "%s" -Password "%s"
        }Else{
            Register-ScheduledTask -TaskPath "%s" -TaskName "%s" -User "%s" -Password "%s" -Action $action -Trigger $trigger -Settings $settingsSet
        }'''%(username,password,folder,name,username,password))


def enableScheduledTask(hostname,folder,name):
    with Powershell(hostname) as ps:
        ps('Enable-ScheduledTask -ErrorAction Ignore -TaskPath "%s" -TaskName "%s"'%(folder,name))


def disableScheduledTask(hostname,folder,name):
    with Powershell(hostname) as ps:
        ps('Disable-ScheduledTask -ErrorAction Ignore -TaskPath "%s" -TaskName "%s"'%(folder,name))


def startScheduledTask(hostname,folder,name):
    with Powershell(hostname) as ps:
        ps('Start-ScheduledTask -TaskPath "%s" -TaskName "%s"'%(folder,name))
