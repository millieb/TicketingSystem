from fabric.api import run, sudo, task, put, get

@task
def pull():
  with cd('TicketingSystem'):
    run('git pull')
  
@task  
def install_requirements():
  with cd('TicketingSystem'):
    with prefix('source env/bin/activate'):
      run('pip install -r requirements.txt')
