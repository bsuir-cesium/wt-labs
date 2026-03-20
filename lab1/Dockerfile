FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y apache2 python3 && \
    a2enmod cgi && \
    rm -rf /var/lib/apt/lists/*

COPY main.py /var/www/html/main.py
RUN chmod +x /var/www/html/main.py

RUN printf '\
<Directory /var/www/html>\n\
    AddHandler cgi-script .py\n\
    Options +ExecCGI\n\
</Directory>\n\
' > /etc/apache2/conf-enabled/cgi.conf

EXPOSE 80

CMD ["/bin/sh", "-c", ". /etc/apache2/envvars && exec apache2 -D FOREGROUND"]
