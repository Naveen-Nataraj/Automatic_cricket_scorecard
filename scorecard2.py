class Batsmen:
    run = 0  # Runs scored
    fours = 0  # Number of fours scored
    sixes = 0  # Number of sixes scored
    balls = 0  # Number of balls faced
    sr = 0  # Strike Rate

    def __init__(self, name):
        self.name = name

    def update_run(self, r):
        self.run += r
        self.balls += 1
        if r == 4:
            self.fours += 1
        elif r == 6:
            self.sixes += 1
        if self.balls != 0:
            self.sr = self.run * 100 / self.balls  # Strike rate calculation


class Bowlers:
    run = 0  # Runs given
    over = 0  # Number of overs
    balls = 0  # Number of balls bowled before it is counted as over(<6)
    wicket = 0  # Number of wickets
    extras = 0  # Extras given

    def __init__(self, name):
        self.name = name

    def update_run(self, r):
        self.run += r
        self.balls += 1
        if self.balls == 6:
            self.update_over()

    def update_over(self):
        self.over += 1
        self.balls = 0
        self.eco = self.run / self.over

    def update_wicket(self):
        self.wicket += 1

    def update_extras(self, r):
        self.extras += r

t_overs=2       #Total number of overs
n_batsmen = 3  # Number of batsmen
bat_lst = list()
print("Enter the names of batsmen")
for i in range(n_batsmen):
    batsman = Batsmen(input())  # Collecting the names of the batsmen.
    bat_lst.append(batsman)  # List of batsmen (Type:Batsmen)

n_bowlers = 3  # Number of bowlers
bowl_lst = list()
print("Enter the names of bowlers")
for i in range(n_bowlers):
    bowler = Bowlers(input())  # Collecting the names of the bowlers
    bowl_lst.append(bowler)  # List of bowlers (Type:Bowlers)

i = 0               # Striker batsman
j = 1  # Non striker batsman
k = 0  # bowler number
overs = 0  # Overs count
balls = 0  # Balls count
score = 0  # Overall Score
wickets = 0  # Overall wickets
extras = 0  # Overall Extras
freehit = 0  # freehit flag variable
run_lst = ['0','1', '2', '3', '4', '6']  # Allowed runs
while True:  # Overs less than total number of overs
    r = input("Enter the number of runs scored or W/Wd/Nb\t{}.{}\t".format(overs, balls))
    if r in run_lst:
        bat_lst[i].update_run(int(r))
        bowl_lst[k].update_run(int(r))
        if r in ['1', '3']:
            i, j = j, i
            print("Batsman:{}".format(bat_lst[i].name))
        score += int(r)
    elif r.upper() == 'W':
        if freehit == 1:
            print("Not out!,It is a freehit")
            continue
        try:
            i = max(i, j) + 1
            print("Batsman:{}".format(bat_lst[i].name))
            bowl_lst[k].update_wicket()
            wickets += 1
        except IndexError:
            print("\n\nAll out!!!")
            wickets += 1
            break
    elif r.upper() == 'WD':
        print("Enter the runs scored in wide ball\t{}.{}".format(overs, balls), end='\t')
        r_wd = input()
        balls -= 1
        if r_wd in run_lst:
            bowl_lst[k].update_extras(int(r_wd) + 1)
            score += int(r_wd) + 1
            extras += int(r_wd) + 1
            if r_wd in ['1','3']:
                i,j=j,i
                print("Batsman:{}".format(bat_lst[i].name))
        else:
            bowl_lst[k].update_extras(1)
            score += 1
            extras += 1
    elif r.upper() == "NB":
        print("Enter the runs scored in no ball\t{}.{}".format(overs, balls), end='\t')
        r_wd = input()
        balls -= 1
        freehit = 2
        if r_wd in run_lst:
            bowl_lst[k].update_extras(int(r_wd) + 1)
            bat_lst[i].update_run(int(r_wd))
            bat_lst[i].balls -= 1
            score += int(r_wd) + 1
            extras += int(r_wd) + 1
            if r_wd in ['1','3']:
                i,j=j,i
                print("Batsman:{}".format(bat_lst[i].name))
        else:
            bowl_lst[k].update_extras(1)
            score += 1
            extras += 1
    else:
        print("Invalid input")
        continue
    balls += 1
    if balls == 6:
        overs += 1
        if overs<t_overs:
            balls = 0
            print("over up")
            i, j = j, i
            print("Batsman:{}".format(bat_lst[i].name))
            k += 1
            print("Bowler:{}".format(bowl_lst[k].name))
        else:
            print("The match is finished!!!")
            break
    if freehit == 2:
        print("Next ball is a free hit!!")
    freehit -= 1
  
print("Score:{}/{}\t\t\tExtras:{}".format(score, wickets, extras))
print("Name\tRuns\tBalls\tFours\tSixes\tStrike Rate")
for i in range(n_batsmen):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{:.2f}".format(bat_lst[i].name, bat_lst[i].run, bat_lst[i].balls, bat_lst[i].fours,
                                              bat_lst[i].sixes, bat_lst[i].sr))

print("Name\tRuns\tOvers\tExtras")
for i in range(n_bowlers):
    print("{}\t\t{}\t\t{}.{}\t\t{}".format(bowl_lst[i].name, bowl_lst[i].run, bowl_lst[i].over, bowl_lst[i].balls, bowl_lst[i].extras))
