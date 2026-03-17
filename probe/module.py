import typer

from abc import ABC, abstractmethod

class Module(ABC):
    def __init__(self):
        """
        Define the base class structure for modules
        """
        self.name = "unknown"
        self.description = "no description"

    @abstractmethod
    def get_data(self):
        """Return structured diagnostic data"""
        pass

    def get_app(self):
        """
        Generate app command for Typer extension
        """
        app = typer.Typer(help=self.description)

        # Default behaviour when no subcommand is provided
        @app.callback(invoke_without_command=True)
        def main(context: typer.Context):
            if (context.invoked_subcommand is None):
                self.print_data()

        # Explicit subcommand
        app.command()(self.get_data)

        return app

    def print_data(self):
        data = self.get_data()
        format = " | ".join(f"{metric}: {value}" for metric, value in data.items())

        print(f"{self.name:10} {format}")