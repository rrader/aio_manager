aio_manager Changelog
======================

Version 2.0.2.dev0 (unreleased)
-----------------
Released on {{date_here}}.

Version 2.0.1
-----------------
Released on October 27, 2017.

  - Fix integration with aiohttp>=2.3
  - Upgrade pre-commit linting-related stuff
  - Add CI pipelines

Version 2.0.0
-----------------
Released on March 29, 2017.

  - Make SQLAlchemy interaction synchronous (PR #8 by @webknjaz)

Version 1.0.2
-----------------
Released on March 28, 2017.

  - Fix internal create_engine event handler naming (PR #6 by @webknjaz)

Version 1.0.1
-----------------
Released on March 25, 2017.

  - Fix create_engine usage (PR #5 by @webknjaz)
  - Fix create_engine dbname arg diversity (PR #5 by @webknjaz)
  - Enable unit tests in TravisCI (PR #5 by @webknjaz)


Version 1.0.0
-----------------

Released on January 4, 2017.

  - Add support for custom db engines (PR #2 by @webknjaz)
  - Add support for passing custom db port (PR #2 by @webknjaz)
  - Add testing against linters via pre-commit tool in Travis CI (PR #2 by @webknjaz)
  - Add mysql and postgres extras to the package (PR #2 by @webknjaz)


Version 0.1.2
-----------------

Released on April 19, 2016.

  - Shell command added. Works the same way as Flask-Script
  https://github.com/smurfix/flask-script/blob/master/flask_script/commands.py#L225

Version 0.1.1
-----------------

Released on April 16, 2016.

  - Unit tests added.

Version 0.1
-----------------

Released on April 15, 2016.

  - First version.
