param(
    [switch]$DryRun,
    [switch]$VerifyOnly,
    [string]$Profile = 'ssh-acg'
)
$ErrorActionPreference = 'Stop'
$entry = Join-Path $PSScriptRoot 'connect_developer.py'
$options = @($entry, '--profile', $Profile)
if ($DryRun) { $options += '--dry-run' }
if ($VerifyOnly) { $options += '--verify-only' }
& python @options
if ($LASTEXITCODE -ne 0) { throw 'SSH preflight failed. Existing old rules were not intentionally removed before verification.' }
