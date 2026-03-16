import typer

from abc import ABC, abstractmethod

class Plugin(ABC):
    """Base class for plugin structure"""

    name = "unknown"
    description = "none"

    @abstractmethod
    def collect(self):
        """Return structured diagnostic data"""
        pass

    # def get_app(self):
    #     "Generate a Typer app for the plugin"

    #     app = typer.Typer(help=self.description)
    #     app.command()(self.run)
    #     return app

    # def run(self):
    #     data = self.collect()

    #     for metric, value in data.items():
    #         print(f"{metric}: {value}")

    def get_app(self):
        """Generate and return a Typer app for the plugin."""
        app = typer.Typer(help=self.description)

        # Register the run method as a Typer command
        @app.command()
        def run():
            data = self.collect()
            for metric, value in data.items():
                print(f"{metric}: {value}")

        return app

