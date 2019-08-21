FROM xonsh/xonsh

RUN apt-get update && apt-get install -y docker.io
COPY rebuild.xsh /rebuild.xsh
