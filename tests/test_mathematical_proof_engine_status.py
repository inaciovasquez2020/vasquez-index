from pathlib import Path

DOC = Path("docs/status/MATHEMATICAL_PROOF_ENGINE_STATUS_2026_05_01.md")

def test_doc_exists():
    assert DOC.exists()

def test_conditional_lock_present():
    text = DOC.read_text()
    assert "Conditional." in text
    assert "Build success is an integrity signal only. It is not theorem-level closure." in text

def test_no_unconditional_major_claim():
    text = DOC.read_text().lower()
    forbidden = [
        "p≠np is proved",
        "yang–mills is solved",
        "navier–stokes is solved",
        "riemann hypothesis is proved",
        "hodge conjecture is proved",
        "clay problem solved",
    ]
    for phrase in forbidden:
        assert phrase not in text

def test_score_present():
    text = DOC.read_text()
    assert "Estimated proof-engine score:" in text
    assert "theorem/lemma declarations:" in text
    assert "sorry count:" in text
    assert "admit count:" in text
    assert "axiom count:" in text
