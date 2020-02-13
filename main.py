import random

class person(object):
    def __init__(self,name,otherGender=None):
        self.name = name
        
        #the array containing all people in the other gender
        self.otherGender = otherGender
        
        #the array containing the preferred people of this person, from best to worse
        self.preferences = []
        
        #creating the preferences
        self.randomPreference()
        
        self.engaged = False
        self.ex = ''
        
    def randomPreference(self):

        #for some reason random.shuffle() would give the same result although iterated various times? so I had to write this section

        #You can't have more preferences than there are people in the other set
        while len(self.preferences) < len(self.otherGender):

            randomPerson = random.choice(self.otherGender)

            if randomPerson not in self.preferences:
                self.preferences.append(randomPerson)


    #when the person 'proposes' to its current top preference
    def propose(self,mate):

        if not mate.engaged:
            self.engaged = mate.name
            mate.engaged = self.name

            return True

        else:

            #since preferences are ordered from best to worst, the smaller the index the better you are
            if mate.preferences.index(mate.engaged) > mate.preferences.index(self.name):
                    mate.ex = mate.engaged
                
                    self.engaged = mate.name
                    mate.engaged = self.name

                    return True

        return False

                

while True:
    setNumber = int(input('How many people are there per gender? '))

    #the names of each male and female: M stands for male, F for female.
    #the numbers 1...n are assigned to each person (as a name): e.g: M5 is male5
    malesList = [f'M{i}' for i in range(1,setNumber+1)]
    femalesList = [f'F{i}' for i in range(1,setNumber+1)]


    males = [person(male,femalesList) for male in malesList]
    females = [person(female,malesList) for female in femalesList]
    
    
    for i in range(len(malesList)):
        
        for male in males:

            if not male.engaged:

                #chooses the female it will propose to:
                #as we have a list of all females names and it's in the same order as the female objects
                #we can use the male preferences (which are only strings, not objects) and find out which object it corresponds
                #to in the females array
                
                potentialMate = females[femalesList.index(male.preferences[i])]
                
                isEngaged = male.propose(potentialMate)

                if isEngaged:

                    try:
                        ex = males[malesList.index(potentialMate.ex)]
                        ex.engaged = False
                        potentialMate.ex = ''

                    #if the current mate didn't have an ex      
                    except: pass


    for male in males:
        print(f'{male.name} and {male.engaged} are engaged')
        
        #print(f"\n the male's preferences: {male.preferences}")
        #print(f" the female's preferences: {females[femalesList.index(male.engaged)].preferences} \n")
        
