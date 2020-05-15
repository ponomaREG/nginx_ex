<h3>/etc/systemd/system/nginx_ex.service</h3>
<br>
<p>[Unit]
<p>Description=Gunicorn instance to server nginx_ex
<p>After=network.target

<p>[Service]
<p>User=root
<p>Group=root
<p>WorkingDirectory=/home/user/nginx_ex
<p>Environment="PATH=/home/user/nginx_ex/nginx_env/bin"
<p>ExecStart=/home/user/nginx_ex/nginx_env/bin/gunicorn --workers 3 --bind unix:nginx_ex.sock -m 007 runserver:app

<p>[Install]
<p>WantedBy=multi-user.target
<br>
<br>
<h3>/etc/systemd/system/perpetum.service</h3>
<br>
<p>[Unit]
<p>Description=Perpetum
<p>After=network.target

<p>[Service]
<p>User=root
<p>Group=root
<p>Environment="PATH=/home/user/perpetum/perpetum_env/bin"
<p>WorkingDirectory=/home/user/perpetum
<p>ExecStart=/home/user/perpetum/perpetum_env/bin/gunicorn --workers 3 --bind unix:perpetum.sock -m 007 runserver:app

<p>[Install]
<p>WantedBy=multi-user.target
<br>

<h3>/etc/nginx/sites-enabled/nginx_ex</h3>
  <br>
<p>server {
<p>        listen 80;
<p>        server_name 161.35.108.15;
<p>        error_log /home/user/nginx_ex/log.error_log;
<p>
<p>        location / {
<p>                include proxy_params;
<p>                proxy_pass http://unix:/home/user/nginx_ex/nginx_ex.sock;
<p>
<p>        }
<p>
<p>}
<p>
<p>server {
<p>        listen 6565;
<p>        server_name 161.35.108.15;
<p>        error_log /home/user/perpetum/log.error_log;
<p>
<p>        location / {
<p>                include proxy_params;
<p>                proxy_pass http://unix:/home/user/perpetum/perpetum.sock;
<p>        }
<p>}


