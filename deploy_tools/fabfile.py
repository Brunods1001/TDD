import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/Brunods1001/TDD.git'

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

'''
# testing
cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/testing.new.brunodos3.com/g" \
    | sudo tee /etc/nginx/sites-available/testing.new.brunodos3.com
   
cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/testing.new.brunodos3.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-testing.new.brunodos3.com.service 

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-testing.new.brunodos3.com
sudo systemctl start gunicorn-testing.new.brunodos3.com
    
# staging
cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/staging.brunodos3.com/g" \
    | sudo tee /etc/nginx/sites-available/staging.brunodos3.com
   
cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/staging.brunodos3.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-staging.brunodos3.com.service 

cd /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/staging.brunodos3.com staging.brunodos3.com

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-staging.brunodos3.com
sudo systemctl start gunicorn-staging.brunodos3.com

# production    
cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/brunodos3.com/g" \
    | sudo tee /etc/nginx/sites-available/brunodos3.com
   
cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/brunodos3.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-brunodos3.com.service 

cd /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/brunodos3.com brunodos3.com

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-brunodos3.com
sudo systemctl start gunicorn-brunodos3.com

'''