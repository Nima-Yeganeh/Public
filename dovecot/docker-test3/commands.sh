docker build -t dovecot .
docker run -p 143:143 -p 993:993 -d dovecot
