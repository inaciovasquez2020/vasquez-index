import subprocess


def test_vasquez_index_urf_core_textbook_cslib_fmt_signal_update():
    subprocess.run(
        [
            "python3",
            "-B",
            "tools/verify_vasquez_index_urf_core_textbook_cslib_fmt_signal_update.py",
        ],
        check=True,
    )
