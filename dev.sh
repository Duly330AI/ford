#!/usr/bin/env bash
# FORD Project - Bash Helper Script
# Usage: source dev.sh (from project root)
# Provides: poetry, pre-commit, ruff, black, pytest, run-game, etc.

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project root
FORD_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if conda environment is active
check_conda() {
    if [[ -z "$CONDA_DEFAULT_ENV" ]]; then
        echo -e "${YELLOW}⚠ Conda environment not active${NC}"
        echo -e "  Run: ${BLUE}conda activate ford${NC}"
        return 1
    fi
    return 0
}

# ===== SETUP COMMANDS =====

install-deps() {
    echo -e "${BLUE}📦 Installing dependencies...${NC}"
    if ! check_conda; then return 1; fi
    poetry install --no-root
    echo -e "${GREEN}✅ Dependencies installed${NC}"
}

install-hooks() {
    echo -e "${BLUE}🪝 Installing pre-commit hooks...${NC}"
    if ! check_conda; then return 1; fi
    pre-commit install
    echo -e "${GREEN}✅ Pre-commit hooks installed${NC}"
}

# ===== WRAPPER COMMANDS =====

# Poetry wrapper
poetry() {
    command poetry "$@"
}

# Pre-commit wrapper
pre-commit() {
    command pre-commit "$@"
}

# Ruff wrapper
ruff() {
    command ruff "$@"
}

# Black wrapper
black() {
    command black "$@"
}

# Pytest wrapper
pytest() {
    command pytest "$@"
}

# ===== LINTING COMMANDS =====

lint-all() {
    echo -e "${BLUE}🔍 Running pre-commit on all files...${NC}"
    if ! check_conda; then return 1; fi
    pre-commit run --all-files
    echo -e "${GREEN}✅ Linting complete${NC}"
}

lint-staged() {
    echo -e "${BLUE}🔍 Running pre-commit on staged files...${NC}"
    if ! check_conda; then return 1; fi
    pre-commit run
    echo -e "${GREEN}✅ Linting complete${NC}"
}

lint-fix() {
    echo -e "${BLUE}🔧 Auto-fixing with ruff...${NC}"
    if ! check_conda; then return 1; fi
    ruff check . --fix
    echo -e "${BLUE}🔧 Auto-formatting with black...${NC}"
    black .
    echo -e "${GREEN}✅ Auto-fixes complete${NC}"
}

# ===== TEST COMMANDS =====

test-all() {
    echo -e "${BLUE}🧪 Running all tests...${NC}"
    if ! check_conda; then return 1; fi
    pytest -v
}

test-fast() {
    echo -e "${BLUE}⚡ Running fast tests (no slow)...${NC}"
    if ! check_conda; then return 1; fi
    pytest -m "not slow" -q
}

test-coverage() {
    echo -e "${BLUE}📊 Running tests with coverage...${NC}"
    if ! check_conda; then return 1; fi
    pytest --cov=game --cov-report=html
    echo -e "${GREEN}✅ Coverage report generated: htmlcov/index.html${NC}"
}

# ===== GAME COMMANDS =====

run-game() {
    echo -e "${BLUE}🎮 Starting FORD game...${NC}"
    if ! check_conda; then return 1; fi
    python -m game.main
}

run-game-debug() {
    echo -e "${BLUE}🎮 Starting FORD game (debug mode)...${NC}"
    if ! check_conda; then return 1; fi
    FORD_DEBUG=1 python -m game.main
}

# ===== UTILITY COMMANDS =====

