/etc/systemd/system/fastapi.service

[Unit]
Description=FastAPI App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/var/www/fast-api-python
EnvironmentFile=/var/www/fast-api-python/.env
ExecStart=/var/www/fast-api-python/venv/bin/gunicorn \
 -k uvicorn.workers.UvicornWorker \
 -w 4 \
 -b 127.0.0.1:8000 \
 app.main:app

Restart=always

[Install]
WantedBy=multi-user.target

THEN
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi

CHECK

sudo systemctl status fastapi
