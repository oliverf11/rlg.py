import random

print("Primary")

p="AR","smg","shotgun","lmg","Marksman rifle","sniper","tactical rifle"
pc=random.choice(p)
print(pc)

par="kilo","fal","m4","fr.5.56","oden","m13","scar","ak-47","ram7","grau","cr-56-amax","an-94","as-val","ak-47cw","kirg6","fara 83","qbz-83","ffar","xm4","groza","c58","stg44","itera burst","BAR","NZ-41","Volkssturmgewehr","AS44","Automaton","Cooper Carbine","kg m40","Vargo 52"
psmg="aug","p90","mp5","uzi","pp19","mp7","striker-45","fennec","iso","mp5cw","ak-74u","bullfrog","ppsh-41","mac-10","ksp 45","milano 821","lc10","nail gun","ots9","TEC-9","LAPA","M1912","Sten","MP-40","PPSh-41","Owen Gun","Type 100","welgun","armagurrea 43"
psh="model-680","r9-0","725","origin-12","vlk-rouge","jak-12","gallo","hauer77","streetsweeper","ironhde","Einhorn Revolving","Gracey Auto","Combat shotgun","Double Barrel"
plmg="pkm","sa87","m91","mg34","holger-26","bruen-mk9","finn-lmg","stoner 63","rpd","m60","mg 82","Mg42","DP27","Bren","Type 11","whitley"
ptr="m16","dmr 14","aug","type 63","carv.2"
pmr="ebr-14","mk2","kae98k","crossbow","sks","spr-208","r1 shadowhunter","m1 garand","SVT-40","G-43"
psr="dragunov","hdr","ax-50","rytec-amr","lw3-tundra","swiss k31","m82","pelington","zrg 20mm","3-Line Rifle","Kar98k(vanguard)","Type 99","Gorenko Anti-Tank Rifle"


if pc=="sniper":
    print(random.choice(psr))
if pc=="Marksman rifle":
    print(random.choice(pmr))
if pc=="lmg":
    print(random.choice(plmg))
if pc=="shotgun":
    print(random.choice(psh))
if pc=="smg":
    print(random.choice(psmg))
if pc=="AR":
    print(random.choice(par))
if pc=="tactical rifle":
    print(random.choice(ptr))

print("secondary:")

s="handguns","launchers","melee.","AR","smg","shotgun","lmg","Marksman rifle","sniper","melee","tactical rifle"
sc=random.choice(s)
print(sc)

sh="x16","1911",".357","m19",".50 Gs","renetti","sykov","1911cw","magnum","diamatti","amp 63","machine pistol","RATT","1911","Top Break","Klauser","marshal"
sl="pila","strela-p","jokr","rpg-7","cigma 2","m79","rpgCW","M1 Bazooka","Panzerschreck","Pazerfaust","MK11 Launcher"
sm="knife","wakizashi","combat knife cw","machete","sledghammer","e-tool","Balitstic Knife","Fs Fighting Knife","Katana","Sawtooth"
pm="riot shield","riot sheild","Combat sheild","Combat sheild"

if sc=="melee.":
    print(random.choice(pm))
if sc=="launchers":
    print(random.choice(sl))
if sc=="handguns":
    print(random.choice(sh))
if sc=="melee":
    print(random.choice(sm))
if sc=="sniper":
    print(random.choice(psr))
if sc=="Marksman rifle":
    print(random.choice(pmr))
if sc=="lmg":
    print(random.choice(plmg))
if sc=="shotgun":
    print(random.choice(psh))
if sc=="smg":
    print(random.choice(psmg))
if sc=="AR":
    print(random.choice(par))
if sc=="tactical rifle":
    print(random.choice(ptr))

    
print("perks:")

p1="double time","e.o.d","scavenger","cold-blooded","kill-chain","quick fix"
print(random.choice(p1))

  
if sc=="handguns"or sc=="launchers"or sc=="melee":
  p2="restock","hardline","high-alert","ghost","point-man","tempered"
else:
  p2="overkill","overkill"

print(random.choice(p2))

p3="tune-up","amped","shrapnel","battle-hardened","spotter","tracker","combat scout"
print(random.choice(p3))

print("lethal:")

l="claymore","frag","molotove","c4","semtex","throwing-knife","prox-mine","thermite"
print(random.choice(l))

print("tactical:")

t="flash","stun","smoke","snapshot","heartbeat-sensor","stim","deycoy","gas"
print(random.choice(t))
