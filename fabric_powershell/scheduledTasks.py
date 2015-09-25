from . import runPowershell


def configureScheduledTask(hostname,folder,name,command,arguments,workingDir,username,password,scheduledTaskTriggerArguments):
    runPowershell('''\
$ErrorActionPreference="Stop"
$s=New-PSSession -ComputerName %s

Invoke-Command -Session $s -ScriptBlock {
    $action = New-ScheduledTaskAction -Execute "%s" -Argument "%s" -WorkingDirectory "%s"
    $trigger = New-ScheduledTaskTrigger %s
    $settingsSet = New-ScheduledTaskSettingsSet -Compatibility Win8

    $task = Get-ScheduledTask -ErrorAction Ignore -TaskPath "%s" -TaskName "%s"
    If($task -ne $Null){
        $task.Actions = $action
        $task.Triggers = $trigger
        $task.Settings = $settingsSet
        Set-ScheduledTask -InputObject $task -User "%s" -Password "%s"
    }Else{
        Register-ScheduledTask -TaskPath "%s" -TaskName "%s" -User "%s" -Password "%s" -Action $action -Trigger $trigger -Settings $settingsSet
    }
}
'''%(hostname,
     command,arguments,workingDir,
     scheduledTaskTriggerArguments,
     folder,name,
     username,password,
     folder,name,username,password))
