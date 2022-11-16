# Questão 2.1
print('Questão 2.1:')

array = []
for i in range(1, 101):
  array.append(i)
array[50] = None


def achaFaltando(arr):
  for j in range(1, 101):
    if arr[j] == None:
      try:
        missing = j
      except:
        missing = 100

      print(missing)
      break


achaFaltando(array)

print()
print()

# Questão 2.3
print('Questão 2.3')

nums = [2, 7, 11, 15]
target = 9

# Criando a hash table com os números do array sendo as chaves, e os índices sendo os valores
hash = {nums[i]: i for i in range(0, len(nums))}

# Pegando o complemento do alvo - o valor do inteiro do array
for i in range(0, len(nums)):
  complement = target - nums[i]
  # Verifica se o complemento é uma chave e se o valor dessa chave não é o índice atual
  if complement in hash.keys() and hash.get(complement) is not i:
    print([i, hash.get(complement)])
    break

print()
# Questão 2.4
print('Questão 2.4:')

class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def removeDuplicates(self):
    temp = self.head
    if temp is None:
      return
    while temp.next is not None:
      if temp.data == temp.next.data:
        temp.next = temp.next.next
      else:
        temp = temp.next
      
  def printList(self):
    temp = self.head
    while (temp):
      print(temp.data, end=' ')
      temp = temp.next


lista = LinkedList()
lista.push(5)
lista.push(5)
lista.push(4)
lista.push(3)
lista.push(3)
lista.push(2)
lista.push(1)
lista.push(1)


lista.printList()

print()
print()

lista.removeDuplicates()

lista.printList()
print()
print()

# Questão 2.5
print('Questão 2.5')

class Node:

  def __init__(self, key):

    self.data = key
    self.left = None
    self.right = None


def insert(root, x):

  if (root == None):
    return Node(x)
  if (x < root.data):
    root.left = insert(root.left, x)
  elif (x > root.data):
    root.right = insert(root.right, x)
  return root


def kthSmallest(root):

  global k

  if (root == None):
    return None

  left = kthSmallest(root.left)

  if (left != None):
    return left

  k -= 1
  if (k == 0):
    return root

  return kthSmallest(root.right)


root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for x in keys:
  root = insert(root, x)

k = 6

print()

print("k = " + str(k))
print("Menor k-ésimo número da árvore = " + str(kthSmallest(root).data))
