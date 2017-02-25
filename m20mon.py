def makepotion(gold):
    import random
    energy=["fire","cold","electricity","acid"]
    protectionfrom=["good","evil","animals","vermin","outsiders"]
    use=["healing","strength","dexterity","mind","growth","protection from "+random.choice(protectionfrom),"speed","explosion of "+random.choice(energy),random.choice(energy)+" resistance","restoration","invisibility",random.choice(energy)+" breath","shield of "+random.choice(energy)]
    lvl=3
    cost=750
    if gold>750:
        lvl=3
        cost=750
    elif gold>300:
        lvl=2
        cost=300
    else:
        lvl=1
        cost=50
    return cost, "Level " + str(lvl) + " potion of "+random.choice(use)

def makeitem(gold,wiz=1):
    import math
    import random
    types=["ring","hat","gloves","belt","amulet","shoes","vest","cloak","figurine","scissors","pen","bracelet","brooch","anklet","necklace","glasses","boots","crevatte","trumpet","harp","pants","girdle"]
    ishard=[1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0]
    if (gold>1000)&(wiz>0):
        types+=["wand","staff"]
        ishard+=[1,1]

    ii=random.randint(0,len(types)-1)
    ishard=ishard[ii]

    if ishard==0:
        typeadj=["leather","gem encrusted","wool","polyester","cotton","feather","lacey","rubber","denim","paper","mithral"]
    else:
        typeadj=["glass","gold","steel","gem encrusted","lead","plastic","uranium","adamantine","mithral","hematite","copper","onyx","iron","obsidian","wooden","bone","granite","shell"]

    name=random.choice(typeadj)+" "+types[ii]

    if random.randint(1,6)>4:
        special=["glowing","runed","shiny","vibrating","muttering","humming","hovering","transluscent","warm","cold","pulsating","holy","unholy"]
        name=random.choice(special)+" "+name

    bonus=int(math.sqrt(gold/500))

    # 0 - lets user do stuff, 1 - produces something
    type=random.randint(0,1)
    if type==0:
        name="+"+str(bonus)+" "+name
        action="gives the user"
        pos=["great strength","great dexterity","extra intelligence","thorny skin","spiked fists","the ability to levitate","darkvision","the ability to detect lies","protection from fire","protection from cold","the ability to fly","the ability to heat things","the ability to eat that which is not edible","the abilty to shapechange","the ability to speak other languages","super speed"]
        action+=" "+random.choice(pos)
    elif type==1:
        acts=["shoots","summons","controls","destroys"]
        action=random.choice(acts)
        pos=["fire","frost","electricity","animals","rocks","acid","holy power","unholy power","teeth","hair","rope","string","chain","wood","flesh","blood","water","salt","air","wind","tornados","bugs","spiders","mosquitos","fish","lava","ice","antelopes","bunnies"]
        action+=" "+random.choice(pos)+" "+str(bonus)+" times per day"

    return name+" that "+action

