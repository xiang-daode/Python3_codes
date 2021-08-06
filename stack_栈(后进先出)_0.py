# stack_栈(后进先出)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)#[3, 4, 5, 6, 7]
z=stack.pop()#z is 7
print(stack)#[3, 4, 5, 6]
z=stack.pop()#z is 6
z=stack.pop()#z is 5
print(stack)#[3, 4]
