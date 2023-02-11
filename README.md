Some notes on deployments and upkeep.

## Logging

- sudo systemctl status levreview.gunicorn.service
- sudo journalctl -u levreview.gunicorn.service
- sudo journalctl -u levreview.gunicorn


## Update Conf Files

- sudo cp $PROJECT_DIR/deployment/levreview.gunicorn.socket /etc/systemd/system/levreview.gunicorn.socket
- sudo cp $PROJECT_DIR/deployment/levreview.gunicorn.service /etc/systemd/system/levreview.gunicorn.service
- sudo cp $PROJECT_DIR/deployment/levreview.nginx.conf /etc/nginx/sites-available/levreview.nginx.conf
- sudo ln -s -f /etc/nginx/sites-available/levreview.nginx.conf /etc/nginx/sites-enabled/levreview.nginx.conf
