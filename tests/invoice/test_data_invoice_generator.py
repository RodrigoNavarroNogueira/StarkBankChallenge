import pytest

from src.invoice import data_invoice_generator


@pytest.mark.parametrize(
    'value, expected_value', [
        ([0, 4, 8, 1, 4, 3, 2, 0, 3], 5),
        ([9, 4, 8, 9, 4, 9, 9, 7, 3], 0),

    ]
)
def test__calcula_digito(value, expected_value):
        result = data_invoice_generator._calcula_digito(value)
        assert result == expected_value


def test_cpf(mocker):
    mocker.patch.object(
        data_invoice_generator,
        '_calcula_digito',
        return_value=0
    )

    result = data_invoice_generator.cpf()

    assert result[-2:] == '00'
    assert len(result) == 14
