import typer
import pkgutil
import importlib
import sysprobe.modules

app = typer.Typer(help="Linux system diagnostic tool")

for _, name, _ in pkgutil.iter_modules(sysprobe.modules.__path__):

    def command(name=name):
        module = importlib.import_module(f"sysprobe.modules.{name}")
        module.run()

    app.command(name)(command)

if __name__ == "__main__":
    app()