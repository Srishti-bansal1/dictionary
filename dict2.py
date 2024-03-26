MAX_HASH_TABLE_SIZE = 100

class Node:
    next:'Node' = None
    key, value = None, None
    def __init__(self,key, value) -> None:
        self.key = key
        self.value = value
    
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        return
    
    def set_next(self, nextNode:'Node'):
        self.next = nextNode

class HashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list:list[Node] = [None] * max_size
        
    def get_valid_index(self, key):
        return self.hash_function(key)
        
    def __getitem__(self, key):
        idx = self.get_valid_index(key)
        head = self.data_list[idx]
        return self.search_for_key(head, key)
    
    def search_for_key(self, head:Node, key):
        while head:
            if head.get_key() == key:
                return head.get_value()
            head = head.next
        raise KeyError
            
    
    def __setitem__(self, key, value):
        idx = self.get_valid_index(key)
        self.set_node(idx, key, value) 
        return True
    
    def __iter__(self):
        for head in self.data_list:
            while head:
                (x,y) = (head.get_key(),head.get_value())
                yield (x, y)
                head = head.next

                
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)
    
    def hash_function(self, key:str):
        count = 0
        for el in key:
            count+=ord(key)
        return count%MAX_HASH_TABLE_SIZE
    
    def set_node(self, idx, key, value):
        current_node = self.data_list[idx]
        end_node = None
        while(current_node):
            if current_node.get_key() == key:
                current_node.set_value(value)
                return
            end_node = current_node
            current_node = current_node.next
        newNode = Node(key=key, value=value)
        if end_node:
            end_node.set_next(newNode)
            return
        self.data_list[idx]= newNode
        




# Create a hash table
table = HashTable()

# Insert some key-value pairs
table['a'] = 1
table['b'] = 34
print(table['b'],table['a'])
# Retrieve the inserted values
table['a'] == 1 and table['b'] == 34
# Update a value
table['a'] = 99
# Check the updated value
table['a'] = 99
# Get a list of key-value pairs
#list(table) == [('a', 99), ('b', 34)]
print(table['a'])

l = [el for el in table]
print(l)