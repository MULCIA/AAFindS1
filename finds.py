training_set = [((1,1),1),((3,4),1),((2,2),1),((4,7),0)]

def hypothesis_funcion(example, iteration):
    x = example[0]
    y = example[1]
    return ((x**2) + (y**2) <= (iteration**2))

def findS():
    hypothesis = ['0','0']
    count = 0
    for example in training_set:
        if example[1] == 1:
            if hypothesis_funcion(example[0],count+1) == False:
                example_attribute = example[0][0]
                hypothesis_attribute = hypothesis[0]
                if example_attribute != hypothesis_attribute:
                    if hypothesis_attribute == '0':
                        hypothesis_attribute = example[0][0]
                    elif hypothesis_attribute != '0' and hypothesis_attribute != '?':
                        hypothesis_attribute = '?'
                hypothesis[0] = hypothesis_attribute
                example_attribute = example[0][1]
                hypothesis_attribute = hypothesis[1]
                if example_attribute != hypothesis_attribute:
                    if hypothesis_attribute == '0':
                        hypothesis_attribute = example[0][1]
                    elif hypothesis_attribute != '0' and hypothesis_attribute != '?':
                        hypothesis_attribute = '?'
                hypothesis[1] = hypothesis_attribute
        count += 1
    return hypothesis

if __name__ == "__main__":
    print("Final hypothesis: " + str(findS()))