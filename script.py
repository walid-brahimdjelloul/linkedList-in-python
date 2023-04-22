from linkedList import LinkedList

obj_list = LinkedList(5)
obj_list.insert_begineer(7)
obj_list.insert_begineer(9)
obj_list.insert_begineer(24)
obj_list.insert_begineer(36)
obj_list.insert_begineer(15)

print(obj_list.print_node_from_linkedList())

obj_list.delete_node(36)
print(obj_list.print_node_from_linkedList())