class Segregate_the_file:
    ''' Segregates the input file '''        
    array = []
    filen=input('Enter the File path:')
    filename=filen
    with open(filename, "r+") as ins:    
        for line in ins:
            array.append(line)
    Started_String='======== Started'
    Ended_String='======== Ended'
    Site_1=[]
    Site_2=[]
    Site_3=[]
    Site_4=[]

    line=0
    while line<len(array):
        if ((Started_String or Ended_String or '\n') in array[line]) or ('Site' not in array[line]):
            Site_1.append(array[line])
            Site_2.append(array[line])
            Site_3.append(array[line])
            Site_4.append(array[line])    

        if 'Site 1' in array[line]: Site_1.append(array[line])
        elif 'Site 2' in array[line]: Site_2.append(array[line])
        elif 'Site 3' in array[line]: Site_3.append(array[line])
        elif 'Site 4' in array[line]: Site_4.append(array[line])
        
        if '******** Started Site : 1' in array[line]:
            for i in range(line,len(array)):
                if '******** Ended   Site : 1' not in array[i]:
                    Site_1.append(array[i])
                elif '******** Ended   Site : 1'  in array[i]:
                    Site_1.append(array[i])
                    line=i
                    break        
        elif '******** Started Site : 2' in array[line]:
            for i in range(line,len(array)):
                if '******** Ended   Site : 2' not in array[i]:
                    Site_2.append(array[i])
                elif '******** Ended   Site : 2'  in array[i]:
                    Site_2.append(array[i])
                    line=i
                    break
        elif '******** Started Site : 3' in array[line]:
            for i in range(line,len(array)):
                if '******** Ended   Site : 3' not in array[i]:
                    Site_3.append(array[i])
                elif '******** Ended   Site : 3' in array[i]:
                    Site_3.append(array[i])
                    line=i
                    break
        elif '******** Started Site : 4' in array[line]:
            for i in range(line,len(array)):
                if '******** Ended   Site : 4' not in array[i]:
                    Site_4.append(array[i])
                elif '******** Ended   Site : 4'  in array[i]:
                    Site_4.append(array[i])
                    line=i
                    break
        line+=1

    site={'Site1':Site_1,'Site2':Site_2,'Site3':Site_3,'Site4':Site_4}
    site_name=['Site1','Site2','Site3','Site4']
    outputfilepath=filename.split('.')[0]
    for site1 in site_name:
        with open(outputfilepath+'_'+site1+'.log', 'w') as f:
            for item in site[site1]:
                f.write("%s" % item)
    print('Segeration completed')
    
Segregate_the_file()