def makemon(cr,isbaby=0):
    import math
    import random
    if (cr<1):
        cr=1
    hd=0+cr
    size=0
    hdsize=3.5
    acbon=0
    tohitbon=0
    # 0 = fire 1 = ice 2 = electric 3 = acid
    energytype=random.randint(0,3)
    energystring=["fire","cold","electric","acid"]
    specials=int(cr/4.)+1
    specialset=[]
    # initial list of adjectives and nouns
    adjectives=["lanky","drunken","creepy","slithering","sticky","bearded","hairy","hairless","smelly","bioluminescent","vibrating","sluggish","fast","jumping","tunneling"]
    nouns=["rabbit","cat","horror","reptile","tiger","ghoul","snake","bird","lemure","spider","centipede","mosquito","shark","tentacle beast","automaton","jelly","duck","goose","alpaca","wombat","bear","moth","fungus","honey badger","ferret","scorpion","maggot","carnivorous plant","zombie","orca","dolphin","bat","ooze","dog","sheep","goat","crab","snail"]
    # 0 = no special abilities
    # 1 = larger hd
    # 2 = poison
    # 3, breath weapon
    # 4, spellcaster
    # 5, fast healing
    # 6, very big
    # 7, resistances
    # 8= damage reduction, 9= stat damage, 10, bristling, 11=energy, 12=petrification, 13=baleful polymorph, 14=swallow whole
    # 15=powerful charge
    # 16=paralysis
    # 17=web
    specialcost=[0,1,1,2,1,1,1,1,1,2,1,1,3,3,2,1,1,1]
    specialdescription=[[],["shadowy","skeletal","ghoulish","undead","zombified"],["poisonous","fanged","infectious"],["with smoke billowing from its mouth", "with icy cold breath", "sparking with electricity", "with acid dripping from its mouth"],["eldritch","magical", "bewitching", "glowing", "runed","temporal","dimensional","prismatic","unholy"],["scarred","vigorous","invulnerable","healthy"],[],["thick skinned","resilient","invulnerable","scarred"],["thick skinned","resilient","invulnerable","scarred"],["vampiric","ghoulish","shadowy"],["spined","scaled","spiked","chain-covered","armored","metallic"],["wreathed in flames","covered with ice and snow","sparking with electricity","dripping with acid"],["with eery green fire burning in its eyes","with piercing eyes","with stone emanating from its footsteps","surrounded by statues of former foes","with its head covered with writhing snakes"],[],["with a gaping maw","with a look of hunger in its eyes","with foot long teeth"],["with mighty horns","with powerful legs","appearing angry and berserk","which looks ready to pounce"],["poisonous","fanged","infectious"],["surrounded by webbed former victims","with eight unblinking eyes","with a set of spinnerets","oozing a trail of silk"]]
    baseability=[[0],[0],[0],[0],[0],[1],[2],[0],[0],[2,17],[2],[0],[0],[0],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[2],[0],[0],[1],[0],[0],[0],[0],[0],[0],[0],[10],[10]]

    # higher CR, feel free to add bigger nouns
    dragoncolor=["red","white","blue","black"]
    elementaltype=["fire","ice","lightning","acid"]

    if specials>1:
        nouns+=["demon","devil","ogre","mammoth","elephant","whale","horse"]
        baseability+=[[7],[7],[6],[6],[6],[6],[6]]
    if specials>2:
        nouns+=[dragoncolor[energytype]+" dragon","shambler","hydra",elementaltype[energytype]+" elemental","basilisk","cockatrice","bull","minotaur","troll","yak"]
        baseability+=[[1,3,6],[4,6,7],[6,5],[3,7,11],[12],[12],[6,15],[6,15],[6,5],[6,15]]
    if specials>3:
        nouns+=["triceratops","t-rex"]
        baseability+=[[6,6,15],[6,6,14]]
    if specials>4:
        nouns+=[dragoncolor[energytype]+" dracolisk"]
        baseability+=[[1,3,6,12]]
    if specials>5:
        nouns+=["tarrasque"]
        baseability+=[[6,6,6,6,6]]

    # random adj and noun
    description=[random.choice(adjectives)]
    j=random.randint(0,len(nouns)-1)

    if nouns[j]=="shambler":
        energytype=2

    specialset+=baseability[j]

