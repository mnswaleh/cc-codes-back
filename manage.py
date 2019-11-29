import os
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from app import create_app

app = create_app(os.getenv('FLASK_ENV') or 'default')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context))

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
