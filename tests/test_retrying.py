from app.retrying import retry


def test_retry_succeeds_after_failures():
    calls = {"n": 0}

    @retry(times=3, delay=0)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError
        return "ok"

    assert flaky() == "ok"
