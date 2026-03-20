FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y apache2 python3 && \
    a2enmod cgi && \
    rm -rf /var/lib/apt/lists/*

COPY task_03.py /var/www/html/task_03.py
COPY task_additional_01.py /var/www/html/task_additional_01.py
RUN chmod +x /var/www/html/*.py

RUN printf '\
<Directory /var/www/html>\n\
    AddHandler cgi-script .py\n\
    Options +ExecCGI\n\
</Directory>\n\
' > /etc/apache2/conf-enabled/cgi.conf

RUN printf '<!doctype html>\n\
<html><head><meta charset="utf-8"><title>Lab 2</title></head>\n\
<body style="font-family: Arial, sans-serif;">\n\
<h1>Lab 2 — CGI scripts</h1>\n\
<ul>\n\
<li><a href="/task_03.py">Task 3 — Nested colored structure</a></li>\n\
<li><a href="/task_additional_01.py?a=42&amp;b=3.14&amp;c=hello">Task Additional 1 — GET param types</a></li>\n\
</ul>\n\
</body></html>' > /var/www/html/index.html

EXPOSE 80

CMD ["/bin/sh", "-c", ". /etc/apache2/envvars && exec apache2 -D FOREGROUND"]
