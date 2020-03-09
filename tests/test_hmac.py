import hmac
import hashlib


def test_generate_hmac_hash(api_secret_key, request_date):
    try:
        hmac.new(
            bytes(api_secret_key, "UTF-8"), bytes(request_date, "UTF-8"), hashlib.sha1,
        ).hexdigest()
    except Exception as e:
        assert False
    assert True
