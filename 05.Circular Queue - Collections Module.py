from collections import deque

circular = deque(maxlen=5)
circular.append(1)
circular.append(2)
circular.append(3)
circular.append(4)
circular.append(5)
circular.append(6)
circular.append(7)

print(circular)