dev-status() {
    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
    echo -e "${BLUE}📋 FORD Development Environment Status${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
    echo ""

    # Conda
    if [[ -n "$CONDA_DEFAULT_ENV" ]]; then
        echo -e "${GREEN}✅ Conda environment: ${CYAN}$CONDA_DEFAULT_ENV${NC}"
    else
        echo -e "${RED}❌ Conda environment: ${YELLOW}NOT ACTIVE${NC}"
    fi

    # Python
    if command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version 2>&1)
        echo -e "${GREEN}✅ Python: ${CYAN}$PYTHON_VERSION${NC}"
    else
        echo -e "${RED}❌ Python: ${YELLOW}NOT FOUND${NC}"
    fi

    # Poetry
    if command -v poetry &> /dev/null; then
        POETRY_VERSION=$(poetry --version 2>&1 | awk '{print $NF}')
        echo -e "${GREEN}✅ Poetry: ${CYAN}$POETRY_VERSION${NC}"
    else
        echo -e "${RED}❌ Poetry: ${YELLOW}NOT FOUND${NC}"
    fi

    # Pre-commit
    if command -v pre-commit &> /dev/null; then
        echo -e "${GREEN}✅ Pre-commit: ${CYAN}installed${NC}"
    else
        echo -e "${RED}❌ Pre-commit: ${YELLOW}NOT FOUND${NC}"
    fi

    # Git
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version 2>&1 | awk '{print $3}')
        echo -e "${GREEN}✅ Git: ${CYAN}$GIT_VERSION${NC}"
    else
        echo -e "${RED}❌ Git: ${YELLOW}NOT FOUND${NC}"
    fi

    # Bash
    echo -e "${GREEN}✅ Bash: ${CYAN}$BASH_VERSION${NC}"

    echo ""
    echo -e "${BLUE}Working directory: ${CYAN}$(pwd)${NC}"
    echo ""

    # Pre-commit status
    if [[ -f "$FORD_ROOT/.git/hooks/pre-commit" ]]; then
        echo -e "${GREEN}✅ Pre-commit hooks: ${CYAN}INSTALLED${NC}"
    else
        echo -e "${YELLOW}⚠ Pre-commit hooks: ${CYAN}NOT INSTALLED${NC}"
        echo -e "  Run: ${BLUE}install-hooks${NC}"
    fi

    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
}

dev-help() {
    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
    echo -e "${BLUE}📚 FORD Development Commands${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
    echo ""

    echo -e "${GREEN}Setup Commands:${NC}"
    echo "  install-deps        Install dependencies from poetry.lock"
    echo "  install-hooks       Install pre-commit git hooks"
    echo ""

    echo -e "${GREEN}Linting Commands:${NC}"
    echo "  lint-all            Run pre-commit on all files"
    echo "  lint-staged         Run pre-commit on staged files only"
    echo "  lint-fix            Auto-fix with ruff & black"
    echo ""

    echo -e "${GREEN}Test Commands:${NC}"
    echo "  test-all            Run all tests with verbose output"
    echo "  test-fast           Run fast tests (no slow tests)"
    echo "  test-coverage       Generate coverage report"
    echo ""

    echo -e "${GREEN}Game Commands:${NC}"
    echo "  run-game            Start FORD game"
    echo "  run-game-debug      Start FORD game in debug mode"
    echo ""

    echo -e "${GREEN}Utility Commands:${NC}"
    echo "  dev-status          Show environment status"
    echo "  dev-help            Show this help message"
    echo ""

    echo -e "${GREEN}Direct Commands:${NC}"
    echo "  poetry <cmd>        Run poetry (e.g., poetry add package)"
    echo "  pre-commit <cmd>    Run pre-commit"
    echo "  ruff <cmd>          Run ruff linter"
    echo "  black <cmd>         Run black formatter"
    echo "  pytest <cmd>        Run pytest (e.g., pytest -v)"
    echo ""

    echo -e "${BLUE}═══════════════════════════════════════════${NC}"
}

# ===== STARTUP MESSAGE =====

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    # Script was sourced
    echo -e "${GREEN}✅ FORD development environment loaded${NC}"
    echo -e "   Type ${BLUE}dev-help${NC} for available commands"
else
    # Script was executed directly
    echo -e "${RED}❌ Error: dev.sh must be sourced, not executed${NC}"
    echo -e "   Usage: ${BLUE}source dev.sh${NC}"
    exit 1
fi
