import subprocess
import sys

def test_urf11_translation_subproblem_registry_index_entry():
    subprocess.run(
        [sys.executable, "tools/verify_urf11_translation_subproblem_registry_index_entry.py"],
        check=True,
    )
