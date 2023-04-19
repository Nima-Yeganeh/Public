FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y dovecot-core dovecot-imapd dovecot-lmtpd

COPY dovecot.conf /etc/dovecot/dovecot.conf

EXPOSE 143 993

CMD ["dovecot", "-F"]
