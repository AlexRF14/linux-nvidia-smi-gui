import subprocess
import time
from rich.live import Live
from rich.table import Table

def get_gpu_data():
    cmd = [
        'nvidia-smi', 
        '--query-gpu=name,memory.used,memory.total,utilization.gpu,temperature.gpu', 
        '--format=csv,noheader,nounits'
    ]
    result = subprocess.check_output(cmd).decode('utf-8').strip()
    return result.split(', ')

def generate_table():
    name, used, total, util, temp = get_gpu_data()
    
    table = Table(title="NVIDIA GPU Monitor", border_style="bright_blue")
    table.add_column("Modelo", style="cyan")
    table.add_column("Memoria", style="magenta")
    table.add_column("Carga", style="yellow")
    table.add_column("Temp", style="red")
    
    table.add_row(
        name, 
        f"{used} / {total} MB", 
        f"{util}%", 
        f"{temp}°C"
    )
    return table

try:
    with Live(generate_table(), refresh_per_second=2) as live:
        while True:
            time.sleep(0.5)
            live.update(generate_table())
except KeyboardInterrupt:
    print("\nMonitor detenido.")