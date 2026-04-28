FROM xonsh/xonsh{colonvariant}

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Xonsh Maintainers <xore.004fdbd5c8e6589bdd80944b5b8d4100.show-sender@streams.zulipchat.com>"

RUN xpip install xonsh[full]{specifier}
COPY rc_interactive.xsh /etc/xonsh/rc.d/100_rc_interactive.xsh

CMD ["/usr/bin/xonsh"]
