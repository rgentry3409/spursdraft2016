# Spurs Draft MMXVI
# By Ryan Gentry
# PA Kassandra Smith
# This is a game based on the draft on the 2K MyTeam Central and
# the mode MyLEAGUE on the game NBA 2K16.

# This imports libraries for the game to call from, and sets the salary cap.
import math
import random
import statistics
import sys
SCOVR = 82

# This is the introduction that describes how to play the game. 
print("")
print("Welcome to SPURS DRAFT MMXVI")
print("by Ryan Gentry")
print("")
print("In this game, you take on the role of R.C. Buford, general manager of")
print("the San Antonio Spurs going into the 2015-16 season of the NBA!")
print("However, it seems that the NBA has gotten mixed up and you have to")
print("draft a new team straight from scratch!")
print("You are creating a NEW SPURS TEAM to play against the other 29 in the NBA!")
print("")
print("In case you don't know how basketball works, there are five positions.")
print("Point guard: the ball handler, maker of plays")
print("Shooting guard: self-explanatory, can shoot threes, can make assists")
print("Small forward: most athletic player, good on offense and defense")
print("Power forward: like SF, but more defensive, large force in the paint")
print("Center: most significant role, tallest on team, gets rebounds, force")
print("on offense and defense")
print("")
print("There will be one player from each position on the floor at the start")
print("of the game. This is your starting lineup. There will also be one more")
print("player of each position, creating your bench lineup.")
print("")
aseirghteri = input("Press Enter to continue: ")
print("")
print("In this game, you will have five random players to choose from in each")
print("position, for starting five and bench players. You can tell how good a")
print("player is based on his \"overall\" rating (abbreviated OVR), a score")
print("out of 100 based on the player's overall strengths. The league's very")
print("best players have overalls over 90, the good stars have ratings over 85,")
print("other good players have ratings over 80, and key role players have")
print("ratings over 75. This info comes from the game NBA 2K16.")
print("")
print("The players available to pick for your starting lineup will generally")
print("have better overall ratings than your bench players.")
print("")
print("That said, teams in the NBA have what is known as a \"salary cap\",")
print("which is an amount of money they cannot exceed when paying their players.")
print("You have the option of having a salary cap measured in total overall")
print("that you cannot exceed. IF you choose this option, you cannot draft a")
print("team whose combined overall is greater than " + str(10*SCOVR) + ", creating an average")
print("overall of " + str(SCOVR) + ". This will be known as the \"Hard\" version of the game.")
print("You also have the option of creating a team without a salary cap,")
print("allowing you to draft as many great players as you can without worrying")
print("about money. That said, which option will you choose?")
print("")
print("Note: You will probably win the championship if you play the easy mode.")
print("")
print("1. Easy")
print("2. Hard")
# This is the selection for difficulty.
diff = input("Type 1 or 2: ")
if diff == "1":
    print("You have chosen Easy.")
elif diff == "2":
    print("You have chosen Hard.")
elif diff == "sc": # This is a secret difficulty option allowing the user to change the salary cap.
    print("You have chosen Hard.")
    SCOVR = float(input("New salary cap: "))
else:
    print("Bad selection.")
    sys.exit(0)

if diff == "1":
    diff = 1
elif diff == "2" or diff == "sc":
    diff = 2

# List of every position and score

# This info comes from the game NBA 2K16 and was found at 2KMTCentral.com.
# The "MT" is a secret scale from ~2500 to ~3700 determining player stats.
# It's not shown to users because it's a technical rating as opposed to the
# "for-show" overall rating (which is easier to make a salary cap around),
# but they match up generally.

# These players are listed in order of their MT.
PGList = ["Russell Westbrook","Stephen Curry","Chris Paul","John Wall","Kyle Lowry","Damian Lillard","Eric Bledsoe","Kyrie Irving","Rajon Rondo","Kemba Walker","Shaun Livingston","Jrue Holiday","Reggie Jackson","Derrick Rose","Michael Carter-Williams","Mike Conley","Isaiah Thomas","Goran Dragic","Deron Williams","Tony Parker","Marcus Smart","Jeff Teague","Mario Chalmers","Brandon Knight"]
PGMTList = [3660,3412,3383,3321,3256,3239,3236,3125,3095,3094,3054,3044,3043,3028,3015,2007,2994,2982,2961,2955,2947,2946,2936,2925]
PGOVRList = [95,96,92,89,86,89,86,88,83,84,76,82,83,80,76,83,86,80,78,79,74,79,76,80]
PGAvgMT = statistics.mean(PGMTList)
PGAvgOVR = statistics.mean(PGOVRList)

SGList = ["James Harden","Klay Thompson","Dwyane Wade","Jimmy Butler","DeMar DeRozan","Kobe Bryant","Victor Oladipo","Andre Roberson","Khris Middleton","Wesley Matthews","Tony Allen","Lance Stephenson","Bradley Beal","Avery Bradley","Manu Ginobili","Will Barton","C.J. McCollum","Rodney Hood","Kentavious Caldwell-Pope","Monta Ellis","Danny Green","Alec Burke","Zach LaVine","J.R. Smith","Eric Gordon"]
SGMTList = [3434,3420,3414,3395,3310,3069,3058,3028,3025,3018,3004,3002,2988,2982,2955,2939,2930,2926,2919,2919,2913,2908,2908,2900,2898]
SGOVRList = [92,90,87,88,88,79,79,75,81,78,78,75,79,80,80,79,83,79,78,78,76,78,78,77,77]
SGAvgMT = statistics.mean(SGMTList)
SGAvgOVR = statistics.mean(SGOVRList)