#    "10-ft tall","massive","giant","titanic","enormous","gargantuan"
    print 'allowed special:', specials
    for basespec in specialset:
        specials-=specialcost[basespec]
        if basespec==6:
            size+=1
    print 'remaining special:',specials

    # choose random specials. Don't allow repeats. If a maximum of 20 failures occurs, call it good enough and move on
    availableoptions=[1,2,3,3,4,4,5,6,6,6,6,6,7,8,9,10,10,11,11,14,15,16,17]
    if ((cr>10) & (random.randint(1,6)>4)):
        availableoptions+=[12,13]
    allowedfails=20
    while ((specials>0) & (allowedfails>0)):
        thisspec=random.choice(availableoptions)
        cost=specialcost[thisspec]
        if (thisspec in specialset) & (thisspec!=6):
            allowedfails-=1
        else:
            if cost<=specials:
                specialset+=[thisspec]
                specials-=cost
                if thisspec==6:
                    size+=1
                if (thisspec!=11)&(thisspec!=3):
                    description+=specialdescription[thisspec]
                else:
                    description+=[specialdescription[thisspec][energytype]]
                    
            else:
                allowedfails-=1
    # Determine the creatures full name
    prefixes=[ii for ii in description if len(ii)<=15]
    suffixes=[ii for ii in description if len(ii)>15]
    name=random.choice(prefixes)+" "+nouns[j]
    if len(suffixes)>0:
        name+=" "+random.choice(suffixes)
    sizedescriptors=["","large","enormous","gargantuan","titanic","kaiju","city sized"]
    sizebon=[0,1,2,4,8,16,32]
    if size>0:
        size=min(size,6)
        name=sizedescriptors[size]+", "+name
    print name
    print description
    print specialset

    # Start calculating stats!
    stats=[11,13,17]
    random.shuffle(stats)
    for ii in range(hd/3):
        b=[1,0,0]
        random.shuffle(b)
        for jj in range(len(stats)):
            stats[jj] += b[jj]
    stats[0]+=2*sizebon[size]
    stats[1]-=2*sizebon[size]#/2
    acbon-=sizebon[size]
    tohitbon-=sizebon[size]
    if specials<0:
        if abs(specials)>=hd:
            hd=1
            stats[0]+=(specials+hd-1)*2
            stats[1]+=(specials+hd-1)*2
            stats[2]+=(specials+hd-1)*2
        else:
            hd+=specials
    if stats[1]<3:
        stats[1]=3

    statbon=[math.floor((stat-10)/2) for stat in stats]
    # [str,dex,mind]
    if 1 in specialset:
        hdsize=4.5
    #hp=math.floor((hdsize+statbon[0])*hd)
    # there is a significant mismatch in monster & npc difficulty at early levels. Attempt to fix the mismatch.
    
    hp1=stats[0]+int(hdsize * (hd-1))
    hp2=int((hdsize+statbon[0])*hd)
    hp=max(hp1,hp2)

    atkbon=max(statbon[:2])+hd+tohitbon # use best of str or dex
    dice=["1d2","1d3","1d4","1d6","1d8","1d10","2d6","2d8","3d6","3d8","4d6","4d8","6d6","6d8","8d6","8d8","12d6","12d8","16d6"]
    dicesize=random.randint(0,2)+1+size
    dmgbon=statbon[0] # str gives damage bonus
    atktype="physical"
    attackname="Ranged" # default to ranged
    energyatkbonus=""
    if ((stats[0] >= stats[1]) | (14 in specialset) | (15 in specialset)): # melee if strength is highest OR if monster has swallow whole ability
        attackname="Melee"
        dicesize+=1
        dmgbon*=2
        #if statbon[0] > statbon[2]:
        #    atkbon+=math.floor(hd/5) # fighter m20 bonus
        #    dmgbon+=math.floor(hd/5)
    if (stats[2] == max(stats)): # mind is highest? Psychic/magic touch attack!
        dicesize-=1
        attackname+=" touch"
        dmgbon=statbon[2]
        atktype=energystring[energytype]
        if 11 in specialset:
            dmgbon+=4

    else:
        if 11 in specialset:
            energyatkbonus=" + 1d6 "+energystring[energytype]

    abldmg=""
    if 9 in specialset:
        abldmg=" + 1d4 "+random.choice(["str","dex","mind"])
        
    dicesize+=math.floor(math.log(hd+0.1)/math.log(2))

    # Is it bristling?
    if 10 in specialset:
        acbon+=4
    
    outstr='<b>'+name+'</b><br>'
    #print name
    # print out stats
    outstr += 'HP=' + str(int(hp)) +" AC=" + str(int(10+statbon[1]+hd+acbon)) +"<br>"
    #outstr += '[str,dex,mind] = ' + str(stats[0])+','+str(stats[1])+','+str(stats[2])+ " , bonuses = " + str(int(statbon[0]))+','+str(int(statbon[1]))+','+str(int(statbon[2]))+'<br>'
    outstr += "STR : "+str(stats[0])+" = "+str(int(statbon[0]))+" DEX : "+str(stats[1])+" = "+str(int(statbon[1]))+" MIND : "+str(stats[2])+" = "+str(int(statbon[2]))+"<br>"
    outstr += attackname +" +" + str(int(atkbon)) + " " + dice[int(dicesize)] +"+"+str(int(dmgbon))+" "+atktype+energyatkbonus+abldmg+'<br>'
    skills=["Physical","Communication","Subterfuge","Knowledge","Survival"]
    outstr += skills[random.randint(0,4)] + ' ' + str(int(hd+3)) + ", all others " + str(int(hd)) + '<br>'

    # 0 = no special abilities
    # 1 = larger hd
    # 2 = poison
    # 3, breath weapon
    # 4, spellcaster
    # 5, fast healing
    # 6, very big
    # 7, resistances
    # 8= damage reduction, 9= stat damage, 10, bristling, 11=energy, 12=petrification, 13=baleful polymorph, 14=swallow whole
    # 15=powerful charge
    # 16=paralysis
    # 17=web

    # Add special attacks/abilities
    for special in specialset:
        abilitystr=""
        if special == 2:
            DC=10+hd+statbon[0]
            abilitystr="Poison, DC="+str(int(DC))+", 1d4 "+random.choice(["str","dex","mind"])+" damage/round"
        elif special == 3:
            DC=10+hd+statbon[0]
            abilitystr="Breath weapon, DC="+str(int(DC))+", "+str(hd)+"d6 "+energystring[energytype]+" usable every 1d4 rounds"
        elif special == 4:
            DC=10+hd+statbon[2]
            abilitystr="Spellcaster, max spell level="+str(min(int(math.ceil(hd/2.)),9))+" DC=" +str(int(DC))
        elif special == 5:
            abilitystr="Fast healing "+str(int(hd))
        elif special == 7:
            abilitystr="Resistance to "+energystring[energytype]+" "+str(int(hd))
        elif special == 8:
            abilitystr="Damage reduction "+str(int(hd))+"/"+random.choice(["bludgeoning","slashing","piercing","cold iron","silver","magic"])
        elif special == 9:
            DC=10+hd+statbon[0]
            abilitystr="Ability damage "+abldmg[3:]
        elif special == 12:
            DC=10+hd+statbon[2]
            abilitystr="Petrifying gaze, DC="+str(int(DC))
        elif special == 13:
            DC=10+hd+statbon[2]
            abilitystr="Baleful polymorph, DC="+str(int(DC))+" usable every 1d4 rounds"
        elif special == 14:
            abilitystr="Swallow whole, stomach HP="+str(int(hp/10))+", damage="+dice[int(dicesize)]+" + "+str(int(dmgbon))+" "+atktype+energyatkbonus+abldmg
        elif special == 15:
            abilitystr="Powerful charge, charge damage="+dice[int(dicesize+4)]+"+"+str(int(dmgbon))+" "+atktype+energyatkbonus+abldmg
        elif special == 16:
            DC=10+hd+statbon[0]
            abilitystr="Paralysis, DC="+str(int(DC))+", lasts for "+dice[int(cr/3+1)]+" rounds"
        elif special == 17:
            DC=10+hd+statbon[0]
            abilitystr="Web, escape/break DC="+str(int(DC))+", can be thrown as a touch attack +"+str(int(hd+statbon[1]+tohitbon))
        if len(abilitystr)>0:
            outstr+=abilitystr+"<br>"
        

    print outstr
    outstr+='Gold : ' + str(int(260*((1.372)**(hd-1))))+" gp"
    outstr+='<p>'
    return outstr

