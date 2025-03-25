import time
import random
from rich.console import Console
from rich.live import Live
from rich.table import Table
from multiprocessing import Process, Manager

"""Showcasing a simple progress bar for multiple parallel processes using rich and multiprocessing.
The task came up since tqdm does not work well with multiprocessing and the console output
is thus not as readable as with this solution. 

Detailled logging could/should go into dedicated log files from each process.
On the console this solution gives a clean overview of the state of each process.

Example output:

```bash
$ python training/python/progress_bar_for_parallel_processes.py
 Sensor 1:             │ --------------x                                                                                                           | 12%                                                                                                                                  
 Sensor 2:             │ ----------------x                                                                                                         | 14%                                                                                                                                  
 Sensor 3:             │ --------------x                                                                                                           | 12%
```

"""


def sensor_progress(sensor_name, progress_dict):
    """Dummy function to simulate updates of varying speed."""
    for i in range(1, 101):  # Progress from 1% to 100%
        progress_dict[sensor_name] = i
        time.sleep(random.uniform(0.05, 0.2))  # Simulating varying sensor speeds


def render_progress(progress_dict):
    """Renders the progress of each sensor in a rich table."""
    table = Table(show_edge=False, show_header=False, expand=True)

    for sensor, progress in progress_dict.items():
        bar_length = 120  # Adjust width of progress bar
        num_chars = int(progress / 100 * bar_length)
        bar = "-" * num_chars + "x" + " " * (bar_length - num_chars)
        table.add_row(f"{sensor}:", f"[cyan]{bar}[/cyan] | {progress}%")

    return table


def main():
    console = Console()
    manager = Manager()
    progress_dict = manager.dict({f"Sensor {i + 1}": 0 for i in range(3)})  # 3 sensors

    # Start the (dummy) sensor processes functions.
    processes = [Process(target=sensor_progress, args=(sensor, progress_dict)) for sensor in progress_dict]
    for p in processes:
        p.start()

    # Progress bar in a rich table.
    with Live(render_progress(progress_dict), console=console, refresh_per_second=2) as live:
        while any(p.is_alive() for p in processes):
            live.update(render_progress(progress_dict))
            time.sleep(0.5)  # Refresh rate

    # Ensure all processes finish.
    for p in processes:
        p.join()

    console.print("\n[bold green]All sensors finished![/bold green]")


if __name__ == "__main__":
    main()
