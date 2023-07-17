import typer
import socket
import psutil
from prettytable import PrettyTable

app = typer.Typer()


def get_open_ports():
    # Get a list of open ports
    open_ports = []
    for port in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', port))
            except socket.error:
                continue
            else:
                open_ports.append(port)

    # Create a table to display the open ports and processes
    table = PrettyTable()
    table.field_names = ["Port", "Process"]

    # Populate the table with the open ports and corresponding processes
    for port in open_ports:
        try:
            process = psutil.Process(psutil.net_connections()[0].pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, IndexError):
            process = "Unknown"
        table.add_row([port, process])

    return table


@app.command(name="list-ports")
def list_ports():
    table = get_open_ports()
    typer.echo(table)


if __name__ == "__main__":
    app()