def makenpc(level,clss="any",race="any"):
    import arcane
    import divine
    import math
    import random
    import names
    name=names.get_full_name()

    # things to be good at
    specskills=["cooking","jumping","running","climbing","sewing","painting","tripping","disarming","dirty tricks","stunning","planting","fertilizing","crafting","repair","hiding","drinking","lockpicking","searching","spotting","appraisal","smoothing","construction","rapelling","throwing","breaking","lying","listening","tasting","balancing","lifting","foraging","hunting","direction","moving quietly","knitting","smelting","brewing","washing","tune","putting out fires","first aid","riding","taming","luring","digging","chopping","translation","pantomime","grabbing","gutting"]
    numskills=int(1+level/2.0)
    goodat='-'
    if numskills>0:
        sample=random.sample(specskills,numskills)
        goodat="Good at: "
        for ii in sample:
            goodat+=ii+", "
        goodat=goodat[:-2]

    # choose background...
    bgs=["farmer","metalsmith","teacher","shopkeeper","craftsman","carpenter","mason","fisherman","hunter","beggar","addict","beast tamer","jeweler","locksmith","barkeeper","waiter","merchant","officer","traveller","adventurer","alchemist","chef","artisan","writer","artist","dancer","musician","priest"]

    bg=random.choice(bgs)
    if bg=="farmer":
        adjs=["banana","potato","squash","sheep","cattle","animal","corn","wheat","rice","apple","gold"]
        adj=random.choice(adjs)
        bg=adj+" "+bg
    if bg=="teacher":
        adjs=["physics","math","biology","chemistry","kindergarten","language","history"]
        adj=random.choice(adjs)
        bg=adj+" "+bg
    if bg=="addict":
        adjs=["magic stardust", "snuggles", "cats", "homosexuality", "caffeine", "party", "puppers", "RPG", "oxygen","kombucha"]
        adj=random.choice(adjs)
        bg=adj+" "+bg
    if bg=="merchant":
        adjs=["magic stardust","oxygen","banana","potato","squash","sheep","cattle","animal","pupper","concepts","corn","wheat","rice","apple","art","weapon","armor","jewelry","magic","sword","hammer","general","medicine","cat","music","caffeine","kombucha"]
        adj=random.choice(adjs)
        bg=adj+" "+bg

    clsses=["fighter","rogue","wizard","cleric"]
    races=["human","elf","dwarf","halfling"]
    rareraces=["gnome","half-orc","lizardman","half-elf","kobold"]
    superrareraces=["bugbear","gnoll","goblin","half-ogre","hobgoblin","orc"]
    matched=0
    for qq in clsses:
        if qq==clss:
            matched=1
    # check that clss is real, and if not set it randomly
    if matched==0:
        clss=random.choice(clsses)
    matched=0
    for qq in (races+rareraces+superrareraces):
        if qq==race:
            matched=1
    # ditto with race
    if matched==0:
        if random.randint(1,6)>4:
            races=races+rareraces
            if random.randint(1,6)>4:
                races=races+superrareraces
        race=random.choice(races)
    ii=0
    stats=[0,0,0]
    for ii in range(len(stats)):
        d=[random.randint(1,6) for _ in range(4)]
        stats[ii]=sum(d)-min(d)
    # sort starts to be optimal for each class
    if clss=="fighter":
        if stats[2]==max(stats):
            tmpstat=stats[0]
            stats[0]=stats[2]
            stats[2]=tmpstat
    if clss=="wizard":
        stats.sort()
    if clss=="rogue":
        stats.sort()
        stats=[stats[1],stats[2],stats[0]]
    if clss=="cleric":
        if stats[1] != min(stats):
            stats.sort()
            stats=[stats[1],stats[0],stats[2]]
    skills=level
    skilllist=["physical","communication","subterfuge","knowledge","survival"]
    skillbons=[0,0,0,0,0]
