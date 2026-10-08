param([string]$Repo = "")
$ErrorActionPreference = "Stop"
Write-Host "Validating local repository..." -ForegroundColor Green
python automation/validate_repository.py
if ($Repo) {
  Write-Host "Creating labels in $Repo..." -ForegroundColor Green
  $labels = Get-Content .github/labels.yml -Raw
  Write-Host "Install GitHub CLI and create labels from .github/labels.yml, or use a label-sync action." -ForegroundColor Yellow
}
Write-Host "Ready. Create a GitHub repository and push this folder." -ForegroundColor Green
