# FORD Extension Cleanup Script
# Removes 23 unnecessary extensions
# Run this in PowerShell

Write-Host "`n🧹 Starting FORD Extension Cleanup..." -ForegroundColor Cyan
Write-Host "This will remove 23 unnecessary extensions (59 -> 36)`n" -ForegroundColor Yellow

$toRemove = @(
    # Web Development (9)
    "bradlc.vscode-tailwindcss",
    "ecmel.vscode-html-css",
    "christian-kohler.npm-intellisense",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
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

    # Azure/Remote (1)
    "github.codespaces",

    # Redundant (3)
    "openai.chatgpt",
    "streetsidesoftware.code-spell-checker",
    "streetsidesoftware.code-spell-checker-german"
)

# Note: ms-dotnettools.vscode-dotnet-runtime might be needed by other extensions
# Removing it last to avoid breaking dependencies
$toRemove += "ms-dotnettools.vscode-dotnet-runtime"

$count = 0
foreach ($ext in $toRemove) {
    $count++
    Write-Host "[$count/$($toRemove.Count)] Removing $ext..." -ForegroundColor Yellow
    code --uninstall-extension $ext 2>&1 | Out-Null

    # Verify removal
    $installed = code --list-extensions | Select-String -Pattern "^$ext$"
    if ($installed) {
        Write-Host "  ⚠️  Failed to remove (might be in use)" -ForegroundColor Red
    }
    else {
        Write-Host "  ✅ Removed" -ForegroundColor Green
    }
}

Write-Host "`n✅ Cleanup Complete!" -ForegroundColor Green
Write-Host "`n📊 Final Status:" -ForegroundColor Cyan
$remaining = (code --list-extensions | Measure-Object).Count
Write-Host "  Extensions Remaining: $remaining" -ForegroundColor White
Write-Host "  Expected: 35-36" -ForegroundColor Gray

Write-Host "`n💡 Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Reload VS Code: Ctrl+Shift+P -> 'Developer: Reload Window'" -ForegroundColor White
Write-Host "  2. Verify: code --list-extensions | Measure-Object" -ForegroundColor White
Write-Host "  3. Check docs/VSCODE_EXTENSIONS.md for details`n" -ForegroundColor White
