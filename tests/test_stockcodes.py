import stockcodes
import pytest
import os.path, time


@pytest.fixture(scope='module')
def stock_codes():
    codes = stockcodes.StockCodes()
    return codes


@pytest.mark.parametrize("sid, exp_name", [('2330', '台積電')])
def test_stock_codes_get_stock_name(stock_codes, sid, exp_name):
    name = stock_codes.get_stock_name(sid)
    assert name == exp_name

