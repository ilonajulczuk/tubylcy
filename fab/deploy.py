from fabric.api import task, run
from fabric.operations import put
from fabric.context_managers import cd

@task
def install_apt_packages():
    run("apt-get install nginx git")

@task
def install_circus_virtualenv():
    run("pip3 install circus chaussette virtualenv")

@task
def clone_repo():
    run("git clone https://github.com/atteroTheGreatest/tubylcy.git /var/www/source/")

@task
def create_virtualenv():
    run("virtualenv -p /usr/bin/python3 /var/www/venv")

@task
def install_packages():
    run("source /var/www/venv/bin/activate && pip install -r /var/www/source/requirements.txt")

@task
def circus_configuration():
    put('circus.ini', '/etc/')

@task
def reload_app():
    with cd('/var/www/source/'):
        venv = "source /var/www/venv/bin/activate && "
        run("git pull origin master")
        run(venv+"python tubylcy/manage_production.py migrate")
        run(venv+"python tubylcy/manage_production.py collectstatic")
        run("service circus restart")
