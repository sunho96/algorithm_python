from structures import LinkedList, Stack, Queue
from prac import isPalindrome, test_problem_stack, test_problem_queue

li = LinkedList()
for num in [1,2,2,1]:
    li.append(num)

li2 = LinkedList()
for num in [1,2]:
    li2.append(num)

assert isPalindrome(li)
assert not isPalindrome(li2)

def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()



assert test_problem_stack("()")
assert test_problem_stack("()[]{}")
assert test_problem_stack("({[][]})")
assert test_problem_stack("({[]})")
assert not test_problem_stack("(]")
assert not test_problem_stack("(()]")
assert not test_problem_stack("(((])")
assert not test_problem_stack("((())")


def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()

    assert test_problem_queue(2) == 2
    assert test_problem_queue(3) == 2
    assert test_problem_queue(4) == 4
    assert test_problem_queue(5) == 2
    assert test_problem_queue(6) == 4
    assert test_problem_queue(7) == 6