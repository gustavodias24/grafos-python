sequencia = "AAAGGCGTTGAGGTT"

# abcd
# bcde
# cdef

# ab
# bc
# cd

salto = 4

# 2 = 1
# 4 = 3 
for i in range(len(sequencia) - (salto - 1)):
    print(sequencia[i:i+salto])
