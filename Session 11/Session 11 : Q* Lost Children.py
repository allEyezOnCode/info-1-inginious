current = first_child
while current.next_child() != first_child:
    if not current.is_next_valid():
        return False
    current = current.next_child()
return True
