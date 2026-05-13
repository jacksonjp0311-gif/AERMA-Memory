# AERMA RCC drift check placeholder
# This script currently reports manual-review mode.
# Future version should validate RCC001-RCC020 style rules.

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $Root

Write-Host "AERMA RCC drift check: manual-review mode"
Write-Host "Required files:"

$Required = @(
    "README.md",
    "docs/context/repository_context_index.json",
    "docs/context/module_index.md",
    "docs/context/validation_surface.md",
    "docs/context/context_budget.md",
    "docs/context/drift_report.md",
    "docs/context/llm_reconstruction_prompt.md",
    "src/README.md",
    "src/aerma/README.md",
    "src/aerma/core/README.md",
    "src/aerma/benchmarks/README.md",
    "src/aerma/evidence/README.md",
    "tasks/README.md",
    "tests/README.md"
)

$Missing = @()

foreach ($Path in $Required) {
    if (!(Test-Path $Path)) {
        $Missing += $Path
        Write-Host "[MISSING] $Path"
    } else {
        Write-Host "[OK] $Path"
    }
}

if ($Missing.Count -gt 0) {
    throw "RCC drift check failed: missing required RCC files."
}

Write-Host "RCC drift check complete: required RCC files present."
