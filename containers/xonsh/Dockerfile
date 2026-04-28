FROM python:3.11{dashvariant}

LABEL "repository"="https://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Xonsh Maintainers <xore.004fdbd5c8e6589bdd80944b5b8d4100.show-sender@streams.zulipchat.com>"

RUN pip install --no-cache-dir --disable-pip-version-check xonsh[linux]{specifier} && \
    ln -s $(which xonsh) /usr/bin/xonsh
COPY xpip.xsh /usr/bin/xpip

CMD ["/usr/bin/xonsh"]
