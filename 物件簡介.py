# encoding=utf8

class Team:
    member = 7
    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    # 可以不用先形成物件就可以存取
    @classmethod
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x,y):
        return x ** y

myTeam = Team()
print 'total working hours', myTeam.all_working_hour()
print 'each working hour', myTeam.working_hour()
print 'get member', Team.get_member(), myTeam.get_member()
print 'calculate 3^5=', Team.calculate(3,5), 'calculate 2^4=', myTeam.calculate(2,4)