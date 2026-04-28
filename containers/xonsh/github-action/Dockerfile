FROM xonsh/xonsh{colonvariant}

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Xonsh Maintainers <xore.004fdbd5c8e6589bdd80944b5b8d4100.show-sender@streams.zulipchat.com>"

COPY rc_action.xsh /etc/xonsh/rc.d/100_rc_action.xsh

CMD ["/usr/bin/xonsh"]