SFList = ["LeBron James","Kawhi Leonard","Kevin Durant","Paul George","Carmelo Anthony","Giannis Antetokounmpo","Jae Crowder","Nicolas Batum","Andrew Wiggins","Gordon Hayward","Andre Iguodala","Rudy Gay","Tyreke Evans","Chandler Parsons","Michael Kidd-Gilchrist","Luol Deng","Al-Farouq Aminu","Jeff Green","Evan Turner","Wilson Chandler","Danilo Gallinari","Tobias Harris","Harrison Barnes","Kent Bazemore","Derrick Williams"]
SFMTList = [3721,3597,3517,3454,3399,3225,3144,3122,3115,3107,3104,3067,3051,3049,3048,3038,3032,3004,3003,3000,2996,2981,2969,2961,2960]
SFOVRList = [96,94,94,90,88,84,84,81,80,81,83,79,80,81,80,79,80,79,76,78,77,81,79,77,76,74]
SFAvgMT = statistics.mean(SGMTList)
SFAvgOVR = statistics.mean(SGOVRList)

PFList = ["Anthony Davis","Draymond Green","Blake Griffin","Paul Millsap","LaMarcus Aldridge","Chris Bosh","Derrick Favors","Kevin Love","Jabari Parker","Dirk Nowitzki","Kristaps Porzingis","Thaddeus Young","Serge Ibaka","Aaron Gordon","Terrence Jones","Kenneth Faried","Nikola Mirotic","Zach Randolph","Julius Randle","Michael Beasley","Boris Diaw","Markieff Morris","Marvin Williams","Amir Johnson","Mirza Teletovic"]
PFMTList = [3619,3619,3508,3492,3291,3265,3207,3160,3126,3122,3104,3101,3083,3071,3051,3046,3021,3020,2995,2991,2989,2988,2982,2980,2969]
PFOVRList = [91,89,88,87,89,85,85,83,78,85,80,79,79,77,74,80,75,80,76,78,75,76,77,77,76]
PFAvgMT = statistics.mean(PFMTList)
PFAvgOVR = statistics.mean(PFOVRList)

CList = ["DeMarcus Cousins","Karl-Anthony Towns","Andre Drummond","Pau Gasol","Hassan Whiteside","Al Horford","Marc Gasol","Brook Lopez","DeAndre Jordan","Nikola Vucevic","Jared Sullinger","Greg Monroe","Dwight Howard","Jonas Valanciunas","Marcin Gortat","Gorgui Dieng","Mason Plumlee","Tim Duncan","Al Jefferson","Kelly Olynyk","Tristan Thompson","Nerlens Noel","Amar'e Stoudemire","Enes Kanter","Marreese Speights"]
CMTList = [3512,3310,3233,3231,3214,3214,3211,3064,3054,3027,3025,3010,3008,3001,2997,2992,2979,2974,2962,2960,2940,2938,2931,2929,2922]
COVRList = [90,86,89,85,86,80,82,84,84,82,77,79,83,83,80,77,77,80,80,76,78,76,76,80,75]
CAvgMT = statistics.mean(CMTList)
CAvgOVR = statistics.mean(COVRList)

AvgMT = ((PGAvgMT+SGAvgMT+SFAvgMT+PFAvgMT+CAvgMT)/5) # variables of the average player
AvgOVR = (PGAvgOVR+SGAvgOVR+SFAvgOVR+PFAvgOVR+CAvgOVR)/5

DTOVR = 0 # variables about the team that increase as the draft progresses
DAOVR = 0

print("")
print("")
draft = True
# This is a while loop that determines whether or not to start a draft.
# this is repeated if at the end of the game, the user decides
# to play again.
while draft == True:

    # Point guard selection

    PGNumber = random.sample(range(15),5)# This gets five random PGs
