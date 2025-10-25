# VS Code Extensions - FORD Project

## ✅ Essential (Already Installed)

### Python Development
- ✅ `ms-python.python` - Python language support
- ✅ `ms-python.vscode-pylance` - Fast type checking & IntelliSense
- ✅ `ms-python.black-formatter` - Black code formatter
- ✅ `charliermarsh.ruff` - Fast Python linter
- ✅ `ms-python.debugpy` - Python debugger
- ✅ `ms-python.vscode-python-envs` - Environment management

### Testing & Quality
- ✅ `ms-toolsai.jupyter` - Jupyter notebook support
- ✅ `usernamehw.errorlens` - Inline error display
- ✅ `visualstudioexptteam.vscodeintellicode` - AI-assisted IntelliSense

### Copilot & AI
- ✅ `github.copilot` - AI coding assistant
- ✅ `github.copilot-chat` - Chat interface for Copilot

### Git
- ✅ `eamodio.gitlens` - Git supercharged
- ✅ `mhutchie.git-graph` - Visual git history
- ✅ `github.vscode-github-actions` - GitHub Actions workflows

### Documentation
- ✅ `davidanson.vscode-markdownlint` - Markdown linting
- ✅ `gruntfuggly.todo-tree` - TODO tracking across project

### Code Quality
- ✅ `editorconfig.editorconfig` - EditorConfig support
- ✅ `aaron-bond.better-comments` - Highlighted comments

### Data Files
- ✅ `redhat.vscode-yaml` - YAML language support
- ✅ `tamasfe.even-better-toml` - TOML language support
- ✅ `mechatroner.rainbow-csv` - CSV file viewer

### Utilities
- ✅ `christian-kohler.path-intellisense` - Path autocomplete
- ✅ `ms-vscode.powershell` - PowerShell support
- ✅ `pkief.material-icon-theme` - Material icon theme

---

## 🆕 Recommended to Install

### Testing
```bash
# Test Explorer for better test visualization
code --install-extension hbenl.vscode-test-explorer
code --install-extension littlefoxteam.vscode-python-test-adapter
```

### Coverage
```bash
# Coverage visualization in gutters
code --install-extension ryanluker.vscode-coverage-gutters
```

---

## ❌ Recommended to Remove

These extensions are not needed for the FORD project:

### Web Development (not needed)
```bash
code --uninstall-extension bradlc.vscode-tailwindcss
code --uninstall-extension ecmel.vscode-html-css
code --uninstall-extension christian-kohler.npm-intellisense
code --uninstall-extension dbaeumer.vscode-eslint
code --uninstall-extension esbenp.prettier-vscode
code --uninstall-extension vue.volar
code --uninstall-extension wix.vscode-import-cost
code --uninstall-extension ms-edgedevtools.vscode-edge-devtools
code --uninstall-extension ms-playwright.playwright
```

### Database Tools (not primary focus)
```bash
code --uninstall-extension ms-mssql.mssql
code --uninstall-extension ms-mssql.data-workspace-vscode
code --uninstall-extension ms-mssql.sql-bindings-vscode
code --uninstall-extension ms-mssql.sql-database-projects-vscode
code --uninstall-extension mtxr.sqltools
code --uninstall-extension qwtel.sqlite-viewer
```

### Other Frameworks
```bash
code --uninstall-extension geequlim.godot-tools
code --uninstall-extension batisteo.vscode-django
code --uninstall-extension samuelcolvin.jinjahtml
```

### Containers (later if needed)
```bash
code --uninstall-extension ms-azuretools.vscode-containers
code --uninstall-extension ms-azuretools.vscode-docker
code --uninstall-extension ms-vscode-remote.remote-containers
code --uninstall-extension p1c2u.docker-compose
```

### Azure/Remote (not needed)
```bash
code --uninstall-extension ms-azuretools.vscode-azureresourcegroups
code --uninstall-extension github.codespaces
code --uninstall-extension github.remotehub
code --uninstall-extension ms-vscode.remote-repositories
code --uninstall-extension ms-vscode.azure-repos
code --uninstall-extension ms-vscode-remote.remote-wsl
```

### Redundant
```bash
code --uninstall-extension openai.chatgpt  # Use Copilot Chat instead
code --uninstall-extension mikestead.dotenv
code --uninstall-extension humao.rest-client
code --uninstall-extension streetsidesoftware.code-spell-checker  # Disabled in settings
code --uninstall-extension streetsidesoftware.code-spell-checker-german
```

---

## 🔧 Extension Settings

All extension settings are configured in `.vscode/settings.json`:
- Python interpreter: `.venv/Scripts/python.exe`
- Formatter: Black (88 char line length)
- Linter: Ruff (on save)
- Testing: Pytest
- Type checking: Pylance (standard mode)

---

## 📦 Batch Commands

### Uninstall all unnecessary extensions:
```powershell
# Copy this entire block and run in PowerShell
$toRemove = @(
  "bradlc.vscode-tailwindcss",
  "ecmel.vscode-html-css",
  "christian-kohler.npm-intellisense",
  "dbaeumer.vscode-eslint",
  "esbenp.prettier-vscode",
  "vue.volar",
  "wix.vscode-import-cost",
  "ms-edgedevtools.vscode-edge-devtools",
  "ms-playwright.playwright",
  "ms-mssql.mssql",
  "ms-mssql.data-workspace-vscode",
  "ms-mssql.sql-bindings-vscode",
  "ms-mssql.sql-database-projects-vscode",
  "mtxr.sqltools",
  "qwtel.sqlite-viewer",
  "geequlim.godot-tools",
  "batisteo.vscode-django",
  "samuelcolvin.jinjahtml",
  "ms-azuretools.vscode-containers",
  "ms-azuretools.vscode-docker",
  "ms-vscode-remote.remote-containers",
  "p1c2u.docker-compose",
  "ms-azuretools.vscode-azureresourcegroups",
  "github.codespaces",
  "github.remotehub",
  "ms-vscode.remote-repositories",
  "ms-vscode.azure-repos",
  "ms-vscode-remote.remote-wsl",
  "openai.chatgpt",
  "mikestead.dotenv",
  "humao.rest-client",
  "streetsidesoftware.code-spell-checker",
  "streetsidesoftware.code-spell-checker-german"
)

foreach ($ext in $toRemove) {
  Write-Host "Uninstalling $ext..." -ForegroundColor Yellow
  code --uninstall-extension $ext
}

Write-Host "`n✅ Cleanup complete!" -ForegroundColor Green
```

### Install recommended extensions:
```powershell
# Test Explorer
code --install-extension hbenl.vscode-test-explorer
code --install-extension littlefoxteam.vscode-python-test-adapter

# Coverage Gutters
code --install-extension ryanluker.vscode-coverage-gutters

Write-Host "`n✅ Recommended extensions installed!" -ForegroundColor Green
```

---

## 🚀 Quick Verification

After cleanup, verify your setup:
```powershell
# List currently installed extensions
code --list-extensions | Sort-Object

# Should have ~25-30 extensions (down from 67)
```

Expected core extensions:
- Python ecosystem (6)
- Testing & Jupyter (5)
- Copilot & AI (2)
- Git tools (3)
- Documentation (2)
- Code quality (2)
- Data files (3)
- Utilities (3)
- Optional: Language pack (1)

---

## 📚 See Also

- `.vscode/settings.json` - Project-specific settings
- `.vscode/extensions.json` - Recommended/unwanted extensions
- `.vscode/tasks.json` - Build/test/lint tasks
- `.vscode/launch.json` - Debug configurations
- `docs/DEVELOPMENT.md` - Development setup guide
