#!/bin/bash

# Gere ou renove o certificado SSL com o Certbot
certbot certonly --webroot -w /code/staticfiles/ -d eadscientia.com.br --agree-tos --non-interactive --email matheusarrow28@gmail.com

# Atualize as configurações do servidor Nginx para usar o certificado SSL
sed -i 's/# SSL configuration/ssl_certificate \/etc\/letsencrypt\/live\/eadscientia.com.br\/fullchain.pem;\n    ssl_certificate_key \/etc\/letsencrypt\/live\/eadscientia.com.br\/privkey.pem;\n    ssl_trusted_certificate \/etc\/letsencrypt\/live\/eadscientia.com.br\/chain.pem;\n    ssl_dhparam \/etc\/letsencrypt\/live\/eadscientia.com.br\/dhparam.pem;\n\n    ssl_protocols TLSv1.2 TLSv1.3;\n    ssl_prefer_server_ciphers on;\n    ssl_ciphers \"EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH\";\n    ssl_ecdh_curve secp384r1;\n    ssl_session_cache shared:SSL:10m;\n    ssl_session_timeout 1d;\n    ssl_session_tickets off;\n\n    ssl_stapling on;\n    ssl_stapling_verify on;\n    resolver 8.8.8.8 8.8.4.4 valid=300s;\n    resolver_timeout 5s;\n\n    add_header Strict-Transport-Security \"max-age=63072000; includeSubDomains; preload\";\n    add_header Content-Security-Policy \"default-src https:; script-src https:; style-src https:; img-src https: data:; font-src https: data:\";\n    add_header X-Frame-Options DENY;\n    add_header X-Content-Type-Options nosniff;\n    add_header X-XSS-Protection \"1; mode=block\";/' /etc/nginx/nginx.conf

# Inicie o serviço web
gunicorn config.wsgi:application --bind 0.0.0.0:8000
