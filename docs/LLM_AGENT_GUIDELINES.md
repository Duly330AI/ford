# 🚀 LLM AGENT EXECUTION GUIDELINES

> **CRITICAL:** Read this before executing ANY command in a terminal.

---

## ⚠️ THE PROBLEM

LLM agents frequently:

1. Start a long-running command (pytest, npm start, build, etc.)
2. Return to user BEFORE command finishes
3. Miss failures/errors that occur after response is sent
4. User thinks everything is OK, but tests actually failed

**Example:**

```
Agent: "Starting tests..."
[Agent returns response without waiting]
[Tests run in background, 300 green dots, then RED FAILURE at the end]
User: "Tests passed!"
Agent: [gone]
```

---

## ✅ THE SOLUTION

Use the **Universal Command Wrapper** for ANY long-running command:

```powershell
# SYNTAX:
invoke-wait "your command here"

# or:
run "your command here"

# or full name:
Invoke-CommandWithCompletion "your command here"
```

---

## 📋 WHEN TO USE IT

Use wrapper for ANY command that:

- ✅ Takes more than 1-2 seconds
- ✅ Has test output (pytest, npm test, etc.)
- ✅ Starts a server (npm start, python -m server, etc.)
- ✅ Clones/downloads large repos
- ✅ Builds code
- ✅ Runs CI/CD commands

Don't use for instant commands (ls, pwd, simple git status, etc.)

---

## 📊 WHAT IT DOES

When you execute `invoke-wait "command"`:

```
╔════ COMMAND_START[a1b2c3d4] ════╗
Executing: command
PID: 1234, WorkDir: C:\project

[Full output of command...]

════════════════════════════════════════
╚════ COMMAND_END_SUCCESS[a1b2c3d4] ════╝
Duration: 45.2s
Exit Code: 0
Timestamp: 2025-10-25 14:30:45
════════════════════════════════════════
```

**Key Points:**

- Green START marker: Agent begins execution
- Full output: You see everything in real-time
- END marker: **CRITICAL** - Agent waits for this
- Exit code: 0 = success, non-zero = failure
- Duration: How long it actually took

---

## 🤖 FOR LLM AGENTS

### Rule 1: Always Wait for End Marker

```
After running: invoke-wait "pytest tests/"

Your response must ACKNOWLEDGE you see:
✓ ╚════ COMMAND_END_SUCCESS or COMMAND_END_FAILED
✓ Exit Code value
✓ Duration

ONLY THEN report results. DO NOT leave terminal early.
```

### Rule 2: Handle Exit Codes

```
If Exit Code == 0:
  → All good, report success

If Exit Code != 0:
  → Command failed, report error
  → DO NOT ignore failures
```

### Rule 3: Output Buffering

Always read the COMPLETE response from the wrapper, including:

- The colored boxes (╔ ╗ ╚ ╝)
- "COMMAND_END_" marker
- "Exit Code:" line

---

## 📝 EXAMPLES

### Example 1: Running Tests (CORRECT)

```powershell
invoke-wait "poetry run pytest tests/ -v"

# Agent sees:
╔════ COMMAND_START[x9y8z7w6] ════╗
Executing: poetry run pytest tests/ -v
[... test output ...]
tests/test_smoke.py::test_example PASSED
tests/test_smoke.py::test_another FAILED
[... more tests ...]
════════════════════════════════════════
╚════ COMMAND_END_FAILED[x9y8z7w6] ════╝
Duration: 23.4s
Exit Code: 1
════════════════════════════════════════

# Agent response: "Tests failed: 1 failure found. See output above."
# NOT: "Tests completed!" (wrong, missed the exit code)
```

### Example 2: Starting Server (CORRECT)

```powershell
invoke-wait "npm start"

# Runs for 5+ seconds, server starts...
╔════ COMMAND_START[a1b2c3d4] ════╗
Executing: npm start
Starting development server...
Server listening on localhost:3000
════════════════════════════════════════
╚════ COMMAND_END_SUCCESS[a1b2c3d4] ════╝
Duration: 4.2s
Exit Code: 0
════════════════════════════════════════

# Agent: "Server started successfully on localhost:3000"
```

### Example 3: Git Clone (CORRECT)

```powershell
invoke-wait "git clone https://github.com/project/repo.git"

╔════ COMMAND_START[p8q7r6s5] ════╗
Cloning into 'repo'...
remote: Enumerating objects: 5000, done.
[...]
════════════════════════════════════════
╚════ COMMAND_END_SUCCESS[p8q7r6s5] ════╝
Duration: 18.6s
Exit Code: 0
════════════════════════════════════════
```

---

## 🔧 TROUBLESHOOTING

**Q: Wrapper not found?**
A: Restart your terminal or run `. $PROFILE` to reload.

**Q: Output still not showing?**
A: Make sure you're running from the project directory where Conda auto-activates.

**Q: Agent still leaves early?**
A: Check if the COMMAND_END marker is visible in the terminal output. If not, increase TimeoutSeconds:

```powershell
Invoke-CommandWithCompletion "slow-command" -TimeoutSeconds 600
```

---

## 🚀 FOR NEW PROJECTS

Copy this file to each project's documentation:

- Backend: `docs/LLM_AGENT_GUIDELINES.md`
- Frontend: `frontend/docs/LLM_GUIDELINES.md`

Agents will find it and follow it!

---

**Last Updated:** 2025-10-25
**Critical for:** pytest, npm, builds, deployments, long-running operations
