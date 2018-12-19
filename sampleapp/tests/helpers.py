from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

# 使いそうな日付変数
today = datetime.today().replace(hour=0, minute=0,
                                 second=0, microsecond=0)
day_before_yesterday = today + timedelta(days=-2)
yesterday = today + timedelta(days=-1)
tomorrow = today + timedelta(days=1)

three_weeks_ago = today + timedelta(days=-21)
two_month_ago = today + relativedelta(months=-2)


def is_iso_date_type(d):
    """入力文字列がISO標準の日付型であることを確認
    """
    try:
        parse(d)
        return True
    except ValueError:
        return False
