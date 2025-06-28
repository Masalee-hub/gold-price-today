"""
Application for update gold today
MODULARIZATION WITH FUNCTION
"""


def data_extraction():
    """
    Harga Emas Hari Ini, 28 Jun 2025
    Butik Emas LM Grahadipta - Jakarta

    Harga di-update setiap hari pkl. 08.30 WIB

    Berat	Harga Dasar	Harga (+Pajak PPh 0.25%)

    Emas Batangan :
    0.5 gr	992,000	994,480
    1 gr	1,884,000	1,888,710
    2 gr	3,708,000	3,717,270
    3 gr	5,537,000	5,550,843
    5 gr	9,195,000	9,217,988
    10 gr	18,335,000	18,380,838
    25 gr	45,712,000	45,826,280
    50 gr	91,345,000	91,573,363
    100 gr	182,612,000	183,068,530
    250 gr	456,265,000	457,405,663
    500 gr	912,320,000	914,600,800
    1000 gr	1,824,600,000	1,829,161,500
    :return:
    """

    r = dict()
    r['update gold today'] = 'June, 28 2025'
    r['prices are update daily at'] = '08:30 WIB'
    r['weight'] = ('0.5 gr','1 gr', '2 gr', '3 gr', '4 gr', '5 gr', '10 gr', '25 gr','50 gr',
                   '100 gr','250 gr','500 gr','1000 gr')
    r[
        "base price IDR"] = ('992,000','1,884,000','3,708,000','5,537,000','9,195,000','18,335,000',
                             '45,712,000','91,345,000','182,612,000','456,265,000','912,320,000',
                             '1,824,600,000')
    r['price +pph 0.25% IDR'] = (
        '994,480','1,888,710','3,717,270','5,550,843','9,217,988','18,380,838','45,826,280','91,573,363',
                                 '183,068,530','457,405,663','914,600,800','1,829,161,500')
    return r

def view_data(result):
    print('Update Price Gold Today source logammulia.com')
    print('\n')
    print(f"Update gold today {result['update gold today']}")
    print(f"prices are update daily at {result['prices are update daily at']}")
    print(f"weight {result['weight'][3]}")
    print(f"base price IDR {result['base price IDR'][3]}")
    print(f"price +pph 0.25% IDR {result['price +pph 0.25% IDR'][3]}")



if __name__ == '__main__':
    print('Main Application')
    print('\n')
    result = data_extraction()
    view_data(result)