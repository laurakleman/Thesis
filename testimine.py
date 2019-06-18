def testimine(ennustatud_lemmade_fail, õiged):
    with open(õiged, encoding="utf-8") as f:
        fail = f.readlines()
    with open(ennustatud_lemmade_fail, encoding="utf-8") as f:
        ennustatud = f.readlines()
    õigedlemmad = []
    for el in fail:
        if len(el) > 1 and el[0] != '#':
            õigedlemmad.append(el.split('\t')[2].replace('=','').replace('_','').replace('-',''))
    ennustatudlemmad = []
    for el in turku:
        if len(el) > 1 and el[0] != '#':
            ennustatudlemmad.append(el.split('\t')[2].replace('=','').replace('_','').replace('-',''))
    score = 0
    valed = []
    for i in range(len(ennustatudlemmad)):
        if ennustatudlemmad[i].lower() == õigedlemmad[i].lower():
            score +=1
        else:
            valed.append((ennustatudlemmad[i],õigedlemmad[i]))
    print(score)
	
	
	with open("tulemusfail.txt", 'w',encoding="utf-8" ) as d:
    for el in valed:
        d.writelines(el[0])
        d.write('\t')
        d.write(el[1])
        d.write('\n')
´