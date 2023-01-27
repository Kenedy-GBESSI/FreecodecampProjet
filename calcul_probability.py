import copy
import random

def get_tab(dic):
    tab = []
    for key,val in dic.items():
        for i in range(val):
            tab.append(key)
    return tab

class Hat:

    def __init__(self,**kwargs) -> None:
        self.contents = get_tab(kwargs)
 
    def draw(self,n_to_drawer):
        generator_tabs = []
        for i in range(n_to_drawer):
            rand_index = random.randrange(len(self.contents))
            generator_tabs.append(self.contents.pop(rand_index))
        return generator_tabs
       
def compare_l(list_1, list_2):
    tab = []
    list_copy = list_1[:]
    for i in list_2:
        for j in list_copy:
            if i==j:
                list_copy.remove(i)
                tab.append(True)
                break
    return all(tab) and len(tab)==len(list_2)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if(num_balls_drawn > len(hat.contents)):
        return 1
    else:
        M = 0;balls_we_expect = get_tab(expected_balls)
        hat_new = copy.deepcopy(hat)
        for i in range(num_experiments):
            experiment_current = hat_new.draw(num_balls_drawn)
            if(compare_l(experiment_current,balls_we_expect)==True):
                M +=1
            hat_new = copy.deepcopy(hat)
        return M/num_experiments

   

hat = Hat(blue=3,red=2,green=6)
print(hat.contents,end="\n\n")

print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
print(compare_l(['blue', 'blue', 'green', 'green'],['blue','blue','green']))
