#!/usr/bin/xonsh
# Because this is specifically for calling from Dockerfile, do some defaults
xpip --no-cache-dir --disable-pip-version-check @($ARGS[1:])
