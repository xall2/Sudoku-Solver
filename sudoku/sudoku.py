

def readsudokuEasy():
 
 list_of_lists = [] 
 with open('sudoku1.txt') as f:
     for line in f:
         inner_list = [int(elt.strip()) for elt in line.split(',')]
         list_of_lists.append(inner_list)
 return list_of_lists



def readsudokuMedium():
    
    list_of_lists = []
    with open('sudoku2.txt') as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split(',')]
            list_of_lists.append(inner_list)
    return list_of_lists



def readsudokuHard():
    
    list_of_lists = []
    with open('sudoku3.txt') as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split(',')]
            list_of_lists.append(inner_list)
    return list_of_lists

















