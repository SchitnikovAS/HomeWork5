immutable_var = 123, 25.0, 'Welcome', False
print(immutable_var)
mutable_list = [123, 25.0, 'Welcome', False]
mutable_list[0] = 'Hello'
mutable_list[-1] = True
mutable_list.append(12345)
mutable_list.extend(['Mister', 3.14])
print(mutable_list)