#                                          from the top 15 PGs.
#                                          (The list is in descending order of MT.)
#                                          Bench positions select from
#                                          the top 25 players in
#                                          their respective position,
#                                          giving the starting five better odds.
    PG1 = PGList[int(PGNumber[0])]# This gets the stats of the five PGs
    PG1MT = PGMTList[int(PGNumber[0])]# That were chosen from the random number
    PG1OVR = PGOVRList[int(PGNumber[0])]# generator.

    PG2 = PGList[int(PGNumber[1])]
    PG2MT = PGMTList[int(PGNumber[1])]
    PG2OVR = PGOVRList[int(PGNumber[1])]

    PG3 = PGList[int(PGNumber[2])]
    PG3MT = PGMTList[int(PGNumber[2])]
    PG3OVR = PGOVRList[int(PGNumber[2])]

    PG4 = PGList[int(PGNumber[3])]
    PG4MT = PGMTList[int(PGNumber[3])]
    PG4OVR = PGOVRList[int(PGNumber[3])]

    PG5 = PGList[int(PGNumber[4])]
    PG5MT = PGMTList[int(PGNumber[4])]
    PG5OVR = PGOVRList[int(PGNumber[4])]

    print ("POINT GUARD SELECTION")
    print ("") # Here is where the user selects their PG.
    print ("Choose between these players. ")
    print ("Type 1 for " + PG1 + " (OVR " + str(PG1OVR) + ").")
    print ("Type 2 for " + PG2 + " (OVR " + str(PG2OVR) + ").")
    print ("Type 3 for " + PG3 + " (OVR " + str(PG3OVR) + ").")
    print ("Type 4 for " + PG4 + " (OVR " + str(PG4OVR) + ").")
    print ("Type 5 for " + PG5 + " (OVR " + str(PG5OVR) + ").")
    PGChoose = input("Choose: ") # Here is where the chosen player's stats
    if PGChoose == "1":#                  are imported into the team.
        PG = PG1
        PGMT = PG1MT
        PGOVR = PG1OVR
    elif PGChoose == "2":
        PG = PG2
        PGMT = PG2MT
        PGOVR = PG2OVR
    elif PGChoose == "3":
        PG = PG3
        PGMT = PG3MT
        PGOVR = PG3OVR
    elif PGChoose == "4":
        PG = PG4
        PGMT = PG4MT
        PGOVR = PG4OVR
    elif PGChoose == "5":
        PG = PG5
        PGMT = PG5MT
        PGOVR = PG5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += PGOVR # Here is where the average and total overalls are calculated.
    DAOVR = PGOVR
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")
    # Then the above method is repeated for every draft position.

    # Shooting guard selection

    SGNumber = random.sample(range(15),5)

    SG1 = SGList[int(SGNumber[0])]
    SG1MT = SGMTList[int(SGNumber[0])]
    SG1OVR = SGOVRList[int(SGNumber[0])]

    SG2 = SGList[int(SGNumber[1])]
    SG2MT = SGMTList[int(SGNumber[1])]
    SG2OVR = SGOVRList[int(SGNumber[1])]

    SG3 = SGList[int(SGNumber[2])]
    SG3MT = SGMTList[int(SGNumber[2])]
    SG3OVR = SGOVRList[int(SGNumber[2])]

    SG4 = SGList[int(SGNumber[3])]
    SG4MT = SGMTList[int(SGNumber[3])]
    SG4OVR = SGOVRList[int(SGNumber[3])]

    SG5 = SGList[int(SGNumber[4])]
    SG5MT = SGMTList[int(SGNumber[4])]
    SG5OVR = SGOVRList[int(SGNumber[4])]

    print ("SHOOTING GUARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + SG1 + " (OVR " + str(SG1OVR) + ").")
    print ("Type 2 for " + SG2 + " (OVR " + str(SG2OVR) + ").")
    print ("Type 3 for " + SG3 + " (OVR " + str(SG3OVR) + ").")
    print ("Type 4 for " + SG4 + " (OVR " + str(SG4OVR) + ").")
    print ("Type 5 for " + SG5 + " (OVR " + str(SG5OVR) + ").")
    SGChoose = input("Choose: ")
    if SGChoose == "1":
        SG = SG1
        SGMT = SG1MT
        SGOVR = SG1OVR
    elif SGChoose == "2":
        SG = SG2
        SGMT = SG2MT
        SGOVR = SG2OVR
    elif SGChoose == "3":
        SG = SG3
        SGMT = SG3MT
        SGOVR = SG3OVR
    elif SGChoose == "4":
        SG = SG4
        SGMT = SG4MT
        SGOVR = SG4OVR
    elif SGChoose == "5":
        SG = SG5
        SGMT = SG5MT
        SGOVR = SG5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += SGOVR
    DAOVR = (PGOVR+SGOVR)/2
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # Small forward selection

    SFNumber = random.sample(range(15),5)

    SF1 = SFList[int(SFNumber[0])]
    SF1MT = SFMTList[int(SFNumber[0])]
    SF1OVR = SFOVRList[int(SFNumber[0])]

    SF2 = SFList[int(SFNumber[1])]
    SF2MT = SFMTList[int(SFNumber[1])]
    SF2OVR = SFOVRList[int(SFNumber[1])]

    SF3 = SFList[int(SFNumber[2])]
    SF3MT = SFMTList[int(SFNumber[2])]
    SF3OVR = SFOVRList[int(SFNumber[2])]

    SF4 = SFList[int(SFNumber[3])]
    SF4MT = SFMTList[int(SFNumber[3])]
    SF4OVR = SFOVRList[int(SFNumber[3])]

    SF5 = SFList[int(SFNumber[4])]
    SF5MT = SFMTList[int(SFNumber[4])]
    SF5OVR = SFOVRList[int(SFNumber[4])]

    print ("SMALL FORWARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + SF1 + " (OVR " + str(SF1OVR) + ").")
    print ("Type 2 for " + SF2 + " (OVR " + str(SF2OVR) + ").")
    print ("Type 3 for " + SF3 + " (OVR " + str(SF3OVR) + ").")
    print ("Type 4 for " + SF4 + " (OVR " + str(SF4OVR) + ").")
    print ("Type 5 for " + SF5 + " (OVR " + str(SF5OVR) + ").")
    SFChoose = input("Choose: ")
    if SFChoose == "1":
        SF = SF1
        SFMT = SF1MT
        SFOVR = SF1OVR
    elif SFChoose == "2":
        SF = SF2
        SFMT = SF2MT
        SFOVR = SF2OVR
    elif SFChoose == "3":
        SF = SF3
        SFMT = SF3MT
        SFOVR = SF3OVR
    elif SFChoose == "4":
        SF = SF4
        SFMT = SF4MT
        SFOVR = SF4OVR
    elif SFChoose == "5":
        SF = SF5
        SFMT = SF5MT
        SFOVR = SF5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += SFOVR
    DAOVR = (PGOVR+SGOVR+SFOVR)/3
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # Power forward selection

    PFNumber = random.sample(range(15),5)

    PF1 = PFList[int(PFNumber[0])]
    PF1MT = PFMTList[int(PFNumber[0])]
    PF1OVR = PFOVRList[int(PFNumber[0])]

    PF2 = PFList[int(PFNumber[1])]
    PF2MT = PFMTList[int(PFNumber[1])]
    PF2OVR = PFOVRList[int(PFNumber[1])]

    PF3 = PFList[int(PFNumber[2])]
    PF3MT = PFMTList[int(PFNumber[2])]
    PF3OVR = PFOVRList[int(PFNumber[2])]

    PF4 = PFList[int(PFNumber[3])]
    PF4MT = PFMTList[int(PFNumber[3])]
    PF4OVR = PFOVRList[int(PFNumber[3])]

    PF5 = PFList[int(PFNumber[4])]
    PF5MT = PFMTList[int(PFNumber[4])]
    PF5OVR = PFOVRList[int(PFNumber[4])]

    print ("POWER FORWARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + PF1 + " (OVR " + str(PF1OVR) + ").")
    print ("Type 2 for " + PF2 + " (OVR " + str(PF2OVR) + ").")
    print ("Type 3 for " + PF3 + " (OVR " + str(PF3OVR) + ").")
    print ("Type 4 for " + PF4 + " (OVR " + str(PF4OVR) + ").")
    print ("Type 5 for " + PF5 + " (OVR " + str(PF5OVR) + ").")
    PFChoose = input("Choose: ")
    if PFChoose == "1":
        PF = PF1
        PFMT = PF1MT
        PFOVR = PF1OVR
    elif PFChoose == "2":
        PF = PF2
        PFMT = PF2MT
        PFOVR = PF2OVR
    elif PFChoose == "3":
        PF = PF3
        PFMT = PF3MT
        PFOVR = PF3OVR
    elif PFChoose == "4":
        PF = PF4
        PFMT = PF4MT
        PFOVR = PF4OVR
    elif PFChoose == "5":
        PF = PF5
        PFMT = PF5MT
        PFOVR = PF5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += PFOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR)/4
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # Center selection

    CNumber = random.sample(range(15),5)

    C1 = CList[int(CNumber[0])]
    C1MT = CMTList[int(CNumber[0])]
    C1OVR = COVRList[int(CNumber[0])]

    C2 = CList[int(CNumber[1])]
    C2MT = CMTList[int(CNumber[1])]
    C2OVR = COVRList[int(CNumber[1])]

    C3 = CList[int(CNumber[2])]
    C3MT = CMTList[int(CNumber[2])]
    C3OVR = COVRList[int(CNumber[2])]

    C4 = CList[int(CNumber[3])]
    C4MT = CMTList[int(CNumber[3])]
    C4OVR = COVRList[int(CNumber[3])]

    C5 = CList[int(CNumber[4])]
    C5MT = CMTList[int(CNumber[4])]
    C5OVR = COVRList[int(CNumber[4])]

    print ("CENTER SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + C1 + " (OVR " + str(C1OVR) + ").")
    print ("Type 2 for " + C2 + " (OVR " + str(C2OVR) + ").")
    print ("Type 3 for " + C3 + " (OVR " + str(C3OVR) + ").")
    print ("Type 4 for " + C4 + " (OVR " + str(C4OVR) + ").")
    print ("Type 5 for " + C5 + " (OVR " + str(C5OVR) + ").")
    CChoose = input("Choose: ")
    if CChoose == "1":
        C = C1
        CMT = C1MT
        COVR = C1OVR
    elif CChoose == "2":
        C = C2
        CMT = C2MT
        COVR = C2OVR
    elif CChoose == "3":
        C = C3
        CMT = C3MT
        COVR = C3OVR
    elif CChoose == "4":
        C = C4
        CMT = C4MT
        COVR = C4OVR
    elif CChoose == "5":
        C = C5
        CMT = C5MT
        COVR = C5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += COVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR)/5
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")


    # END STARTING LINEUP SELECTIONS

    # START BENCH SELECTIONS

    # BENCH POINT GUARD SELECTION

    BPGNumber = random.sample(range(24),5) # Notice how this number is 24, as
#                                            opposed to the starters' 15.
#                                            This gives the bench players
#                                            not as good odds as the starters.
    BPG1 = PGList[int(BPGNumber[0])]
    BPG1MT = PGMTList[int(BPGNumber[0])]
    BPG1OVR = PGOVRList[int(BPGNumber[0])]

    BPG2 = PGList[int(BPGNumber[1])]
    BPG2MT = PGMTList[int(BPGNumber[1])]
    BPG2OVR = PGOVRList[int(BPGNumber[1])]

    BPG3 = PGList[int(BPGNumber[2])]
    BPG3MT = PGMTList[int(BPGNumber[2])]
    BPG3OVR = PGOVRList[int(BPGNumber[2])]

    BPG4 = PGList[int(BPGNumber[3])]
    BPG4MT = PGMTList[int(BPGNumber[3])]
    BPG4OVR = PGOVRList[int(BPGNumber[3])]

    BPG5 = PGList[int(BPGNumber[4])]
    BPG5MT = PGMTList[int(BPGNumber[4])]
    BPG5OVR = PGOVRList[int(BPGNumber[4])]

    print ("BENCH POINT GUARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + BPG1 + " (OVR " + str(BPG1OVR) + ").")
    print ("Type 2 for " + BPG2 + " (OVR " + str(BPG2OVR) + ").")
    print ("Type 3 for " + BPG3 + " (OVR " + str(BPG3OVR) + ").")
    print ("Type 4 for " + BPG4 + " (OVR " + str(BPG4OVR) + ").")
    print ("Type 5 for " + BPG5 + " (OVR " + str(BPG5OVR) + ").")
    BPGChoose = input("Choose: ")
    if BPGChoose == "1":
        BPG = BPG1
        BPGMT = BPG1MT
        BPGOVR = BPG1OVR
    elif BPGChoose == "2":
        BPG = BPG2
        BPGMT = BPG2MT
        BPGOVR = BPG2OVR
    elif BPGChoose == "3":
        BPG = BPG3
        BPGMT = BPG3MT
        BPGOVR = BPG3OVR
    elif BPGChoose == "4":
        BPG = BPG4
        BPGMT = BPG4MT
        BPGOVR = BPG4OVR
    elif BPGChoose == "5":
        BPG = BPG5
        BPGMT = BPG5MT
        BPGOVR = BPG5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += BPGOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR)/6
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # BENCH SHOOTING GUARD SELECTION

    BSGNumber = random.sample(range(24),5)

    BSG1 = SGList[int(BSGNumber[0])]
    BSG1MT = SGMTList[int(BSGNumber[0])]
    BSG1OVR = SGOVRList[int(BSGNumber[0])]

    BSG2 = SGList[int(BSGNumber[1])]
    BSG2MT = SGMTList[int(BSGNumber[1])]
    BSG2OVR = SGOVRList[int(BSGNumber[1])]

    BSG3 = SGList[int(BSGNumber[2])]
    BSG3MT = SGMTList[int(BSGNumber[2])]
    BSG3OVR = SGOVRList[int(BSGNumber[2])]

    BSG4 = SGList[int(BSGNumber[3])]
    BSG4MT = SGMTList[int(BSGNumber[3])]
    BSG4OVR = SGOVRList[int(BSGNumber[3])]

    BSG5 = SGList[int(BSGNumber[4])]
    BSG5MT = SGMTList[int(BSGNumber[4])]
    BSG5OVR = SGOVRList[int(BSGNumber[4])]

    print ("BENCH SHOOTING GUARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + BSG1 + " (OVR " + str(BSG1OVR) + ").")
    print ("Type 2 for " + BSG2 + " (OVR " + str(BSG2OVR) + ").")
    print ("Type 3 for " + BSG3 + " (OVR " + str(BSG3OVR) + ").")
    print ("Type 4 for " + BSG4 + " (OVR " + str(BSG4OVR) + ").")
    print ("Type 5 for " + BSG5 + " (OVR " + str(BSG5OVR) + ").")
    BSGChoose = input("Choose: ")
    if BSGChoose == "1":
        BSG = BSG1
        BSGMT = BSG1MT
        BSGOVR = BSG1OVR
    elif BSGChoose == "2":
        BSG = BSG2
        BSGMT = BSG2MT
        BSGOVR = BSG2OVR
    elif BSGChoose == "3":
        BSG = BSG3
        BSGMT = BSG3MT
        BSGOVR = BSG3OVR
    elif BSGChoose == "4":
        BSG = BSG4
        BSGMT = BSG4MT
        BSGOVR = BSG4OVR
    elif BSGChoose == "5":
        BSG = BSG5
        BSGMT = BSG5MT
        BSGOVR = BSG5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += BSGOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR+BSGOVR)/7
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # BENCH SMALL FORWARD POSITION

    BSFNumber = random.sample(range(24),5)

    BSF1 = SFList[int(BSFNumber[0])]
    BSF1MT = SFMTList[int(BSFNumber[0])]
    BSF1OVR = SFOVRList[int(BSFNumber[0])]

    BSF2 = SFList[int(BSFNumber[1])]
    BSF2MT = SFMTList[int(BSFNumber[1])]
    BSF2OVR = SFOVRList[int(BSFNumber[1])]

    BSF3 = SFList[int(BSFNumber[2])]
    BSF3MT = SFMTList[int(BSFNumber[2])]
    BSF3OVR = SFOVRList[int(BSFNumber[2])]

    BSF4 = SFList[int(BSFNumber[3])]
    BSF4MT = SFMTList[int(BSFNumber[3])]
    BSF4OVR = SFOVRList[int(BSFNumber[3])]

    BSF5 = SFList[int(BSFNumber[4])]
    BSF5MT = SFMTList[int(BSFNumber[4])]
    BSF5OVR = SFOVRList[int(BSFNumber[4])]

    print ("BENCH SMALL FORWARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + BSF1 + " (OVR " + str(BSF1OVR) + ").")
    print ("Type 2 for " + BSF2 + " (OVR " + str(BSF2OVR) + ").")
    print ("Type 3 for " + BSF3 + " (OVR " + str(BSF3OVR) + ").")
    print ("Type 4 for " + BSF4 + " (OVR " + str(BSF4OVR) + ").")
    print ("Type 5 for " + BSF5 + " (OVR " + str(BSF5OVR) + ").")
    BSFChoose = input("Choose: ")
    if BSFChoose == "1":
        BSF = BSF1
        BSFMT = BSF1MT
        BSFOVR = BSF1OVR
    elif BSFChoose == "2":
        BSF = BSF2
        BSFMT = BSF2MT
        BSFOVR = BSF2OVR
    elif BSFChoose == "3":
        BSF = BSF3
        BSFMT = BSF3MT
        BSFOVR = BSF3OVR
    elif BSFChoose == "4":
        BSF = BSF4
        BSFMT = BSF4MT
        BSFOVR = BSF4OVR
    elif BSFChoose == "5":
        BSF = BSF5
        BSFMT = BSF5MT
        BSFOVR = BSF5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += BSFOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR+BSGOVR+BSFOVR)/8
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # BENCH POWER FORWARD SELECTION

    BPFNumber = random.sample(range(24),5)

    BPF1 = PFList[int(BPFNumber[0])]
    BPF1MT = PFMTList[int(BPFNumber[0])]
    BPF1OVR = PFOVRList[int(BPFNumber[0])]

    BPF2 = PFList[int(BPFNumber[1])]
    BPF2MT = PFMTList[int(BPFNumber[1])]
    BPF2OVR = PFOVRList[int(BPFNumber[1])]

    BPF3 = PFList[int(BPFNumber[2])]
    BPF3MT = PFMTList[int(BPFNumber[2])]
    BPF3OVR = PFOVRList[int(BPFNumber[2])]

    BPF4 = PFList[int(BPFNumber[3])]
    BPF4MT = PFMTList[int(BPFNumber[3])]
    BPF4OVR = PFOVRList[int(BPFNumber[3])]

    BPF5 = PFList[int(BPFNumber[4])]
    BPF5MT = PFMTList[int(BPFNumber[4])]
    BPF5OVR = PFOVRList[int(BPFNumber[4])]

    print ("BENCH POWER FORWARD SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + BPF1 + " (OVR " + str(BPF1OVR) + ").")
    print ("Type 2 for " + BPF2 + " (OVR " + str(BPF2OVR) + ").")
    print ("Type 3 for " + BPF3 + " (OVR " + str(BPF3OVR) + ").")
    print ("Type 4 for " + BPF4 + " (OVR " + str(BPF4OVR) + ").")
    print ("Type 5 for " + BPF5 + " (OVR " + str(BPF5OVR) + ").")
    BPFChoose = input("Choose: ")
    if BPFChoose == "1":
        BPF = BPF1
        BPFMT = BPF1MT
        BPFOVR = BPF1OVR
    elif BPFChoose == "2":
        BPF = BPF2
        BPFMT = BPF2MT
        BPFOVR = BPF2OVR
    elif BPFChoose == "3":
        BPF = BPF3
        BPFMT = BPF3MT
        BPFOVR = BPF3OVR
    elif BPFChoose == "4":
        BPF = BPF4
        BPFMT = BPF4MT
        BPFOVR = BPF4OVR
    elif BPFChoose == "5":
        BPF = BPF5
        BPFMT = BPF5MT
        BPFOVR = BPF5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += BPFOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR+BSGOVR+BSFOVR+BPFOVR)/9
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # BENCH CENTER SELECTION

    BCNumber = random.sample(range(24),5)

    BC1 = CList[int(BCNumber[0])]
    BC1MT = CMTList[int(BCNumber[0])]
    BC1OVR = COVRList[int(BCNumber[0])]

    BC2 = CList[int(BCNumber[1])]
    BC2MT = CMTList[int(BCNumber[1])]
    BC2OVR = COVRList[int(BCNumber[1])]

    BC3 = CList[int(BCNumber[2])]
    BC3MT = CMTList[int(BCNumber[2])]
    BC3OVR = COVRList[int(BCNumber[2])]

    BC4 = CList[int(BCNumber[3])]
    BC4MT = CMTList[int(BCNumber[3])]
    BC4OVR = COVRList[int(BCNumber[3])]

    BC5 = CList[int(BCNumber[4])]
    BC5MT = CMTList[int(BCNumber[4])]
    BC5OVR = COVRList[int(BCNumber[4])]

    print ("BENCH CENTER SELECTION")
    print ("")
    print ("Choose between these players. ")
    print ("Type 1 for " + BC1 + " (OVR " + str(BC1OVR) + ").")
    print ("Type 2 for " + BC2 + " (OVR " + str(BC2OVR) + ").")
    print ("Type 3 for " + BC3 + " (OVR " + str(BC3OVR) + ").")
    print ("Type 4 for " + BC4 + " (OVR " + str(BC4OVR) + ").")
    print ("Type 5 for " + BC5 + " (OVR " + str(BC5OVR) + ").")
    BCChoose = input("Choose: ")
    if BCChoose == "1":
        BC = BC1
        BCMT = BC1MT
        BCOVR = BC1OVR
    elif BCChoose == "2":
        BC = BC2
        BCMT = BC2MT
        BCOVR = BC2OVR
    elif BCChoose == "3":
        BC = BC3
        BCMT = BC3MT
        BCOVR = BC3OVR
    elif BCChoose == "4":
        BC = BC4
        BCMT = BC4MT
        BCOVR = BC4OVR
    elif BCChoose == "5":
        BC = BC5
        BCMT = BC5MT
        BCOVR = BC5OVR
    else:
        print("You were supposed to type something from 1 to 5.")
        sys.exit(0)
    DTOVR += BCOVR
    DAOVR = (PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR+BSGOVR+BSFOVR+BPFOVR+BCOVR)/10
    print("Avg. OVR: " + str(DAOVR))
    print("Total OVR: " + str(DTOVR))
    print("")

    # Telling user the results

    print("")
    print("")
    print("YOUR LINEUP")
    print("")
    print("")
    print("YOUR STARTING LINEUP")
    print("")
    print("PG: " + PG, PGOVR)
    print("SG: " + SG, SGOVR)
    print("SF: " + SF, SFOVR)
    print("PF: " + PF, PFOVR)
    print("C: " + C, COVR)
    print("")
    print("YOUR BENCH LINEUP")
    print("")
    print("PG: " + BPG, BPGOVR)
    print("SG: " + BSG, BSGOVR)
    print("SF: " + BSF, BSFOVR)
    print("PF: " + BPF, BPFOVR)
    print("C: " + BC, BCOVR)
    print("")# here the total MT, overall, etc are calculated
    TotalMT = .95*(PGMT+SGMT+SFMT+PFMT+CMT+BPGMT+BSGMT+BSFMT+BPFMT+BCMT)
    print("Total score: " + str(TotalMT) + " (average score is " + str(int(10*AvgMT)) + ")")
    print("Average stats out of 3500: " + str(int(((PGMT+SGMT+SFMT+PFMT+CMT+BPGMT+BSGMT+BSFMT+BPFMT+BCMT)/10))))
    print("Average overall: " + str((PGOVR+SGOVR+SFOVR+PFOVR+COVR+BPGOVR+BSGOVR+BSFOVR+BPFOVR+BCOVR)/10))
    print("Total overall: " + str(DTOVR))
    # Determining whether the user exceeded the salary cap
    if diff == 2:
        if DAOVR > SCOVR:
            print("")
            print("YOU HAVE FAILED")
            print("You exceeded your salary cap of " + str(10*SCOVR) + " total OVR by " + str(DTOVR-(10*SCOVR)) + ".")
            sys.exit(0)
        else:
            print("")
            print("GOOD JOB")
            print("You did not exceed your total salary cap of " + str(10*SCOVR) + " total OVR.")

    print("")
    reer = input("Press Enter to see how well your team, the Spurs, will do in the NBA.")

    # 76ers mt = 28178, gsw mt = 30864

    # This is the info of stats of the other 29 NBA teams using the MT
    # system of their top ten players.
    # This info is from the game NBA 2K16 and was found at the site 2KMTCentral.com.
    MT_BOS = 3144+3025+3003+2994+2982+2980+2960+2947+2795+2756
    MT_BKN = 3101+3064+2833+2808+2775+2722+2709+2668+2664+2654
    MT_NYK = 3399+3104+2960+2914+2904+2877+2840+2811+2794+2671
    MT_PHI = 2938+2904+2903+2858+2820+2817+2742+2736+2732+2728
    MT_TOR = 3310+3256+3001+2945+2898+2878+2873+2872+2857+2838
    MT_CHI = 3395+3231+3028+3021+2892+2803+2793+2769+2767+2763
    MT_CLE = 3721+3160+3125+2940+2900+2847+2821+2808+2796+2787
    MT_DET = 3233+3043+2981+2919+2889+2845+2775+2756+2731+2679
    MT_IND = 3454+2920+2919+2906+2893+2872+2860+2827+2806+2734
    MT_MIL = 3225+3126+3025+3015+3010+2855+2792+2736+2720+2657
    MT_ATL = 3492+3214+2961+2946+2884+2879+2869+2849+2786+2751
    MT_CHA = 3122+3094+3048+2982+2962+2899+2894+2835+2813+2805
    MT_MIA = 3414+3265+3214+3038+2982+2931+2931+2920+2842+2828
    MT_ORL = 3071+3058+3027+2927+2858+2824+2819+2800+2796+2759
    MT_WAS = 3321+2997+2988+2988+2927+2871+2807+2789+2786+2766
    MT_DEN = 3046+3000+2996+2939+2910+2908+2872+2866+2817+2667
    MT_MIN = 3310+3115+2992+2908+2888+2885+2880+2820+2801+2777
    MT_OKC = 3630+3517+3083+3028+2929+2921+2836+2760+2705+2698
    MT_POR = 3239+3032+2979+2930+2864+2857+2808+2749+2669+2667
    MT_UTA = 3207+3107+2926+2908+2830+2818+2788+2786+2777+2777
    MT_GSW = 3619+3420+3412+3104+3054+2969+2922+2817+2782+2765
    MT_LAC = 3508+3383+3054+3004+2947+2827+2822+2800+2781+2747
    MT_LAL = 3069+2995+2923+2899+2894+2845+2750+2715+2689+2681
    MT_PHO = 3236+2969+2925+2923+2884+2882+2801+2764+2718+2691
    MT_SAC = 3512+3095+3067+2922+2918+2762+2756+2752+2722+2678
    MT_DAL = 3122+3049+3018+2961+2890+2887+2877+2843+2780+2746
    MT_HOU = 3434+3051+3008+2991+2957+2950+2844+2821+2816+2786
    MT_MEM = 3211+3020+2007+2004+3002+2914+2887+2833+2831+2747
    MT_NOP = 3619+3051+3044+2909+2898+2858+2804+2737+2712+2679
    MT_SAS = TotalMT

    SortedMT = sorted([MT_BOS,MT_BKN,MT_NYK,MT_PHI,MT_TOR,MT_CHI,MT_CLE,MT_DET,MT_IND,MT_MIL,MT_ATL,MT_CHA,MT_MIA,MT_ORL,MT_WAS,MT_DEN,MT_MIN,MT_OKC,MT_POR,MT_UTA,MT_GSW,MT_LAC,MT_LAL,MT_PHO,MT_SAC,MT_DAL,MT_HOU,MT_MEM,MT_NOP,MT_SAS])

    W = 0
    L = 0

    # Here, the user's team record is creating by comparing the team stats on 
    # the Spurs' 2015-16 schedule
    # This info was taken from the NBA.

    if MT_SAS > MT_BOS:# if the MT of the drafted team has more MT than a given
        W += 2#          team, then they will add the amount of wins to their
    elif MT_SAS < MT_BOS:#record that the Spurs played them in 15-16.
        L += 2#          The reverse applies if they're worse.
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_BKN:
        W += 2
    elif MT_SAS < MT_BKN:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_NYK:
        W += 2
    elif MT_SAS < MT_NYK:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_PHI:
        W += 2
    elif MT_SAS < MT_PHI:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_TOR:
        W += 2
    elif MT_SAS < MT_TOR:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_CHI:
        W += 2
    elif MT_SAS < MT_CHI:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_CLE:
        W += 2
    elif MT_SAS < MT_CLE:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_DET:
        W += 2
    elif MT_SAS < MT_DET:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_IND:
        W += 2
    elif MT_SAS < MT_IND:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_MIL:
        W += 2
    elif MT_SAS < MT_MIL:
        L += 2
    else:
        W += 1
        L += 1
        
    if MT_SAS > MT_ATL:
        W += 2
    elif MT_SAS < MT_ATL:
        L += 2
    else:
        W += 1
        L += 1

    if MT_SAS > MT_CHA:
        W += 2
    elif MT_SAS < MT_CHA:
        L += 2
    else:
        W += 1
        L += 1

    if MT_SAS > MT_MIA:
        W += 2
    elif MT_SAS < MT_MIA:
        L += 2
    else:
        W += 1
        L += 1

    if MT_SAS > MT_ORL:
        W += 2
    elif MT_SAS < MT_ORL:
        L += 2
    else:
        W += 1
        L += 1

    if MT_SAS > MT_WAS:
        W += 2
    elif MT_SAS < MT_WAS:
        L += 2
    else:
        W += 1
        L += 1

    if MT_SAS > MT_DEN:
        W += 4
    elif MT_SAS < MT_DEN:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_MIN:
        W += 3
    elif MT_SAS < MT_MIN:
        L += 3
    else:
        W += 2
        L += 1

    if MT_SAS > MT_OKC:
        W += 4
    elif MT_SAS < MT_OKC:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_POR:
        W += 3
    elif MT_SAS < MT_POR:
        L += 3
    else:
        W += 2
        L += 1

    if MT_SAS > MT_UTA:
        W += 4
    elif MT_SAS < MT_UTA:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_GSW:
        W += 4
    elif MT_SAS < MT_GSW:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_LAC:
        W += 3
    elif MT_SAS < MT_LAC:
        L += 3
    else:
        W += 2
        L += 1

    if MT_SAS > MT_LAL:
        W += 4
    elif MT_SAS < MT_LAL:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_PHO:
        W += 4
    elif MT_SAS < MT_PHO:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_SAC:
        W += 3
    elif MT_SAS < MT_SAC:
        L += 3
    else:
        W += 2
        L += 1

    if MT_SAS > MT_DAL:
        W += 4
    elif MT_SAS < MT_DAL:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_HOU:
        W += 4
    elif MT_SAS < MT_HOU:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_MEM:
        W += 4
    elif MT_SAS < MT_MEM:
        L += 4
    else:
        W += 2
        L += 2

    if MT_SAS > MT_NOP:
        W += 4
    elif MT_SAS < MT_NOP:
        L += 4
    else:
        W += 2
        L += 2
    print("")
    print("Your record is " + str(W) + "-" + str(L) + ".")

    # Here, the program is deciding how far the user's team goes in the playoffs
    # based on their record.
    # You make the playoffs if your record is 40 to 42
    # (the record of HOU, the worst team to make the playoffs in the West)
    # You lose the first round to MEM if your record is 40 to 43
    # (the record of MEM, whom the Spurs played in the first round)
    # You lose the second round to OKC if your record is 44 to 55
    # (the record of OKC, whom the Spurs lost to in the second round)
    # You lose the conference finals to GSW if your record is 56 to 65
    # (the record of CLE)
    # You lose the finals to CLE if your record is 66 to 73
    # (the record of GSW)
    # The reason I did this is beacuse even though CLE (from the East)
    # beat GSW (from the West), GSW still had a better record.
    # Switching the records of GSW and CLE to determine how far the user
    # goes in the playoffs allows for the system to be linear and actually work.

    if W < 40:
        print("You do not make the playoffs.")
    else:
        print("You make the playoffs.")
        if W < 43:
            print("You lose to the Memphis Grizzlies in the first round.")
        else:
            print("You beat the Memphis Grizzlies in the first round.")
            if W < 55:
                print("You lose to the Oklahoma City Thunder in the Western Conference Semifinals.")
            else:
                print("You beat the Oklahoma City Thunder in the Western Conference Semifinals.")
                if W < 65:
                    print("You lose to the Golden State Warriors in the Western Conference Finals.")
                else:
                    print("You beat the Golden State Warriors in the Western Conference Finals.")
                    if W < 73:
                        print("You lose to the Cleveland Cavaliers in the NBA Finals.")
                    else:
                        print("")
                        print("You beat the Cleveland Cavaliers in the NBA Finals.")
                        print("CONGRATULATIONS!")
                        print("THE SAN ANTONIO SPURS ARE NBA CHAMPIONS!")
    print("")
    dc = input("Draft another team? Y or N ")
    if dc == "Y" or dc == "y":# deciding if the user wants to play again.
        draft = True
        print("")
    if dc == "N" or dc == "n":
        draft = False
        print("")# credits
        print("Thank you for playing.")
        print("")
        print("----------")
        print("")
        print("SPURS DRAFT MMXVI")
        print("")
        print("Created by Ryan Gentry")
        print("at the University of Texas at San Antonio")
        print("for Mr. Alonzo for PREP IV")
        print("")
        print("Special thanks to:")
        print("Benjamin Farias")
        print("Not only God but also Jesus")
        print("2KMTCentral.com")
        print("My dog, \"Puff Daddy\"")
        print("Lil B 'The BasedGod'")
        print("All of my haters")
        print("My mom and also my dad")
        print("Mr. Alonzo and Kassandra")
        print("RiFF RAFF")
        print("")
        print("----------")
