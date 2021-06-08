# self type defenitions
from __future__ import annotations

from typing import Any

import random



class Node():
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList():
    def __init__(self, head=None) -> None:
        self.head = Node(head)

    def append(self, data: Any) -> None:
        new_node = Node(data)

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def print(self) -> None:
        current_node = self.head.next
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def print_tree(self) -> None:
        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.data, '->', current_node.next.data)
            else:
                print(current_node.data, '->', current_node.next)

            current_node = current_node.next
    
    def remove(self, data: Any) -> None:
        current_node = self.head.next
        if current_node and current_node.data == data:
            self.head.next = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return
        
        previous_node.next = current_node.next
        current_node = None
    
    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head.next
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        
        self.head.next = previous_node
    
    # def reverse_recursive(self) -> None:
    #     def _reverse_recursive(current_node: None, previous_node: None):
    #         if current_node is None:
    #             return previous_node
    #         next_node = current_node.next
    #         current_node.next = previous_node

    #         previous_node = current_node
    #         current_node = next_node
    #         return _reverse_recursive(current_node,previous_node)
        
    #     self.head.next = _reverse_recursive(self.head.next, None)
    
    def restrictive_reverse_recursive(self, start_node:Node, end_node: Node = None) -> None:
        def _restrictive_reverse_recursive(current_node: None, previous_node: None):
            if current_node is end_node:
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
            return _restrictive_reverse_recursive(current_node, previous_node)
        
        start_node.next = _restrictive_reverse_recursive(start_node.next, end_node)
    

    def reverse_recursive(self) -> None:
        self.restrictive_reverse_recursive(self.head,None)
    

    def reverse_even(self) -> None:
        current_node = self.head
        start_node = self.head
        end_node = None
        while current_node:
            next_node = current_node.next
            if current_node.data and next_node:
                if current_node.data % 2 and not next_node.data % 2:
                    start_node = current_node
                elif not current_node.data % 2 and (next_node.data % 2 or not next_node):
                    end_node = next_node
                    self.restrictive_reverse_recursive(start_node,end_node)
            elif not next_node:
                end_node = None
                self.restrictive_reverse_recursive(start_node,end_node)

            # if end_node:
            #     print(current_node.data,start_node.data,end_node.data)
            # else:
            #     print(current_node.data,start_node.data,end_node)
            current_node = next_node
        # print(current_node)

            




if __name__=='__main__':
    l = LinkedList()
    # l.append(1)
    # l.append(2)
    # l.append(3)
    # l.insert(0)
    # l.print()
    # print('#'*10)
    # l.reverse_iterative()
    # l.print()
    # print('#'*10)
    # l.reverse_recursive()
    # l.print()
    l.append(2)
    l.append(4)
    l.append(1)
    l.append(4)
    l.append(6)
    l.append(8)
    l.append(9)
    l.append(3)
    l.append(4)
    l.append(6)
    l.append(8)
    l.append(9)
    # for i in range(1000):
    #     l.append(random.randint(0,100))
    l.print_tree()
    print('#'*50)
    l.reverse_even()
    print('#'*50)
    l.print_tree()