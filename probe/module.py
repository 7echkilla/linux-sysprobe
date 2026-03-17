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
                self.run()

        # Explicit subcommand
        app.command()(self.run)

        return app

    def run(self):
        data = self.get_data()
        print(data)