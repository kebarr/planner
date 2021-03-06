from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from planner.config import CurrentConfig
from planner import model
from planner.model import engagement, iteration, team, client

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
m = model.Base.metadata


# Jordan: Can't be autogenerated... manual bollocks
#for t in engagement.Engagement.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Expense.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.ExpenseType.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Status.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Alignment.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Sustainability.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Probability.metadata.tables.values():
#    t.tometadata(m)

#for t in engagement.Complexity.metadata.tables.values():
#    t.tometadata(m)

#for t in team.Team.metadata.tables.values():
#    t.tometadata(m)

#for t in team.TeamMember.metadata.tables.values():
#    t.tometadata(m)

#for t in team.Cost.metadata.tables.values():
#    t.tometadata(m)

#for t in team.CostType.metadata.tables.values():
#    t.tometadata(m)

#for t in client.Contact.metadata.tables.values():
#    t.tometadata(m)

#for t in client.Contact.metadata.tables.values():
#    t.tometadata(m)

#for t in iteration.Iteration.metadata.tables.values():
#    t.tometadata(m)


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = CurrentConfig.DBPATH
    context.configure(url=url, target_metadata=m)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    alembic_config = config.get_section(config.config_ini_section)
    alembic_config['sqlalchemy.url'] = CurrentConfig.DBPATH


    engine = engine_from_config(
        alembic_config,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=m
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
