from brownie import accounts, config, SimpleStorage, network

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage.retrieve())
    storage_transaction = simple_storage.store(77, {"from": account})
    storage_transaction.wait(1)
    print(simple_storage.retrieve())


def deploySimpleStorage():
    account = accounts.load("freecodecamp-account")
    print("acc", account)


def main():
    # deploySimpleStorage()
    deploy()
