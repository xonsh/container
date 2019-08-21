FROM python:3-slim

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Jamie Bliss <jamie@ivyleav.es>"

RUN ["pip", "install", "--no-cache-dir", "--disable-pip-version-check", "xonsh[linux]"]
