from random import randint
import random
from generate import *
rules_amount=1000
rules_pf=10
mutation_rate=50
def ReadRulesFromFile(name):
    with open('rr/'+name+'.rule') as f:
        rules=f.readlines()
    rules = [x.strip() for x in rules]
    return rules
def MakePool(fitness):
    rules_pool=[]
    print('making pool')
    for i in range(0,len(fitness)):
        rules=ReadRulesFromFile(str(i))
        if(rules.count(':')!=0):
            rules.remove(':')
        for m in range(0,fitness[i]):
            rules_pool=rules_pool+rules
    print('made pool')
    return rules_pool
def GenerateDummyFitness():
    fitness=[]
    for i in range(0,rules_amount):
        fitness.append(randint(0,10))
    print('Generated Dummy Fitness')
    return fitness
def GenerateNewRules(rules_pool):
    new_rules=[':']
    for i in range(0,rules_pf):
        rule=random.choice(rules_pool)
        if(new_rules.count(rule)==0):
            new_rules.append(rule)
        else:
            while(len(new_rules)-1==i):
                new_rule=random.choice(rules_pool)
                if(new_rules.count(new_rule)==0):
                    new_rules.append(new_rule)
                
    return new_rules
def MutateRules(rules):
    rand=randint(0,1000)
    if(rand<mutation_rate):
        rules[randint(0,len(rules)-1)]=ReturnRandomRule()
    return rules
def Dummy():
    #call fitness function here
    rules_pool=MakePool(GenerateDummyFitness())
    for i in range(0,rules_amount):
        new_rules=GenerateNewRules(rules_pool)
        new_rules=MutateRules(new_rules)
        SaveRulesToFile(str(i),new_rules)
    print('done')
    
        
