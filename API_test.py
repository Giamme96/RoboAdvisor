

import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError


def import_share(azione):

    my_share = share.Share(azione)
    share_data = None

    try:
        share_data = my_share.get_historical(share.PERIOD_TYPE_YEAR, 1, share.FREQUENCY_TYPE_MONTH, 1)

    except YahooFinanceError as exc:
        print(exc.message)
        sys.exit(1)

    print(share_data)








import_share('MSFT')