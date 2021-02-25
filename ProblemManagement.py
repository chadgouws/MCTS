# File Name

# @ Author: Chad Gouws
# Date: 10/01/2020


class Insurance:

    def __init__(self):
        self.weekly_return = 0.0015

    def investment_return(self, cash_at_beginning_of_week):
        return cash_at_beginning_of_week * (1 + self.weekly_return)

    def cash_flow(self):

