from invoke import task

@task
def startdatabase(ctx):
    ctx.run('start-pg.sh', pty=True)

@task
def compile_translations(ctx):
    ctx.run("pybabel compile -d translations")

@task(compile_translations)
def start(ctx):
    ctx.run('python3 src/index.py', pty = True)

@task(compile_translations)
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

@task
def update_translation_files(ctx):
    ctx.run("pybabel extract -F babel.cfg -o messages.pot .")
    ctx.run("pybabel update -i messages.pot -d translations")

@task(update_translation_files)
def create_translation_file(ctx, lang):
    ctx.run(f"pybabel init -i messages.pot -d translations -l {lang}")

