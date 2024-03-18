class SuperList(list):
    def __len__(self):
        print("len of SuperList is called!")
        return super().__len__()


super_list1 = SuperList()
super_list1.append(5)
super_list1.append(6)
print(len(super_list1))

print(issubclass(SuperList, list))
print(issubclass(list, object))
