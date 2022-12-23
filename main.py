import shioaji as sj

# api = sj.Shioaji()
# accounts = api.login("YOUR_PERSON_ID", "YOUR_PASSWORD")
# api.activate_ca(
#     ca_path="/c/your/ca/path/Sinopac.pfx",
#     ca_passwd="YOUR_CA_PASSWORD",
#     person_id="Person of this Ca",
# )

import shioaji as sj
api = sj.Shioaji(simulation=True)
api.login("PAPIUSER01","2222")

api = sj.Shioaji(simulation=True)
accounts = api.login(
    person_id="PAPIUSER01", 
    passwd="2222", 
)

api.quote.subscribe(api.Contracts.Stocks["2330"], quote_type="tick")
api.quote.subscribe(api.Contracts.Stocks["2330"], quote_type="bidask")
api.quote.subscribe(api.Contracts.Futures["TXFC0"], quote_type="tick")

#%%
contract = api.Contracts.Stocks["2890"]
order = api.Order(
    price=12,
    quantity=5,
    action=sj.constant.Action.Buy,
    price_type=sj.constant.StockPriceType.LMT,
    order_type=sj.constant.StockOrderType.Common,
)
trade = api.place_order(contract, order)