#    rareraces=["gnome","half-orc","lizardman","half-elf","kobold"]
#    superrareraces=["bugbear","gnoll","goblin","half-ogre","hobgoblin","orc"]
    if race=="dwarf":
        stats[0]+=2
    elif race=="elf":
        stats[2]+=2
    elif race=="halfling":
        stats[1]+=2
    elif race=="human":
        skills+=1
    elif race=="gnome":
        stats[1]+=1
        stats[2]+=1
    elif race=="half-orc":
        stats[0]+=4
        stats[2]-=2
    elif race=="lizardman":
        stats[0]+=2
        stats[1]+=2
        stats[2]-=2
    elif race=="half-elf":
        stats[1]+=1
        goodskill1=random.randint(0,4)
        goodskill2=random.randint(0,4)
        if goodskill1==goodskill2:
            if goodskill1==4:
                goodskill2-=1
            else:
                goodskill2+=1
        skillbons[goodskill1]=1
        skillbons[goodskill2]=1
    elif race=="kobold":
        stats[0]-=2
        stats[1]+=4
    elif race=="bugbear":
        stats[0]+=2
        stats[1]+=1
        skillbons[1]=-2
    elif race=="gnoll":
        stats[0]+=4
        skillbons[1]=-2
        skillbons[3]=-2
    elif race=="goblin":
        stats[1]+=2
        skillbons[1]=-1
        skillbons[2]=1
    elif race=="half-ogre":
        stats[0]+=6
        stats[1]-=2
        stats[2]-=2
    elif race=="hobgoblin":
        stats[0]+=1
        stats[1]+=1
    elif race=="orc":
        stats[0]+=4
        stats[2]-=2
        skillbons[0]=1
        skillbons[1]=-1
