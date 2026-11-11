$ErrorActionPreference = 'Stop'
$destination = Join-Path $env:LOCALAPPDATA 'TradingAutomation\provisioning'
if (-not (Test-Path -LiteralPath $destination -PathType Container)) {
    throw 'Existing provisioning directory required.'
}
$files = @('ssh_acg_policy.py', 'ncloud_ssh_backend.py', 'connect_developer.py', 'connect-developer.ps1')
$stamp = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff') + '-' + [Guid]::NewGuid().ToString('N')
foreach ($file in $files) {
    $source = Join-Path $PSScriptRoot $file
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw 'Installation source missing.' }
}
foreach ($file in $files) {
    $source = Join-Path $PSScriptRoot $file
    $target = Join-Path $destination $file
    if (Test-Path -LiteralPath $target) {
        Copy-Item -LiteralPath $target -Destination ($target + '.' + $stamp + '.bak') -ErrorAction Stop
    }
    Copy-Item -LiteralPath $source -Destination $target -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $source).Hash -ne (Get-FileHash -LiteralPath $target).Hash) {
        throw 'Installed content verification failed.'
    }
}
Write-Output 'Installed local SSH helper. Original files backed up; private state and credentials unchanged.'
