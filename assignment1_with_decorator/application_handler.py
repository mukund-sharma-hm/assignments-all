"""Application handling"""

import psutil
import decorator


instance = []

@decorator.logger
def monitor_app(process_name, max_instnace):
    """function to monitor the application"""
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == process_name:
            instance.append(process)

    if len(instance) > max_instnace:
        print(f"Killing {process_name} (more than {max_instnace})")
        instance[0].kill()
        print("killed process")
    else:
        print(f"Number of instances of {process_name}: {len(instance)}")
monitor_app('notepad.exe', 2)
