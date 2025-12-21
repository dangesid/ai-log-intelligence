import typer 
import requests
from rich import print

app = typer.Typer()

API_URL = "http://127.0.0.1:8000"

@app.command()
def ingest(path: str):
    """
    Ingest logs from a file or directory
    """
    logs = []

    try:
        with open(path,"r") as f:
            logs = f.readlines()
    except IsADirectoryError:
        print("[red] Directory ingestion coming next[/red]")
        raise typer.Exit(1)
    
    payload = {"logs": logs}
    r = requests.post(f"{API_URL}/ingest", json=payload)

    if r.status_code == 200:
        print(f"[green] Ingested {len(logs)} logs successfully[/green]")
    else:
        print(f"[red] Failed to ingest logs: {r.text} [/red]")

@app.command()
def query(question: str):
    """
    Ask AI about Logs 
    """
    payload = {"query": question}
    r = requests.post(f"{API_URL}/query", json=payload)

    if r.status_code == 200:
        print("[red]Query failed[/red]", r.text)
        raise typer.Exit(1)
    
    data = r.json()
    print("\n[bold_cyan] Rettrieved Logs: [/bold_cyan]")
    for log in data["retrieved_logs"]:
        print(f"- {log}")

    print("\n[bold_green] AI Response: [/bold_green]")
    print(data["answer"])

if __name__ == "__main__":
    app()
    