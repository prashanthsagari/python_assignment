import unittest
import BankAccount as ba

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = ba.BankAccount(1000)
    
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)
        
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 1050)
    
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-200)
            
    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 950)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_zero_balance_withdrawal(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)
        
if __name__ == '__main__':
    unittest.main()
