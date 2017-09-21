# encoding=utf8

class Emp():
    gradeLevel = 6
    def startWorking(self):
        pass
    def endWorking(self):
        pass

class RD(Emp):
    def __init__(self):
        self.currentGreade = self.gradeLevel

    def startWorking(self):
        print 'RD work: ', self.currentGreade

    def endWorking(self):
        print 'RD end work', self.currentGreade

rd1 = RD()
rd1.currentGreade = 7
rd1.startWorking()
print 'rd1 grade = ', rd1.currentGreade, '\n', 'Level', rd1.gradeLevel