#    skilllist=["physical","communication","subterfuge","knowledge","survival"]
#    skillbons=[0]
#    raceskill=-1
#    rareraces=["gnome","half-orc","lizardman","half-elf","kobold"]
#    superrareraces=["bugbear","gnoll","goblin","half-ogre","hobgoblin","orc"]

    # ability advancement by level
    advancement=int(math.floor(level/3))
    if clss=="fighter":
        if (stats[1]>stats[0]):
            stats[1]+=advancement
        else:
            stats[0]+=advancement
    elif clss=="wizard":
        stats[2]+=advancement
    elif clss=="rogue":
        stats[1]+=advancement
    else:
        for qq in range(len(stats)):
            if stats[qq]==max(stats):
                stats[qq]+=advancement
                break

    statbon=[math.floor((stat-10)/2.) for stat in stats]
    
    atkbon=level
    dmgbon=0
    ac=10+statbon[1]
    if clss=="fighter":
        atkbon+=1+int(level/5)
        dmgbon+=1+int(level/5)

    betterdex=0
    if statbon[1]>statbon[0]:
        betterdex=1

    #skillline
    # and fightstyle
    # and special ability
    fightstyle=0
    # fightstyles, 0 one big weapon, 1 med weapon and shield, 2 small weapon and shield, 3 small weapon, 4 ranged weapon, 5 two small weapons
    skt="Skills +"+str(skills)
    if clss=="fighter":
        special="none"
        skt="Physical +"+str(skills+3+skillbons[0])#+", all others +"+str(skills)
        if skillbons[0]!=0:
            skillbons[0]=0
        if betterdex==0:
            fightstyle=random.randint(0,1)
        else:
            fightstyle=random.randint(3,5)
            if fightstyle==3:
                fightstyle=2
    if clss=="rogue":
        special="+Subterfuge to damage if successfully sneaking"
        skt="Subterfuge +"+str(skills+3+skillbons[2])#+", all others +"+str(skills)
        if skillbons[2]!=0:
            skillbons[2]=0
        if betterdex==0:
            fightstyle=0
        else:
            fightstyle=random.randint(3,5)
    if clss=="cleric":
        special="Casts <a href='static/divinespells.txt'>divine spells</a>, max level " + str(max(int(math.ceil(level/2.0)),9))+", save DC=" + str(int(10+level+statbon[2])) + "\nTurn undead "+str(int(level+statbon[2]+2))+"/day, +"+str(int(level+statbon[2]))+" vs undead hp<br>Favoured spells: "
        for qqq in range(min([9,int(math.ceil(level/2.0))])):
            if qqq>0:
                special+=", "
            special+=str(qqq+1)+" - "+random.choice(divine.divine[qqq+1])
        skt="Communication +"+str(skills+3+skillbons[1])#+", all others +"+str(skills)
        if skillbons[1]!=0:
            skillbons[1]=0
        if betterdex==0:
            fightstyle=0
        else:
            fightstyle=4
    if clss=="wizard":
        special="Casts <a href='static/arcanespells.txt'>arcane spells</a>, max level " + str(max(int(math.ceil(level/2.0)),9))+", save DC=" + str(int(10+level+statbon[2]))+"<br>Favoured spells: "
        for qqq in range(min([9,int(math.ceil(level/2.0))])):
            if qqq>0:
                special+=", "
            special+=str(qqq+1)+" - "+random.choice(arcane.arcane[qqq+1])
        skt="Knowledge +"+str(skills+3+skillbons[3])#+", all others +"+str(skills)
        if skillbons[3]!=0:
            skillbons[3]=0
        if betterdex==0:
            fightstyle=0
        else:
            fightstyle=random.randint(3,4)

    for qq in range(len(skilllist)):
        if skillbons[qq]!=0:
            skt+=", "+skilllist[qq]+" +"+str(skills+skillbons[qq])

    skt+=", all others +"+str(skills)

    # basic equipment
    #    gold=int(50*(2**((level+1)/2.)))
    gold=int(100*((level+1)/2.)**3)
    #gold=int(390*((1.372)**(level-1)))
    # weapon?
    costmult=1
    if fightstyle==0:
        weps=["greatsword","greataxe","halberd"]
        wepdmgs=["2d6","1d12","1d10"]
        ii=random.randint(0,len(weps)-1)
        wep=weps[ii]
        wepdmg=wepdmgs[ii]
        atkbon+=statbon[0]
        dmgbon+=2*statbon[0]
    if fightstyle==1:
        weps=["longsword","battleaxe","warhammer","bastard sword","flail","trident","heavy mace"]
        ii=random.randint(0,len(weps)-1)
        wep=weps[ii]
        wepdmg="1d8"
        if wep=="bastard sword":
            wepdmg="1d10"
        atkbon+=statbon[0]
        dmgbon+=statbon[0]
    if (fightstyle==2)|(fightstyle==3)|(fightstyle==5):
        weps=["sickle","light hammer","light mace","short sword","dagger"]
        ii=random.randint(0,len(weps)-1)
        wep=weps[ii]
        wepdmg="1d6"
        if wep=="dagger":
            wepdmg="1d4"
        atkbon+=statbon[1]
        dmgbon+=statbon[0]
    if fightstyle==5:
        costmult=2
    if fightstyle==4:
        weps=["light crossbow","shortbow","longbow","heavy crossbow"]
        wepdmgs=["1d8","1d6","1d8","1d10"]
        ii=random.randint(0,len(weps)-1)
        wep=weps[ii]
        wepdmg=wepdmgs[ii]
        if (gold > 2*statbon[0]*100)&(statbon[0]>0):
            wep="composite longbow (+"+str(statbon[0])+" str)"
            gold-=statbon[0]*100
            wepdmg="1d8"
            dmgbon+=statbon[0]
        atkbon+=statbon[1]
    wepbon=0
    if (gold>148000):
        wepbon=6
        gold-=costmult*72000
    elif (gold>100000):
        wepbon=5
        gold-=costmult*50000
    elif (gold>64000):
        wepbon=4
        gold-=32000*costmult
    elif (gold>36000):
        wepbon=3
        gold-=18000*costmult
    elif (gold>16000):
        wepbon=2
        gold-=8000*costmult
    elif (gold>4000):
        wepbon=1
        gold-=2000*costmult

    if ((wepbon>1)&(random.randint(1,6)>3))|(wepbon>5):
        pos=["flaming","shocking","frost"]
        wep=random.choice(pos)+" "+wep
        wepdmg+=" + 1d6"
        wepbon-=1

    if wepbon>0:
        wep="+"+str(wepbon)+" "+wep
        atkbon+=wepbon
        dmgbon+=wepbon
    if fightstyle==5:
        atkbon-=2
        wep="Two "+wep+"s"
    # weapon line
    atkbon=int(atkbon)
    wepline=wep+" +"+str(atkbon)
    if fightstyle==5:
        wepline+="/+"+str(atkbon)
    if level>5:
        wepline+="/+"+str(atkbon-5)
    if level>10:
        wepline+="/+"+str(atkbon-10)
    if level>15:
        wepline+="/+"+str(atkbon-15)
    #wepline=wep+" +"+str(atkbon)+" "+wepdmg+"+"+str(dmgbon)
    wepline+=" "+wepdmg
    if dmgbon<0:
        wepline+=str(int(dmgbon))
    elif dmgbon>0:
        wepline+="+"+str(int(dmgbon))

    shield="no shield"
    if (fightstyle==1) | (fightstyle==2):
        if (clss=="fighter"):
            shield="heavy steel shield"
            ac+=2
        else:
            shield="light steel shield"
            ac+=1
        shbon=0
        if (gold>50000):
            shbon=5
            gold-=25000
        elif (gold>32000):
            shbon=4
            gold-=16000
        elif (gold>18000):
            shbon=3
            gold-=9000
        elif (gold>8000):
            shbon=2
            gold-=4000
        elif (gold>2000):
            shbon=1
            gold-=1000
        if shbon>0:
            shield="+"+str(shbon)+" "+shield
            ac+=shbon
            
    # armor
    armor="robes"
    if clss!="wizard":
        if clss=="fighter":
            if (gold>1500):
                armor="full plate"
                ac+=8
                gold-=1500
            elif (gold>600):
                armor="half plate"
                ac+=7
                gold-=600
            elif (gold>200):
                armor="splint mail"
                ac+=6
                gold-=200
        if (armor=="robes")&((clss=="fighter")|(clss=="cleric")):
            if (gold>150):
                armor="chainmail"
                gold-=150
                ac+=5
            elif (gold>50):
                armor="scale mail"
                gold-=50
                ac+=4
        if (armor=="robes"):
            if (gold>100):
                armor="chain shirt"
                gold-=100
                ac+=4
            elif (gold>25):
                armor="studded leather"
                gold-=25
                ac+=3
        if (armor != "robes"):
            shbon=0
            if (gold>25000):
                shbon=5
                gold-=25000
            elif (gold>16000):
                shbon=4
                gold-=16000
            elif (gold>9000):
                shbon=3
                gold-=9000
            elif (gold>4000):
                shbon=2
                gold-=4000
            elif (gold>1000):
                shbon=1
                gold-=1000
            if shbon>0:
                armor="+"+str(shbon)+" "+armor
                ac+=shbon
        
    # leftovers, magic
    shbon=0
    extracost=2
    if (gold>32000*extracost):
        shbon=5
        gold-=32000
    elif (gold>32000*extracost):
        shbon=4
        gold-=32000
    elif (gold>18000*extracost):
        shbon=3
        gold-=18000
    elif (gold>8000*extracost):
        shbon=2
        gold-=8000
    elif (gold>2000*extracost):
        shbon=1
        gold-=2000
    if shbon>0:
        armor+=" and +"+str(shbon)+" ring of protection"
        ac+=shbon


    # Most basic info

    hp=stats[0]+int(3.5 * (level-1))
    outstr = '<b>'+name+'</b><br>'
    outstr+= "Level "+str(level)+" "+race+" "+clss+" / "+bg+' +' + str(int(math.ceil(level/2.0)))+ '<br>'
    outstr+="HP="+str(int(hp))+" AC="+str(int(ac)) + " ("+armor+" and "+shield+")<br>"
    outstr+="STR: "+str(stats[0])+" = "+str(int(statbon[0]))+" DEX: "+str(stats[1])+" = "+str(int(statbon[1]))+" MIND: "+str(stats[2])+" = "+str(int(statbon[2]))+'<br>'
    outstr+=wepline+'<br>'
    outstr+= skt+'<br>'
    if goodat!="-":
        outstr+=goodat+'<br>'
    if special!="none":
        outstr+=special
    item=0
    if (gold>=1000):
        outstr+= "<p>Magic item:<br>"
        item=1
        izwiz=0
        if (clss=="wizard"):
            izwiz=1
        itemout=makeitem(gold,wiz=izwiz)
        outstr += itemout+'<br>'
        bonus=int(math.sqrt(gold/500))
        gold-=500*(bonus**2)

    while((gold>50)&(random.randint(1,6)>3)):
        if item==0:
            outstr += "<p>Magic item:<br>"
            item=1
        cost,string=makepotion(gold)
        outstr += string+'<br>'
        gold-=cost
    
    outstr += "<p>Gold : " + str(int(gold))+'<br>'
    return outstr

