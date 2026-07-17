"""Smoke import test."""

def test_import():
    from loggerplus import RobustLogger
    assert RobustLogger is not None
