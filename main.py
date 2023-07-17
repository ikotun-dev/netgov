import typer
import psutil

app = typer.Typer()


@app.command()
def ports():
    # Get all network connections
    connections = psutil.net_connections()

    # Filter the connections to include only TCP and UDP connections
    network_connections = [conn for conn in connections if conn.status == psutil.CONN_ESTABLISHED]

    # Print the open ports and the corresponding process names
    for conn in network_connections:
        typer.echo(f"Port: {conn.laddr.port} - Process: {psutil.Process(conn.pid).name()}")


@app.command()
def close(port: int):
    # Iterate over all network connections
    for conn in psutil.net_connections():
        if conn.status == psutil.CONN_ESTABLISHED and conn.laddr.port == port:
            # Terminate the process that is using the specified port
            psutil.Process(conn.pid).kill()
            typer.echo(f"Port {port} closed successfully.")
            return

    typer.echo(f"No process found using port {port}.")


if __name__ == "__main__":
    app()
