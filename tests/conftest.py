"""Keep calculator tests offline and prevent writes to real report files."""
from unittest.mock import patch

import pytest


def pytest_configure(config):
    # nisab fetches prices at import time, before fixtures can run.
    patches = [
        patch("app.services.price.gold_price", return_value=4242.0),
        patch("app.services.price.silver_price", return_value=50.0),
    ]
    for price_patch in patches:
        price_patch.start()
        config.add_cleanup(price_patch.stop)


@pytest.fixture(autouse=True)
def disable_report_writes(monkeypatch):
    from app.utils.nisab import Sako

    monkeypatch.setattr(Sako, "data_collection", lambda *args, **kwargs: None)
