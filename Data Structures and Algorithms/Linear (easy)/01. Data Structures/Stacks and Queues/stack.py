# supports LIFO -> Last in first out ... access, remove from top

class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, value):
        self.s.append(value)

    # def push(self, value):
    #     self.s.insert(0, value)

    def isEmpty(self):
        return len(self.s) == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else: return self.s[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else: return self.s.pop()
        # else: print(self.s.pop(), "is deleted")


st = stack()

st.push(10)
st.push(20)
st.push(30)
st.push(40)

st.peek()
st.pop()
st.peek()

print(st.isEmpty())