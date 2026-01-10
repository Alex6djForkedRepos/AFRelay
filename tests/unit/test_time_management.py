from unittest.mock import patch

from service.time.time_management import generate_ntp_timestamp


def test_generate_ntp_timestamp():

    with patch('ntplib.NTPClient') as MockClient:
        instance = MockClient.return_value
        instance.request.return_value.tx_time = 1673356800

        epoch, gen_time, exp_time = generate_ntp_timestamp()

        assert epoch == 1673356800