from src.transfer.data_transfer_generator import create_external_id


def test_create_external_id():
    result = create_external_id()

    assert isinstance(result, str)
    assert all(number.isnumeric() for number in result)
    assert len(result) == 15
