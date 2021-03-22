from fabric.api import run, sudo, task, put, get

@task
def pull():
  with cd('TicketingSystem'):
    run('git pull')
  
@task  
def install_requirements():
  run('cd TicketingSystem && source env/bin/activate && pip install -r requirements.txt')
