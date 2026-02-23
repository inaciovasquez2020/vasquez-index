from pathlib import Path

def test_registry_exists():
    assert Path("REGISTRY.md").exists()
