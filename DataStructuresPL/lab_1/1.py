# Exercises:
ex1 = True
ex2 = True
ex3 = False
ex4 = True

class Stack:
    def __init__(self, max_size: int, data_type: type):
        self.stack = []
        self.max_size = max_size
        self.data_type = data_type

    def push(self, element):
        """
        Append the element to the stack on the last place in the stack.
        """
        if len(self.stack) < self.max_size:
            if isinstance(element, self.data_type):
                self.stack.append(element)
            else:
                print(f'Wrong element type, which is actually {type(element)}. You have to provide {self.data_type} type.')
        else:
            print(f"Maximum size of the stack appeared. The maximum size of the stack is {self.max_size}")
        
    def pop(self):
        """
        Returns the last one element in the stack. The element which was added at the beggining.
        """
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            print("Stack is empty")


    def isempty(self):
        """
        Checks if the stack is empty, returning Bool value
        """
        return len(self.stack) == 0

    def top(self):
        """
        Returns the first one element in the stack. The element which was added lately
        """
        return self.stack[-1] if not self.isempty() else "Stack's empty"

# Testing the class Stack
if __name__ == "__main__" and ex1:
    stack = Stack(max_size=5,
                data_type=int)
    stack.push(2.5)
    print(f"Is stack empty? {stack.isempty()}")

    # Adding values to the stack
    stack.push(2)
    stack.push(3)
    stack.push(5)

    print(f"Is stack empty? {stack.isempty()}")

    print(stack.stack)
    print(stack.pop())
    print(stack.stack)
    print(stack.top())


if __name__ == "__main__" and ex2:
    first_string = "3 + 6 * 2" # -> 36 + 2 *

    print("\n")
    def exercise_2(number: str):
        # Brute force solution, adhoc
        number_list = number.split()
        number_list.append(None)
        
        numbers = Stack(len(number_list), data_type=int)
        i = 0
        output = ""
        operator = None
        operators = ['+', '-', '/', '*']

        for element in number_list:
            if element == None:
                for x in range(i):
                    output += numbers.pop()
                output += f" {operator}"
            elif element.isdigit():
                numbers.stack.append(element)
                i += 1
            elif element in operators:
                if operator == None:
                    operator = element
                else:
                    for x in range(i):
                        output += f" {numbers.pop()}"
                    output += f" {operator} "
                    operator = element
                    i = 0
        return output


    print(exercise_2(first_string))


if __name__ == "__main__" and ex3:
    first_string = "3 6 + 2 *" # 15
    def exercise_3(number: str):
        pass

if __name__ == "__main__" and ex4:
    print("\n")
    expression_1 = 12203022
    expression_2 = 3120213

    class Node:
        def __init__(self, data):
            self.data = data if data else None
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None
        
        def append(self, data):
            "adds element on the back of the linked list"
            new_node = Node(data=data)
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        def display(self):
            "displays chain of the linked list"
            current = self.head
            path = ""
            while current:
                path += f"{current.data} -> "
                current = current.next
            print(path, "Null")

        def get(self, n):
            "Returns n-index element of the linked list, starting from 0 index"
            current = self.head
            for i in range(n):
                current = current.next
            return current.data

    print("First part of the exercise")
    linked_list_1 = SinglyLinkedList()
    for i in str(expression_1):
        linked_list_1.append(i)
    linked_list_1.display()

    print("\nThe second part of the exercise")
    def is_palindrome(element) -> bool:
        element = str(element)
        stack_number = Stack(max_size=len(element), data_type=str)
        for i in element:
            stack_number.push(i)
        

        for i in range(len(element)):
            if element[i] != stack_number.pop():
                return False
        return True
    
    print(is_palindrome(expression_1))
    print(is_palindrome(1111))
    print(is_palindrome(expression_2))