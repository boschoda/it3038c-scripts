function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
    }
function getDate{
    (Get-Date).Date
    }

function getVersion{
    (Get-Host).Version
    }
function getUser{
    $env:USERNAME
    }

$IP = getIP
$USER = getUser
$DATE = getDate
$VERSION = getVersion

$BODY = "This machine's IP is $IP. User is $USER. The version is POWERSHELL $VERSION. Today's date is $DATE"

Write-Host($BODY)