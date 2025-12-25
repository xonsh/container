#!/usr/bin/python3
import urllib.request
import json
import tempfile
import subprocess
from pathlib import Path
from contextlib import chdir

VARIANTS = [
    '',
    'slim',
    'alpine'
]


def get_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)


def build_dockerfile(source_dockerfile, target_dockerfile, *, variant=None, version=None):
    """Format source_file and save to target_file."""
    target_dockerfile.write(Path(source_dockerfile).read_text().format(
        dashvariant=f"-{variant}" if variant else "",
        colonvariant=f":{variant}" if variant else "",
        specifier=f"=={version}" if version else ""
    ))


def rebuild_branch(container_name, source_dockerfile:Path, version, variant, *, unversioned=False):
    if variant:
        tags = [f"xonsh/{container_name}:{version}-{variant}"]
    else:
        tags = [f"xonsh/{container_name}:{version}"]

    if unversioned:
        if variant:
            tags += [f"xonsh/{container_name}:{variant}"]
        else:
            tags += [f"xonsh/{container_name}:latest"]

    print(f"== Building {container_name} {version} {variant} ==", flush=True)

    with tempfile.TemporaryFile(mode='w+t', encoding='utf-8') as target_dockerfile:
        build_dockerfile(source_dockerfile, target_dockerfile, version=version, variant=variant)
        target_dockerfile.flush()
        target_dockerfile.seek(0)

        with chdir(source_dockerfile.parent):
            subprocess.run(
                ["docker", "build", *(f"--tag={t}" for t in tags), "-f-", "."],
                stdin=target_dockerfile, check=True,
            )

    for t in tags:
        print(f"== Pushing {t} ==", flush=True)
        subprocess.run(["docker", "push", t], check=True,)



# Do this to publish all versions
# versions = metadata['releases'].keys()
# for version in versions:
#     for variant in VARIANTS:
#         rebuild_branch(version, variant, unversioned=(version == latest))

if __name__ == '__main__':
    metadata = get_json("https://pypi.org/pypi/xonsh/json")
    metadata_latest_version = metadata['info']['version']

    for base_dockerfile in Path('./containers/').glob('*/Dockerfile'):
        base_name = base_dockerfile.parent.name
        for variant in VARIANTS:
            print(f"Build {base_name}:{variant}", flush=True)
            rebuild_branch(base_name, base_dockerfile, metadata_latest_version, variant, unversioned=True)
            for child_dockerfile in base_dockerfile.glob('*/Dockerfile'):
                child_name = child_dockerfile.parent.name
                container_name = f"{base_name}-{child_name}"
                print(f"Build {container_name}:{variant}", flush=True)
                rebuild_branch(container_name, child_dockerfile, metadata_latest_version, variant, unversioned=True)

                # Backwards compatibility
                if container_name == 'xonsh-interactive':
                    rebuild_branch('interactive', child_dockerfile, metadata_latest_version, variant, unversioned=True)
                elif container_name == 'xonsh-github-action':
                    rebuild_branch('action', child_dockerfile, metadata_latest_version, variant, unversioned=True)

