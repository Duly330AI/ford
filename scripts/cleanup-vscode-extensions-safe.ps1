# FORD Extension Cleanup Script (CORRECTED - Codex SAFE!)
# Removes 18 unnecessary extensions (NOT Codex!)
# Run this in PowerShell

Write-Host "`n🧹 FORD Extension Cleanup (Codex-Safe Version)" -ForegroundColor Cyan
Write-Host "This will remove 16 unnecessary extensions (NOT Codex!)`n" -ForegroundColor Yellow

$toRemove = @(
    # Web Development (4 remaining - 5 already removed)
    "wix.vscode-import-cost",
    "ms-edgedevtools.vscode-edge-devtools",
    "ms-playwright.playwright",
    "ms-vscode.vscode-typescript-next",

    # Database (6)
    "ms-mssql.data-workspace-vscode",
    "ms-mssql.mssql",
    "ms-mssql.sql-bindings-vscode",
    "ms-mssql.sql-database-projects-vscode",
    "mtxr.sqltools",
    "qwtel.sqlite-viewer",

    # Containers (4)
    "ms-azuretools.vscode-containers",
    "ms-azuretools.vscode-docker",
    "ms-vscode-remote.remote-containers",
    "p1c2u.docker-compose",

    # Azure/Remote (1) - CODESPACES, NOT CODEX!
    "github.codespaces",

    # Redundant (2) - NOTE: openai.chatgpt is CODEX, DO NOT REMOVE!
    "streetsidesoftware.code-spell-checker",
    "streetsidesoftware.code-spell-checker-german"
)

Write-Host "⚠️  NOTE: Codex (openai.chatgpt) is SAFE and NOT in removal list!`n" -ForegroundColor Green

$count = 0
foreach ($ext in $toRemove) {
    $count++
    Write-Host "[$count/$($toRemove.Count)] Removing $ext..." -ForegroundColor Yellow
    code --uninstall-extension $ext 2>&1 | Out-Null
    Start-Sleep -Milliseconds 500
}

Write-Host "`n✅ Cleanup Complete!" -ForegroundColor Green
Write-Host "`n📊 Final Status:" -ForegroundColor Cyan
$remaining = (code --list-extensions | Measure-Object).Count
Write-Host "  Extensions Remaining: $remaining" -ForegroundColor White
Write-Host "  Expected: 37 (includes Codex)" -ForegroundColor Gray

Write-Host "`n💡 Verify Codex is still there:" -ForegroundColor Yellow
Write-Host "  code --list-extensions | Select-String -Pattern 'openai.chatgpt'" -ForegroundColor White
$codex = code --list-extensions | Select-String -Pattern "openai.chatgpt"
if ($codex) {
    Write-Host "  ✅ Codex found: $codex`n" -ForegroundColor Green
} else {
    Write-Host "  ❌ Codex MISSING! Re-install: code --install-extension openai.chatgpt`n" -ForegroundColor Red
}
