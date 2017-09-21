class emp:
    pass

class engineer(emp):
    pass

class pm(emp):
    pass

class hr(emp):
    pass


emp1 = emp()
engineer1 = engineer()

pm1 = pm()
hr1 = hr()

staffs = [(emp1, 'Employee1'), (engineer1, 'Enguneer1'),
          (pm1, 'Project Manager1'), (hr1, 'Human Resource')]

emp_classes = [emp, engineer, pm, hr]

for staff, name in staffs:
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        msg1 = 'is a' if isA else 'is not a'
        print name, msg1, emp_class.__name__

for class1  in emp_classes:
    for class2 in emp_classes:
        isSubclass = issubclass(class1, class2)
        message = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print class1.__name__, message, class2.__name__

