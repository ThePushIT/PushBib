from invoke import task

@task
def startdatabase(ctx):
    ctx.run('start-pg.sh', pty=True)

@task
def start(ctx):
    ctx.run('python3 src/index.py', pty = True)

@task
def starttestapp(ctx):
    ctx.run('dotenv -f .env.test run -- python3 src/index.py', pty = True)


@task
def unittests(ctx):
    ctx.run('pytest src/', pty = True)


@task
def robottests(ctx):
    ctx.run('robot src/tests/robot', pty = True)

@task
def initdb(ctx):
    #ctx.run('start_pg.sh', pty=True)
    ctx.run('python3 src/init_db.py')


@task
def inittestdb(ctx):
    ctx.run('dotenv -f .env.test run -- python3 src/init_db.py')

@task
def pylint(ctx):
    ctx.run('pylint src/')

@task
def autopep(ctx):
    ctx.run('autopep8 --in-place --recursive src/*.py')

@task
def coveragereport(ctx):
    ctx.run('coverage run --branch -m pytest')
    ctx.run('coverage html')