from logical_expression import *

model = {}
model['M_1_1'] = False
model['M_1_2'] = False
model['M_2_2'] = False
model['M_2_1'] = False
model['S_3_2'] = True
model['S_2_3'] = True
model['P_2_2'] = True

statement = logical_expression()
sub1 = logical_expression()
sub2 = logical_expression()
sub3 = logical_expression()
#sub1.symbol[0] = 'M_1_1'
sub1.symbol[0] = 'S_3_2'
#sub2.symbol[0] = 'M_2_2'
sub2.symbol[0] = 'S_2_3'
sub3.symbol[0] = 'P_2_2'
statement.connective[0] = 'and'
#statement.subexpressions.append(sub1)
#statement.subexpressions.append(sub2)
#statement.subexpressions.append(sub3)

print(pl_true(statement, model))

#Assuming proper input for each (didn't test cause im assuming valid takes care of this)
#And passed tests
#Or passed tests
#If passed tests
#iff passed tests
#not passed tests
#xor passed tests
