"""qtl CLI — single entry point."""

from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from qtl_lab.registry import PLUGIN_KINDS, discover
from qtl_lab.scaffold import new_plugin

app = typer.Typer(help="Quant Theory Lab CLI", no_args_is_help=True)
console = Console()


@app.command("doctor")
def doctor() -> None:
    """Health check."""
    from qtl_core.paths import artifacts, repo_root

    root = repo_root()
    console.print(f"QTL_ROOT: {root}")
    console.print(f"artifacts: {artifacts()} ({'ok' if artifacts().exists() else 'missing'})")
    for kind in PLUGIN_KINDS:
        n = len(discover(kind))
        console.print(f"  {kind}: {n}")


@app.command("list")
def list_plugins(kind: Optional[str] = typer.Argument(None)) -> None:
    """List discovered plugins."""
    plugins = discover(kind)
    table = Table(title="Quant Theory Lab plugins")
    table.add_column("kind")
    table.add_column("slug")
    table.add_column("status")
    table.add_column("domain")
    for p in plugins:
        table.add_row(
            p.kind,
            p.slug,
            str(p.meta.get("status", "")),
            str(p.meta.get("domain", "")),
        )
    console.print(table)


@app.command("new")
def new_cmd(
    kind: str = typer.Argument(..., help="notebook|paper|post|project|data|dataset|model"),
    name: str = typer.Argument(...),
    domain: str = typer.Option("general", "--domain", "-d"),
) -> None:
    """Scaffold a new plugin."""
    path = new_plugin(kind, name, domain=domain)
    console.print(f"Created {path}")


if __name__ == "__main__":
    app()
