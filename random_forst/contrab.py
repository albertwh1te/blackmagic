#!/webapps/xueqiu_predict/python3_env/bin/python
import gevent.monkey
from gevent.pool import Pool
from crawler import crawl_stocks_followers, crawl_stocks_prices
from utils import engine
from sqlalchemy.orm import sessionmaker
from models import Stock, StockDetail
gevent.monkey.patch_all()
Session = sessionmaker(bind=engine)
session1 = Session()

stocks_list = []
for stock in session1.query(Stock):
    stocks_list.append((stock.code, stock.id))

p = Pool(4)


# def followers_into_sql(code, stock_id):
def followers_into_sql(a):
    code = a[0]
    stock_id = a[1]
    followers = crawl_stocks_followers(code)
    current_prices = crawl_stocks_prices(code)
    print(followers, current_prices)
    new_detail = StockDetail(
        followers=followers,
        stock_id=stock_id,
        current_prices=current_prices,
    )
    print(new_detail.stock_id)
    session2 = Session()
    session2.add(new_detail)
    session2.commit()
    print("done", new_detail.followers)
    session2.close()

print(stocks_list[10:])
p.map(followers_into_sql, stocks_list)
p.join()

