from brownie import SimpleStorage, accounts

def test_deploy():
  # Arrange 
  account = accounts[0]

  # Act
  simple_storage = SimpleStorage.deploy({"from": account})
  starting_value = simple_storage.retrieve()

  # Assert
  assert starting_value == 0

def test_updating_storage():
  # Arrange 
  account = accounts[0]

  # Act
  simple_storage = SimpleStorage.deploy({"from": account})
  simple_storage.store(15, {"from": account})
  updated_value = simple_storage.retrieve()

  #Assert
  assert updated_value == 15

