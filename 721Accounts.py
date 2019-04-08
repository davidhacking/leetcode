# encoding=utf-8

from collections import defaultdict


class Solution(object):
    def root(self, mail):
        if mail not in self.union_list:
            self.union_list[mail] = mail
            self.root_size[mail] = 1
        while self.union_list[mail] != mail:
            # self.union_list[mail] = self.union_list[self.union_list[mail]]
            mail = self.union_list[mail]
        return mail

    def union(self, m1, m2):
        r1 = self.root(m1)
        r2 = self.root(m2)
        if self.root_size[r1] > self.root_size[r2]:
            self.union_list[r2] = r1
            self.root_size[r1] += self.root_size[r2]
        else:
            self.union_list[r1] = r2
            self.root_size[r2] += self.root_size[r1]

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        res = []
        mail2name = {}
        self.union_list = {}
        self.root_size = {}
        for i, account in enumerate(accounts):
            name = None
            last_mail = None
            for j, data in enumerate(account):
                if j == 0:
                    name = data
                else:
                    mail2name[data] = name
                    self.union(data, last_mail if last_mail else data)
                    last_mail = data

        mail2account = {}
        for mail in self.union_list.keys():
            root = self.root(mail)
            if root not in mail2account:
                mail2account[root] = set()
            mail2account[root].add(mail)
        for rmail, mails in mail2account.items():
            mails = list(mails)
            mails.sort()
            res.append([mail2name[rmail]] + mails)
        return res


if __name__ == '__main__':
    """
    [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
    """
    s = Solution()
    print s.accountsMerge([["David","David4@m.co","David2@m.co","David4@m.co"],["John","John7@m.co","John5@m.co","John3@m.co"],["Fern","Fern6@m.co","Fern4@m.co","Fern5@m.co"],["Celine","Celine0@m.co","Celine7@m.co","Celine7@m.co"],["Gabe","Gabe8@m.co","Gabe8@m.co","Gabe1@m.co"],["Ethan","Ethan1@m.co","Ethan6@m.co","Ethan6@m.co"],["Celine","Celine4@m.co","Celine8@m.co","Celine6@m.co"],["Celine","Celine0@m.co","Celine0@m.co","Celine4@m.co"]])
