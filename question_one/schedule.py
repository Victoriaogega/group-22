from operator import itemgetter

def scheduling(tasks):
    for task in tasks:
        print(sorted(tasks, key = lambda x : x['deadline'] ))
        

        



tasks = [
    {'taskname':'cleaning','deadline':1400},
    {'taskname':'NYJ','deadline':1800},
    {'taskname':'DAS','deadline':1200}
]



   