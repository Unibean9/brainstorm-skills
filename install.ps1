[CmdletBinding()]
param(
    [ValidateSet('all', 'brainstorming', 'prd', 'frontend-design')]
    [string]$Skill = 'all'
)

$ErrorActionPreference = 'Stop'

$repoRoot = $PSScriptRoot
$npxCommand = Get-Command npx -ErrorAction SilentlyContinue

if (-not $npxCommand) {
    throw "Node.js/npm is required. Install Node.js, then run this script again."
}

$arguments = @('skills', 'add', $repoRoot)
if ($Skill -ne 'all') {
    $arguments += @('--skill', $Skill)
}

Write-Host "Installing $Skill skill set from $repoRoot ..."
& $npxCommand.Path @arguments
if ($LASTEXITCODE -ne 0) {
    throw "skills CLI exited with code $LASTEXITCODE."
}

Write-Host 'Installation completed.'
