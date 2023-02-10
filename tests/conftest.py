import os
import sys
from datetime import timedelta

import pytest
from hypothesis import settings

on_ci = bool(os.getenv('CI', False))
is_pypy = sys.implementation.name == 'pypy'
max_examples = settings.default.max_examples // (5 if is_pypy else 1)
settings.register_profile('default',
                          deadline=(timedelta(hours=1) / max_examples
                                    if on_ci
                                    else None),
                          max_examples=max_examples)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session: pytest.Session,
                         exitstatus: pytest.ExitCode) -> None:
    if exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED:
        session.exitstatus = pytest.ExitCode.OK