# Generate and encounter
def makeencounter(lvl):
    import random
    import math

    mons=[0 for _ in range(lvl)]
    mons[0]+=1

    while (random.randint(1,10)>5):
        # choose a nonzero one which is not at the minimum (no hd<1)
        #tries=50
        nonzero=[i for i, e in enumerate(mons[:-1]) if e != 0 ]
        #nonzero=(numpy.where(mons[:-1]>0))[0]
        if len(nonzero)==0:
            break
        print nonzero
        adjustme=random.choice(nonzero)
        mons[adjustme]-=1
        mons[adjustme+1]+=2
        # do something

    print mons
    monfrac=random.randint(0,4)
    numbername=['none','A lone:','A pair of:','A trio of:','A quartet of:','Five:','Six:','Seven:','Eight:','Nine:','Ten:','Eleven:','Twelve:','Thirteen:','Fourteen:','Fifteen:','Sixteen:','An endless hoard of:']
    outstr='<h1>Level '+str(lvl)+' encounter:</h1>'
    for ii in range(len(mons)):
        if mons[ii]==0:
            continue
        hd=lvl-ii
        if (random.randint(0,3)<monfrac)|(mons[ii]>4):
            outstr+=numbername[int(min([mons[ii],len(numbername)-1]))]+'<br>'
            outstr+=makemon(hd)
            outstr+='<p>'
        else:
            for jj in range(int(mons[ii])):
                outstr+=makenpc(hd)+'<br>'
                outstr+='<p>'
            
    return outstr
