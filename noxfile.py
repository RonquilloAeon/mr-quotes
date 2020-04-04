import nox


@nox.session(python="3.8", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-r", "test-requirements.txt")


@nox.session(python="3.8", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "src")


@nox.session(python="3.8", reuse_venv=True)
def check(session):
    session.install("flake8")
    session.run("flake8", "src")


@nox.session(python="3.8", reuse_venv=True)
def test(session):
    session.install("-r", "test-requirements.txt")
    session.run(
        "pytest",
        "--cov=src",
        *session.posargs,
        env={
            "DB_HOST": "localhost",
            "DB_NAME": "test_quotesdb",
            "DB_USER": "mrquotes",
            "DB_PASS": "passpass",
            "TESTING": "true",
        }
    )
