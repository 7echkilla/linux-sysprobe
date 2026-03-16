import typer
import pkgutil
import importlib
import probe.modules

app = typer.Typer(help="Linux system diagnostic tool")

for _, name, _ in pkgutil.iter_modules(probe.modules.__path__):

    def command(name=name):
        module = importlib.import_module(f"probe.modules.{name}")
        module.run()

    app.command(name)(command)

if __name__ == "__main__":
    app()