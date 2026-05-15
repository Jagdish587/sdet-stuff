# tests/ui/test_ui.py

import pytest


@pytest.mark.ui
def test_ui_user_name(sample_user):
    assert sample_user["name"] == "Alice"


@pytest.mark.ui
def test_normal_user_role(normal_user):
    assert normal_user["role"] == "user"


@pytest.mark.ui
def test_auth_token(auth_token):
    assert auth_token.startswith("jwt")