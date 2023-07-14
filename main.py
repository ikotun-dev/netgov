
import typer
import psutil

app = typer.Typer()


@app.command()
def ports():
    # Get the list of running processes
    processes = psutil.process_iter(['pid', 'name'])

    # Refresh the process information
    processes = [p.info for p in processes]

    # Filter the processes to only include network-related processes
    network_processes = [p for p in processes if p.get('name') in ['tcp', 'udp']]

    # Print the open ports and the corresponding process names
    for proc in network_processes:
        connections = proc.connections()
        for conn in connections:
            typer.echo(f"Port: {conn.laddr.port} - Process: {proc['name']}")


@app.command()
def close(port: int):
    # Iterate over the network processes
    for proc in psutil.process_iter(['pid', 'name']):
        proc_info = proc.info

        # Refresh the process information
        proc_info = proc_info if proc_info else proc.info

        connections = proc_info.connections()
        for conn in connections:
            if conn.laddr.port == port:
                # Terminate the process that is using the specified port
                proc.kill()
                typer.echo(f"Port {port} closed successfully.")
                return

    typer.echo(f"No process found using port {port}.")


if __name__ == "__main__":
    app()
