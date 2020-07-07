from src.b import b_fn
from unittest.mock import patch


def a_mocked():
    print('hello from a_mocked')


# Note that to mock a_fn inside module `b`, you must mock the path `src.b.a_fn`
with patch('src.b.a_fn', return_value='mocked!', side_effect=a_mocked):
    b_fn()
