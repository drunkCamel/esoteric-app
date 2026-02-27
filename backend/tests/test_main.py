import pytest

from app.main import read_root


@pytest.mark.unit
def test_read_root():
    response = read_root()
    assert response == {"message": "Hello from FastAPI!"}
    

