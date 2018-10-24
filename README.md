# sqlalch-base-project

*This project is heavily influenced if not a direct copy of the code base from a part of the database portion of the code base of the [Apache Airflow](https://airflow.apache.org/) project*.

The purpose of this project is to produce a baseline for any project wanting to use SQLAlchemy for database access.
I found in my own projects a lot of this code is required, and is almost exactly the same between projects.

This can be used to simplify the process of starting a new application that uses any db supported by SQLALchemy.

### Setup
* `pip3 install -r requirements.txt`
* Configure your own models.
* To build migrations automatically run `alembic revision --autogenerate`.

It might be necessary to specify `PYTHONPATH='../'` to allow alembic to find the module.
(It is planned to add this functionality to the api.cli module)

To bring the database up to the current version run `export PYTHONPATH='../../'; python cli.py upgradedb` from the api directory.

### Customisation
Customising migrations is as simple as modifying the models and rerunning the `alembic revision --autogenerate` command.
Deleting any previously uneeded migrations before.

Regarding application code, dump any custom modules in the `sqlalch_base_project` dir.  To access the database from these files either define the functions on models such as the [`User.all()`](../65d0c23c540a69b66a6aece348d60adfdca576eb/sqlalch_base_project/models.py#L30) function, that is defined in the examples, or you can import one (or both) of `provide_session` and `create_session` from [`sqlalch_base_project.utils.db`](../master/sqlalch_base_project/utils/db.py) to give access to session objects.

### TODO
* Copy all the code across
* Add migrations
* Fully implement the cli interface
