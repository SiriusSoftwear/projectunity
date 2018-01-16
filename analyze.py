from mutate import *
rules_amount=1000
def AnalyzeRules():
    rules_pool=[]
    not_unique=0
    for i in range(0,rules_amount):
        rules=ReadRulesFromFile(str(i))
        if(rules.count(':')!=0):
            rules.remove(':')
        rules_pool=rules_pool+rules
    uniq_rules=[]
    for m in range(0,len(rules_pool)-1):
        if(uniq_rules.count(rules_pool[m])==0):
            uniq_rules.append(rules_pool[m])
        else:
            not_unique=not_unique+1
    print('unique rules:  '+str(len(uniq_rules)))
    print('clones:  '+str(not_unique))
GenerateRandomRules()
AnalyzeRules()
for i in range(0,100):
    Dummy()
    AnalyzeRules()
