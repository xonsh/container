# xonsh for interactive use

[GitHub](https://github.com/xonsh/container) | [Docker Hub](https://hub.docker.com/r/xonsh/xonsh-interactive)

Xonsh (sounds like "consh") is a modern, full-featured and cross-platform Python-based shell. The language is a superset of Python 3 with seamless integration of shell functionality and commands. It works on all major systems including Linux, macOS, and Windows. Xonsh is meant for the daily use of experts and novices.

This container includes additional dependencies and some configuration tweaks
specifically for interactive use.

## Additions
* Prompt Toolkit and Pygments are installed
* Saving history is disabled

In addition, this container inherits from the main xonsh container and includes
these:
* `/usr/bin/xpip`: `xpip` usable from Dockerfiles/etc to enable installing
  Python packages into the xonsh environment. Doesn't require cleanup.
* `/usr/bin/xonsh`: xonsh itself.

## Tags

* `<version>`/`latest`: Based on `xonsh`/`python:3` (Debian Buster)
* `<version>-slim`/`slim`: Based on `xonsh:slim`/`python:3-slim` (Debian Buster, slim variant)
* `<version>-alpine`/`alpine`: Based on `xonsh:alpine`/`python:3-alpine` (Alpine Linux)
