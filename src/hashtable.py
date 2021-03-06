# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"<{self.key}, {self.value}>"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        ''' 
        index = self._hash_mod(key)
        hash_ = self.storage

        if hash_[index] is not None:
            new_hash = LinkedPair(key, value)
            new_hash.next = hash_[index] 
            hash_[index] = new_hash
        else:
            hash_[index] = LinkedPair(key,value)
        return

# the hash MVP:
        # index = self._hash_mod(key)

        # if self.storage[index] is not None:
        #     print('key in user')
        #     node = self.storage[index]
        #     while node.next:
        #         node = node.next

        #     node.next = LinkedPair(key,value)
        # else:
        #     self.storage[index] = LinkedPair(key,value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        cur = self.storage[index]

        if cur.key == key:
            self.storage[index] = cur.next
        if cur.key != key:
            while cur.next is not None:
                next = cur.next
                if next.key == key:
                    cur.next = next.next
            print("Warning: Key does not exist")

# the hash MVP:
        # index = self._hash_mod(key)
        # if self.storage[index] is None:
        #     self.storage[index] = None
        # else:
        #     print("Warning: Key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        cur = self.storage[index]

        if cur is not None:
            while cur:
                if cur.key is key:
                    return cur.value
                elif cur.next is not None:
                    cur = cur.next
        else:
            return None
# the hash MVP:
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     return self.storage[index]
        # else:
        #     return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        current = None
        for i in old_storage:
            current = i
            while current:
                self.insert(current.key, current.value)
                current = current.next
# the hash MVP:
        # #double capacity
        # self.capacity *=2
        # #store out storage before we nullify it
        # old_storage = self.storage
        # self.storage = None
        # #re-fit our storage to hold out capacity
        # self.storage = [None] * self.capacity

        # for item in old_storage:
        #     #must hash on insert, so instead of assigning item=item you gotta insert it
        #     self.insert(item.key, item.value)

        # self.capacity *= 2
        # new_storage = [None] * self.capacity 

        # for bucket_item in self.storage:
        #     if bucket_item is not None:
        #         new_index = self._hash_mod(bucket_item.key)
        #         new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)

        # self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

# Lecture notes:
# class LinkedPair:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#     def __repr__(self):
#         return f"<{self.key}, {self.value}>"
# class HashTable:
#     '''
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     '''
#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity
#     def _hash(self, key):
#         '''
#         Hash an arbitrary key and return an integer.
# ​
#         You may replace the Python hash with DJB2 as a stretch goal.
#         '''
#         return hash(key)
#     def _hash_djb2(self, key):
#         '''
#         Hash an arbitrary key using DJB2 hash
# ​
#         OPTIONAL STRETCH: Research and implement DJB2
#         '''
#         pass
#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity
#     def insert(self, key, value):
#         '''
#         Store the value with the given key.
# ​
#         # Part 1: Hash collisions should be handled with an error warning. (Think about and
#         # investigate the impact this will have on the tests)
# ​
#         # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
# ​
#         Fill this in.
#         '''
#         # Hashmod the key to find the bucket
#         index = self._hash_mod(key)
#         # Check if a pair already exists in the bucket
#         pair = self.storage[index]
#         if pair is not None:
#             # If so, overwrite the key/value and throw a warning
#             if pair.key != key:
#                 print("Warning: Overwriting value")
#                 pair.key = key
#             pair.value = value
#         else:
#             # If not, Create a new LinkedPair and place it in the bucket
#             self.storage[index] = LinkedPair(key, value)
#     def remove(self, key):
#         '''
#         Remove the value stored with the given key.
# ​
#         Print a warning if the key is not found.
# ​
#         Fill this in.
#         '''
#         index = self._hash_mod(key)
#         # Check if a pair exists in the bucket with matching keys
#         if self.storage[index] is not None and self.storage[index].key == key:
#             # If so, remove that pair
#             self.storage[index] = None
#         else:
#             # Else print warning
#             print("Warning: Key does not exist")
#     def retrieve(self, key):
#         '''
#         Retrieve the value stored with the given key.
# ​
#         Returns None if the key is not found.
# ​
#         Fill this in.
#         '''
#         # Get the index from hashmod
#         index = self._hash_mod(key)
#         # Check if a pair exists in the bucket with matching keys
#         if self.storage[index] is not None and self.storage[index].key == key:
#             # If so, return the value
#             return self.storage[index].value
#         else:
#             # Else return None
#             return None
#     def resize(self):
#         '''
#         Doubles the capacity of the hash table and
#         rehash all key/value pairs.
# ​
#         Fill this in.
#         '''
#         pass

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     # ht.insert("line_2", "Filled beyond capacity")
#     # ht.insert("line_3", "Linked list saves the day!")

#     print(ht.storage)

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     # print(ht.retrieve("line_2"))
#     # print(ht.retrieve("line_3"))

#     # Test resizing
#     # old_capacity = len(ht.storage)
#     # ht.resize()
#     # new_capacity = len(ht.storage)

#     # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # # Test if data intact after resizing
#     # print(ht.retrieve("line_1"))
#     # print(ht.retrieve("line_2"))
#     # print(ht.retrieve("line_3"))
#     # print("")