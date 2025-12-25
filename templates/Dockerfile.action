FROM xonsh/xonsh{colonvariant}

LABEL "repository"="http://github.com/xonsh/container"
LABEL "homepage"="https://xon.sh/"
LABEL "maintainer"="Jamie Bliss <jamie@ivyleav.es>"

COPY rc_action.xsh /etc/xonsh/rc.d/100_rc_action.xsh

CMD ["/usr/bin/xonsh"]
