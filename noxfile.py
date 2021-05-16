"""Run common tasks using nox."""
import pathlib
import sys

import mkdocs.commands.build
import mkdocs.commands.gh_deploy
import mkdocs.commands.serve
import mkdocs.config
import mkdocs.utils
import nox
from nox.sessions import Session
from pygments.lexers import LEXERS

sys.path.append(str(pathlib.Path(__file__).resolve().parent))

from edgeql_lexer import EdgeQLLexer  # isort:skip


LEXERS["EdgeQLLexer"] = (
    "edgeql_lexer",
    EdgeQLLexer.name,
    EdgeQLLexer.aliases,
    EdgeQLLexer.filenames,
    (),
)


def _process_add_single_comma_path(session: Session, path: pathlib.Path) -> None:
    if path.is_dir():
        for new_path in path.iterdir():
            _process_add_single_comma_path(session, new_path)

        return

    if path.suffix not in {".py", ".pyi"}:
        return

    session.run(
        "add-trailing-comma",
        "--py36-plus",
        "--exit-zero-even-if-changed",
        str(path),
    )


def _process_add_single_comma(session: Session, *paths: str) -> None:
    for target in paths:
        path = pathlib.Path(target)
        _process_add_single_comma_path(session, path)


@nox.session(python=False, name="format")
def run_formatters(session: Session) -> None:
    """Run all project formatters.

    Formatters to run:
    1. isort with autoflake to remove all unused imports.
    2. black for sinle style in all project.
    3. add-trailing-comma to adding or removing comma from line.
    4. isort for properly imports sorting.
    """
    targets = ("edgeql_queries", "tests", "example", "noxfile.py")
    # we need to run isort here, since autoflake is unable to understand unused imports
    # when they are multiline.
    # see https://github.com/myint/autoflake/issues/8
    session.run("isort", "--recursive", "--force-single-line-imports", *targets)
    session.run(
        "autoflake",
        "--recursive",
        "--remove-all-unused-imports",
        "--remove-unused-variables",
        "--in-place",
        *targets,
    )
    session.run("black", *targets)
    _process_add_single_comma(session, *targets)
    session.run("isort", *targets)
    # sort edgeql_queries imports like as it was third-party library
    session.run(
        "isort",
        "--thirdparty=edgeql_queries",
        "--thirdparty=asyncpg",
        "--project=app",
        "example",
        "docs/src",
    )


@nox.session(python=False)
def lint(session: Session) -> None:
    """Run all project linters.

    Linters to run:
    1. black for code format style.
    2. mypy for type checking.
    3. flake8 for common python code style issues.
    """
    targets = ("edgeql_queries",)
    black_targets = targets + ("tests", "example", "noxfile.py")
    flake8_targets = targets + ("tests",)

    session.run("black", "--check", "--diff", *black_targets)
    session.run("mypy", *targets)
    session.run("flake8", *flake8_targets)


@nox.session(python=False)
def test(session: Session) -> None:
    """Run pytest."""
    session.run("pytest", "--cov-config=setup.cfg")


@nox.session(python=False, name="docs-build")
def docs_build(_session: Session) -> None:
    """Build docs for deploing them on GitHub Pages or Netlify."""
    mkdocs.commands.build.build(_get_docs_config())


@nox.session(python=False, name="docs-serve")
def docs_serve(_session: Session) -> None:
    """Run local website with documentation."""
    mkdocs.commands.serve.serve()


@nox.session(python=False, name="docs-gh-deploy")
def docs_gh_deploy(_session: Session) -> None:
    """Deploy docs on GitHub Pages."""
    mkdocs.commands.gh_deploy.gh_deploy(_get_docs_config())


def _get_docs_config() -> dict:
    return mkdocs.config.load_config(site_dir="./site")
