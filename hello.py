import typer

app = typer.Typer()

@app.command()
def hello(name: str, age: int):
    print(f"hello {name}, age {age}")
@app.command()
def goodbye():
    print("goodbye")
if __name__ == "__main__":
    app()
