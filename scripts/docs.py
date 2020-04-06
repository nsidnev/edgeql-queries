#!/usr/bin/env python

import mkdocs.commands.build
import mkdocs.commands.gh_deploy
import mkdocs.commands.serve
import mkdocs.config
import mkdocs.utils
from pygments.lexers import LEXERS
from typer import Typer

from edgeql_lexer import EdgeQLLexer

LEXERS["EdgeQLLexer"] = (
    "edgeql_lexer",
    EdgeQLLexer.name,
    EdgeQLLexer.aliases,
    EdgeQLLexer.filenames,
    (),
)

cli = Typer()

config = mkdocs.config.load_config(site_dir=str("./site"))


@cli.command()
def build() -> None:
    mkdocs.commands.build.build(config)


@cli.command()
def serve() -> None:
    mkdocs.commands.serve.serve(dev_addr="0.0.0.0:8000")


@cli.command("gh-deploy")
def gh_deploy() -> None:
    mkdocs.commands.gh_deploy.gh_deploy(config)


if __name__ == "__main__":
    cli()
