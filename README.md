# xonsh containers

Docker images for [xonsh](https://xon.sh) — a Python-powered shell.

Built daily from the latest PyPI release for `linux/amd64` and `linux/arm64`.

## Containers

* [`xonsh/xonsh`](https://hub.docker.com/r/xonsh/xonsh) — Base image. Minimal xonsh installation, suitable as a build base or for non-interactive scripts.
* [`xonsh/xonsh-interactive`](https://hub.docker.com/r/xonsh/xonsh-interactive) — Interactive shell. Adds `prompt_toolkit` and `pygments`; history is disabled.
* [`xonsh/xonsh-github-action`](https://hub.docker.com/r/xonsh/xonsh-github-action) — For GitHub Actions. Parses `$GITHUB_EVENT`, exposes `$INPUT`; PyGithub/gqlmod-ready.

## Tags

Each image publishes the same set of tags:

* `latest` / `<version>` — based on `python:3` (Debian)
* `slim` / `<version>-slim` — based on `python:3-slim`
* `alpine` / `<version>-alpine` — based on `python:3-alpine`

`<version>` is the xonsh version on PyPI, e.g. `0.23.2`.

## Usage

Run xonsh once:

```sh
docker run --rm xonsh/xonsh -c 'echo $(uname -a)'
```

Interactive shell:

```sh
docker run --rm -it xonsh/xonsh-interactive
```

Mount the current directory and start an interactive session in it:

```sh
docker run --rm -it -v "$PWD:/work" -w /work xonsh/xonsh-interactive
```

Run a local `.xsh` script:

```sh
docker run --rm -v "$PWD:/work" -w /work xonsh/xonsh xonsh ./script.xsh
```

Pin a specific version and use the slim variant:

```sh
docker run --rm xonsh/xonsh:0.23.2-slim -c '2 + 2'
```

Use as a base image:

```Dockerfile
FROM xonsh/xonsh:alpine
RUN xpip install requests
COPY ./build.xsh /build.xsh
CMD ["xonsh", "/build.xsh"]
```

Use in GitHub Actions:

```yaml
jobs:
  example:
    runs-on: ubuntu-latest
    container: xonsh/xonsh-github-action
    steps:
      - run: echo $GITHUB_EVENT['repository']['full_name']
        shell: xonsh {0}
```

## Dev

Images are built and pushed to Docker Hub from [`.github/workflows/build.yml`](./.github/workflows/build.yml). The build script ([`rebuild.xsh`](./rebuild.xsh)) is itself a xonsh script, executed in CI via [`xonsh/actions`](https://github.com/xonsh/actions) — the GitHub Action that installs xonsh on the runner.

