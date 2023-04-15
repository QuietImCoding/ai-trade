from utils import * 

## Instantiate trader class -- DONE
## Implements trade(in, amount, out), queryPrice(token), -- TODO
## Instantiate openai class -- DONE ish

trader = TradeBot()
ai = ChatGPT()


while trader.getEthBalances > 10:
    trades = ai.update(trader.queryMarket)
    for t in trades:
        decTrade = ai.parse_commands(t)
        trader.execute_trades(t)

## TODO -- implement sending money off to other address every "day"
## TODO -- implement posting to / getting feedback off lens
## internet no work :'((( 

        
