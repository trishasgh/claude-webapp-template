
This file documents development standards for AI coding agents (Claude Code, Codex, etc.).  
Read this alongside `CLAUDE.md` for full context.

## IMPORTANT - Execution Environment

An external hook will set up a python Virtual Environment for you under
the subdirectory '.venv/' and will set environment variables PATH,
PYTHON_PATH, etc. accordingly.  Always use the virtual environment's
"pip" and not "/usr/bin/pip" or other system-installed tools.

You are running as a nonprivileged user within a Linux container.
You do not have the ability to "sudo", so do not assume you can add
system packages (e.g. "apt-get").  If needed functionality is only
available via that path, stop execution and ask the user to update the
container configuration.

Your network ports are not directly accessible to the user.  A single TCP port 8000 has been
SSH-tunnelled (-L 8000:localhost:8000) from the user's client to the container; use this port for applications you build.


