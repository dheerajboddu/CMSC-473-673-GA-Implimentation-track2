import os




def read_grammar(filename="./grammar.txt"):
    filename = os.path.join(os.curdir, filename)
    with open(filename) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []
        v = {}
        t = {}

        for rule in rules:
            left, right = rule.split(" -> ")

            # for two or more results from a variable
            right = right[:-1].split(" | ")
            for ri in right:

                # it is a terminal
                if str.islower(ri):
                    t_rules.append([left, ri])
                    t[ri] = left

                # it is a variable
                else:
                    v_rules.append([left, ri])
                    v[ri] = left
        return v, t


def read_input(filename="./input.txt"):
    """
    reads the inputs from a text file
    :param filename: name of the text file in current directory
    :return: list of inputs
    """
    filename = os.path.join(os.curdir, filename)
    res = []
    with open(filename) as inp:
        inputs = inp.readlines()
        for i in inputs:

            # remove \n
            st = i
    res = st.split()
    return res



def cyk_alg(varies, terms, inp):
    length = len(inp)
    Matrix = [[0 for x in range(length)] for y in range(length)] 
    blocks = []
    for i in range(length):
        Matrix[i][i] = terms[inp[i]] 
    for i in range(1,length):
        j=0
        a= j
        for k in range(j+i,length):
                blocks.append([a,k])
               # Matrix[a][k] = varies[Matrix[a][k]]
                if(k==length-1):
                    break
                a = a + 1
    for each in blocks:
        i,j = each
        a = i
        b = j
        while Matrix[a][j] == 0:
            j = j-1
        while Matrix[i][b] == 0:
            i = i+1   
        if Matrix[a][j]+" "+Matrix[i][b] in varies:
            if not (varies[Matrix[a][j]+" "+Matrix[i][b]] == 'S'):
                Matrix[a][b] = varies[Matrix[a][j]+" "+Matrix[i][b]]
            else:
                if(blocks.index(each)==len(blocks)-1):
                    Matrix[a][b] = varies[Matrix[a][j]+" "+Matrix[i][b]]
                    
    return Matrix

def show_result(tab, inp):
   
    print(tab)
    if tab[0][len(inp)-1] == 'S':
        print("The input belongs to this context free grammar!")
    else:
        print("The input does not belong to this context free grammar!")


if __name__ == '__main__':
    v, t = read_grammar()
    r = read_input()
    ta = cyk_alg(v, t, r)
    show_result(ta, r)
    
    
    
