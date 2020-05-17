class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity;

    def fnv1(self, key):
        hval = 0x811c9dc5

        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
            
        # print(hval)
        return hval

    # def djb2(self, key):
        # hash = 5381;
        # c = 0;

        # while (c = len(key)):
        #     hash = ((hash << 5) + hash) + c * hash * 33 + c *
        #     c =+ 1
        # return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        self.size += 1
        index = self.hash_index(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = HashTableEntry(key,value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = HashTableEntry(key,value)

    def delete(self, key):
        index = self.hash_index(key)
        node = self.buckets[index]
        prev = node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -=1
            result = node.value
            if prev is None:
                node = None
            else:
                if prev.next  != None:
                    prev.next = prev.next.next
            return result

        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

    def get(self, key):
        index = self.hash_index(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

    def resize(self, n):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        new_hash = [] * n
        self.capacity = n
        for i in self.buckets:
            if i != None:
                new_index = self.hash_index[i[1]]
                new_hash[new_index] = (i.key,i.value)
        self.buckets = new_hash

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
