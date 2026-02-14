import platform
from utils.logger import log

def generate_report():
    system = platform.system()
    node = platform.node()

    log(f"System report generated for {node}")
    return {
        "system": system,
        "node": node
    }
