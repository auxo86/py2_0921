class Emp():
    gradeLevel = 6
    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    pass

class PM(Emp):
    pass


print '1.[RD grade level]', RD.gradeLevel
print '1.[PM grade level]', PM.gradeLevel

PM.gradeLevel = 8
print '2.[RD grade level]', RD.gradeLevel
print '2.[PM grade level]', PM.gradeLevel

Emp.gradeLevel = 7

print '3.[RD grade level]', RD.gradeLevel
print '3.[PM grade level]', PM.gradeLevel