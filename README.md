# xonsh

[GitHub](https://github.com/xonsh/container) | [Docker Hub](https://hub.docker.com/r/xonsh/xonsh)

Xonsh is a Python-powered shell. Full-featured and cross-platform. The language is a superset of Python 3.5+ with additional shell primitives that you are used to from Bash and IPython. It works on all major systems including Linux, Mac OSX, and Windows. Xonsh is meant for the daily use of experts and novices alike.

## Additions

* `/usr/bin/xpip`: `xpip` usable from Dockerfiles/etc to enable installing
  Python packages into the xonsh environment. Doesn't require cleanup.
* `/usr/bin/xonsh`: xonsh itself.

## Tags

* `<version>`/`latest`: Based on `python:3` (Debian Buster)
* `<version>-slim`/`slim`: Based on `python:3-slim` (Debian Buster, slim variant)
* `<version>-alpine`/`alpine`: Based on `python:3-alpine` (Alpine Linux)


# xonsh for github actions

[GitHub](https://github.com/xonsh/container) | [Docker Hub](https://hub.docker.com/r/xonsh/action)

Xonsh is a Python-powered shell. Full-featured and cross-platform. The language is a superset of Python 3.5+ with additional shell primitives that you are used to from Bash and IPython. It works on all major systems including Linux, Mac OSX, and Windows. Xonsh is meant for the daily use of experts and novices alike.

This container includes code to help with GitHub Actions. It automatically
parses the input and configures GitHub API client libraries.
[PyGithub](https://pygithub.readthedocs.io/) and [gqlmod](https://gqlmod.readthedocs.io/) are supported (but not installed by default).

## Additions
* `$GITHUB_EVENT`: The parsed event payload
* `$INPUT`: A dictionary of input values (the `with` block in the workflow config)
* If PyGithub is installed, `$GITHUB` is the client object

The GitHub Token is looked for as `GITHUB_TOKEN` in the environment and inputs.

In addition, this container inherits from the main xonsh container and includes
these:
* `/usr/bin/xpip`: `xpip` usable from Dockerfiles/etc to enable installing
  Python packages into the xonsh environment. Doesn't require cleanup.
* `/usr/bin/xonsh`: xonsh itself.

## Tags

* `<version>`/`latest`: Based on `xonsh`/`python:3` (Debian Buster)
* `<version>-slim`/`slim`: Based on `xonsh:slim`/`python:3-slim` (Debian Buster, slim variant)
* `<version>-alpine`/`alpine`: Based on `xonsh:alpine`/`python:3-alpine` (Alpine Linux)


# xonsh for interactive use
[GitHub](https://github.com/xonsh/container) | [Docker Hub](https://hub.docker.com/r/xonsh/interactive)

Xonsh is a Python-powered shell. Full-featured and cross-platform. The language is a superset of Python 3.5+ with additional shell primitives that you are used to from Bash and IPython. It works on all major systems including Linux, Mac OSX, and Windows. Xonsh is meant for the daily use of experts and novices alike.

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
