class Stack:
    def __init__(self):
        self.li = list()

    def push(self, item):
        self.li.append(item)

    def pop(self):
        if len(self.li) != 0:
            return self.li.pop()
        return "Stack is Empty"

    def peek(self):
        if len(self.li) != 0:
            item = self.li.pop()
            self.li.append(item)
            return item
        return "Stack is Empty"

    def is_empty(self):
        if len(self.li)==0:
            return True
        return False


if __name__ == '__main__':
    st = Stack()
    st.push(10)
    st.push(9)
    st.push(8)
    st.push(7)
    print(st.peek())
    print(st.pop())
    print(st.is_empty())


