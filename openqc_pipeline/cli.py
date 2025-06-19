import typer

app = typer.Typer()


@app.command()
def validate(input: str):
    typer.echo(f"Validating input: {input}")


@app.command()
def visualize(type: str = "heatmap"):
    typer.echo(f"Generating {type} visualization...")


if __name__ == "__main__":
    app()
