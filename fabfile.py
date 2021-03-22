from fabric.api import run, task, env, cd, prefix, sudo

env.hosts = ['143.198.54.173']
env.user = 'mildred'

def pull():
  run('git pull')
  
def install_requirements():
  run('pip install -r requirements.txt')
  
@task
def deploy():
  with cd('TicketingSystem'):
    pull()
   
    with prefix('source env/bin/activate'):
      install requirements()
      
    sudo('systemctl restart nginx')
