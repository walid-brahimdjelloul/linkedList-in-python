from Node import Node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    

    def get_head(self):
        return self.head
    
    def insert_begineer(self, node_value):
        new_node = Node(node_value)
        new_node.set_next_node(self.head)
        self.head = new_node
    
    def print_node_from_linkedList(self):
        all_nodes = ''
        current_node = self.get_head()
        while current_node:
            if current_node.get_value() != None:
                all_nodes += str(current_node.get_value()) + "-->"
            
            current_node = current_node.get_next_node()
        return all_nodes
    
    def delete_node(self, remove_node):
        current_node = self.get_head()
        if current_node.get_value() == remove_node:
            self.head = current_node.get_next_node()
        
        else:
            while current_node:
                if current_node.get_next_node().get_value() == remove_node:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    current_node = None
                else:
                    current_node = current_node.get_next_node()
    
    def swap(input_list, val1, val2):
        node1 = input_list.head
        node2 = input_list.head
        pre_node1 = None
        pre_node2 = None

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        while node1 is not None:
            if node1.get_value() == val1:
                break
            pre_node1 = node1
            node1 = node1.get_next_node()
        
        while node2 is not None:
            if node2.get_value() == val2:
                break
            pre_node2 = node2
            node2 = node2.get_next_node()

        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return
        
        if pre_node1 is None:
            input_list.head = node2
        
        else:
            pre_node1.set_next_node(node2)
        
        if pre_node2 is None:
            input_list.head = node1
        
        else:
            pre_node2.set_next_node(node1)
        
        temp = node1.get_next_node()
        node1.set_next_node(node2.set_next_node())
        node2.set_next_node(temp)