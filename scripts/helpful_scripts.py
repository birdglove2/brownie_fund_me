from brownie import network, config, accounts, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS \
      or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
      
def deploy_mocks():
  print("The active network is ", network.show_active())
  print("Deploying Mocks...")
    
  # no need to mock address more than 1 in the network
  if len(MockV3Aggregator) <= 0:  
    MockV3Aggregator.deploy(DECIMALS,
                           STARTING_PRICE, 
                            {"from": get_account()})
      
  print("Mocks Deployed!")  