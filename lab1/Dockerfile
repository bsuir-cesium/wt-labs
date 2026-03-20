FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y apache2 python3 && \
    a2enmod cgi && \
    rm -rf /var/lib/apt/lists/*

COPY main.py /usr/lib/cgi-bin/main.py
RUN chmod +x /usr/lib/cgi-bin/main.py

RUN echo 'ScriptAlias /main.py /usr/lib/cgi-bin/main.py' \
    > /etc/apache2/conf-enabled/cgi-alias.conf

EXPOSE 80

CMD ["/bin/sh", "-c", ". /etc/apache2/envvars && exec apache2 -D FOREGROUND"]
