def create_grid(size):
   """
   >>> create_grid(4)
   [['0', '0', '0', '0'], ['0', '0', '0', '0'],
    ['0', '0', '0', '0'], ['0', '0', '0', '0']]
   """
   grid = []
   for i in range(size):
       row = ['0']*size
       grid.append(row)

   return grid

if __name__ == "__main__":
    import doctest
    doctest.testmod()
