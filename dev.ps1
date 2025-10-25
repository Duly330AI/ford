# FORD Project - PowerShell Helper Script
# Usage: . .\dev.ps1  (dot-source to keep functions in current session)

# Activate virtual environment
function Activate-Venv {
    & .\.venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual environment activated" -ForegroundColor Green
}

# Run poetry commands
function poetry {
    & .\.venv\Scripts\poetry.exe @args
}

# Run pre-commit
function pre-commit {
    & .\.venv\Scripts\pre-commit.exe @args
}

# Run ruff
function ruff {
    & .\.venv\Scripts\ruff.exe @args
}

# Run black
function black {
    & .\.venv\Scripts\black.exe @args
}

# Run pytest
function pytest {
    & .\.venv\Scripts\pytest.exe @args
}

# Run the game
function run-game {
    & .\.venv\Scripts\python.exe -m game.main
}

# Install dependencies
function install-deps {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    & .\.venv\Scripts\poetry.exe install --no-root
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
}

# Run pre-commit on all files
function lint-all {
    Write-Host "Running pre-commit on all files..." -ForegroundColor Yellow
    & .\.venv\Scripts\pre-commit.exe run --all-files
}

# Run pre-commit on staged files
function lint-staged {
    Write-Host "Running pre-commit on staged files..." -ForegroundColor Yellow
    & .\.venv\Scripts\pre-commit.exe run
}

# Install pre-commit hooks
function install-hooks {
    Write-Host "Installing pre-commit hooks..." -ForegroundColor Yellow
    & .\.venv\Scripts\pre-commit.exe install
    Write-Host "✅ Hooks installed" -ForegroundColor Green
}

# Quick status
function dev-status {
    Write-Host "`n📦 FORD Development Environment Status" -ForegroundColor Cyan
    Write-Host "=======================================" -ForegroundColor Cyan

    Write-Host "`nPoetry: " -NoNewline
    & .\.venv\Scripts\poetry.exe --version

    Write-Host "Pre-commit: " -NoNewline
    & .\.venv\Scripts\pre-commit.exe --version

    Write-Host "Python: " -NoNewline
    & .\.venv\Scripts\python.exe --version

    Write-Host "Ruff: " -NoNewline
    & .\.venv\Scripts\ruff.exe --version

    Write-Host "Black: " -NoNewline
    & .\.venv\Scripts\black.exe --version

    Write-Host "`nGit Status:" -ForegroundColor Yellow
    git status --short

    Write-Host "`n✅ All tools ready!" -ForegroundColor Green
}

# Help
function dev-help {
    Write-Host "`n📚 FORD Development Helper Commands" -ForegroundColor Cyan
    Write-Host "=====================================" -ForegroundColor Cyan
    Write-Host "`nSetup:"
    Write-Host "  install-deps     - Install all dependencies"
    Write-Host "  install-hooks    - Install pre-commit hooks"
    Write-Host "`nDevelopment:"
    Write-Host "  poetry <cmd>     - Run poetry commands"
    Write-Host "  pre-commit <cmd> - Run pre-commit commands"
    Write-Host "  ruff <cmd>       - Run ruff linter"
    Write-Host "  black <cmd>      - Run black formatter"
    Write-Host "  pytest <cmd>     - Run pytest"
    Write-Host "  run-game         - Run the FORD game"
    Write-Host "`nLinting:"
    Write-Host "  lint-all         - Lint all files"
    Write-Host "  lint-staged      - Lint staged files only"
    Write-Host "`nUtilities:"
    Write-Host "  dev-status       - Show development environment status"
    Write-Host "  dev-help         - Show this help message"
    Write-Host "`n💡 Tip: Run '. .\dev.ps1' to load these functions"
    Write-Host ""
}

# Auto-show help on first load
Write-Host "`n🚀 FORD Development Environment Loaded" -ForegroundColor Green
Write-Host "Run 'dev-help' for available commands`n" -ForegroundColor Yellow
