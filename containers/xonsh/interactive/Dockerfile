FROM xonsh/xonsh{colonvariant}

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Jamie Bliss <jamie@ivyleav.es>"

RUN xpip install xonsh[full]{specifier}
COPY rc_interactive.xsh /etc/xonsh/rc.d/100_rc_interactive.xsh

CMD ["/usr/bin/xonsh"]
