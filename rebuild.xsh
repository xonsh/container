#!/usr/bin/env xonsh
import urllib.request
import json


VARIANTS = [
    '',
    'slim',
    'alpine'
]


DF_TEMPLATE = """
FROM python:3{variant}

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Jamie Bliss <jamie@ivyleav.es>"

RUN ["pip", "install", "--no-cache-dir", "--disable-pip-version-check", "xonsh[linux]{specifier}"]
"""


def get_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)


def build_dockerfile(*, variant=None, version=None):
    """
    Write out a Dockerfile for the given variant and xonsh version.

    Variant should match one of the python container tag suffixes (eg slim, alpine)
    """
    p"Dockerfile".write_text(DF_TEMPLATE.format(
        variant=f"-{variant}" if variant else "",
        specifier=f"=={version}" if version else ""
    ))
    git add Dockerfile


def rebuild_branch(version, variant, *, unversioned=False):
    if variant:
        branch = f"{version}-{variant}"
    else:
        branch = version
    git checkout master
    git checkout -B @(branch)

    build_dockerfile(version=version, variant=variant)

    git commit -am "Build Dockerfile"
    # git push --force origin @(branch)

    if unversioned:
        if variant:
            branch = variant
        else:
            branch = 'latest'
        # We're currently on the post-generated commit, so just branch and push
        git checkout -B @(branch)
        # git push --force origin @(branch)


metadata = get_json("https://pypi.org/pypi/xonsh/json")

latest = metadata['info']['version']
versions = metadata['releases'].keys()

for version in versions:
    for variant in VARIANTS:
        rebuild_branch(version, variant, unversioned=(version == latest))

git checkout master
