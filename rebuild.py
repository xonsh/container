#!/usr/bin/python3
import urllib.request
import json
import tempfile
import subprocess
from pathlib import Path

VARIANTS = [
    '',
    'slim',
    'alpine'
]


def get_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)


def build_dockerfile(fobj, *, which='xonsh', variant=None, version=None):
    """
    Write out a Dockerfile for the given variant and xonsh version.

    Variant should match one of the python container tag suffixes (eg slim, alpine)
    """
    fobj.write(Path(f"templates/Dockerfile.{which}").read_text().format(
        dashvariant=f"-{variant}" if variant else "",
        colonvariant=f":{variant}" if variant else "",
        specifier=f"=={version}" if version else ""
    ))


def rebuild_branch(which, version, variant, *, unversioned=False):
    if variant:
        tags = [f"xonsh/{which}:{version}-{variant}"]
    else:
        tags = [f"xonsh/{which}:{version}"]

    if unversioned:
        if variant:
            tags += [f"xonsh/{which}:{variant}"]
        else:
            tags += [f"xonsh/{which}:latest"]

    print(f"== Building {which} {version} {variant} ==", flush=True)

    with tempfile.TemporaryFile(mode='w+t', encoding='utf-8') as ntf:
        build_dockerfile(ntf, which=which, version=version, variant=variant)
        ntf.flush()
        ntf.seek(0)

        subprocess.run(
            ["docker", "build", *(f"--tag={t}" for t in tags), "-f-", "."],
            stdin=ntf, check=True,
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

for container in ('xonsh', 'action'):
    for variant in VARIANTS:
        rebuild_branch(container, latest, variant, unversioned=True)
        print("", flush=True)
