from pathlib import Path

README = Path("README.md").read_text()

REQUIRED = [
    "urf-spine-public",
    "sanitized public audit surface",
    "URF spine layer",
    "public status surface",
    "citation metadata",
    "scope limitations",
    "external status lock",
    "minimal verifier",
    "minimal finite certificate example",
    "public audit surface only",
    "not theorem-prover-complete",
    "not a primary mathematics-closure repository",
    "unrestricted Chronos-RR",
    "unrestricted H4.1/FGL",
    "P vs NP",
    "Clay problem",
]

def test_urf_spine_public_index_block_present():
    for token in REQUIRED:
        assert token in README, token
