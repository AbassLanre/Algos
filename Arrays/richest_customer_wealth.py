def maximumWealth(self, accounts: List[List[int]]) -> int:
    maxCustomer = []
    for i in range(len(accounts)):
        maxCustomer.append(sum(accounts[i]))

    return max(maxCustomer)