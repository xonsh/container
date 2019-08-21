#!/usr/bin/python3
import urllib.request
import json
import tempfile
import subprocess

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


def build_dockerfile(fobj, *, variant=None, version=None):
    """
    Write out a Dockerfile for the given variant and xonsh version.

    Variant should match one of the python container tag suffixes (eg slim, alpine)
    """
    fobj.write(DF_TEMPLATE.format(
        variant=f"-{variant}" if variant else "",
        specifier=f"=={version}" if version else ""
    ))


def rebuild_branch(version, variant, *, unversioned=False):
    if variant:
        tags = [f"xonsh/xonsh:{version}-{variant}"]
    else:
        tags = [f"xonsh/xonsh:{version}"]

    if unversioned:
        if variant:
            tags += [f"xonsh/xonsh:{variant}"]
        else:
            tags += [f"xonsh/xonsh:latest"]

    print(f"== Building {version} {variant} ==", flush=True)

    with tempfile.NamedTemporaryFile(mode='w+t', encoding='utf-8') as ntf:
        build_dockerfile(ntf, version=version, variant=variant)
        ntf.flush()

        subprocess.run(
            ["docker", "build", *(f"--tag={t}" for t in tags), "-f", ntf.name, "."],
            check=True,
        )

    for t in tags:
        print(f"== Pushing {t} ==", flush=True)
        subprocess.run(
            ["docker", "push", t],
            check=True,
        )


metadata = get_json("https://pypi.org/pypi/xonsh/json")

latest = metadata['info']['version']

# Do this to publish all versions
# versions = metadata['releases'].keys()
# for version in versions:
#     for variant in VARIANTS:
#         rebuild_branch(version, variant, unversioned=(version == latest))

for variant in VARIANTS:
    rebuild_branch(latest, variant, unversioned=True)
    print("", flush=True)
