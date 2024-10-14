import random

from datetime import datetime
import logging
import sys

logger = logging.getLogger("__name__")
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('formatter.log')
formatter = logging.Formatter(fmt="%(asctime)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)



class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    logger.info(self.balance)
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      logger.info(f"PIN: {pin}")
      if pin != 1234:
        logger.warning("Error! Invalid pin. Try again.")
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      logger.info(f"Amount: {amount}")
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info(f"Current balance: {self.balance}")
      print("Amount Deposited: ${amount}".format(amount=amount))
      print("Transaction Info:")
      print("Status: Successful")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.warning("Error! You entered a non-number value to deposit.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      logger.info(f"Amount: {amount}")
      if self.balance >= amount:
        self.balance -= amount
        logger.info(f"Current balance: {self.balance}")
        print("You withdrew: ${amount}".format( amount=amount))
        print("Transaction Info:")
        print("Status: Successful")
        print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.warning("Error! Insufficient balance to complete withdraw.")
        print("Transaction Info:")
        print("Status: Failed")
        print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.warning("Error! You entered a non-number value to withdraw.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
