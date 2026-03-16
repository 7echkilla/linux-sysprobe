import typer

from probe.loader import load_plugins

app = typer.Typer(help="Linux system diagnostic tool")
plugins = load_plugins()

for plugin in plugins.values():
    app.add_typer(plugin.get_app(), name=plugin.name)

if __name__ == "__main__":
    app()