def analyze_scores(*scores):
    count=len(scores)
    if count==0:
        return 0,0,0
    su=sum(scores)
    average=su/count
    return su,count,average
def print_report(team_name, **info):
    print(f"{team_name}")
    for key,value in info.items():
        print(f"{key}:{value}")

analyz1=analyze_scores(8, 10, 7, 9)
print(analyz1)

analyz2=analyze_scores(5,5)
print(analyz2)

analyz3=analyze_scores()
print(analyz3)

team={"coach":"Влад","city":"Минск"}
print_report("Комета",**team)
