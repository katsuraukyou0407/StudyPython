import sys
units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tys = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
thousands = ['thousand','million','billion','trillion']
def num2words(num,depth=0):
    if num == 0: return 'zero'

    

    words = []
    
    #last two digits
    x = num%100
    if x == 0:
        pass
    elif x >= 1 and x <= 9:
        words.append(units[x])
    elif x >= 10 and x <= 19:
        words.append(teens[x%10])
    else:
        words.append(units[x%10])
        words.append(tys[x//10])

    #3rd digit
    y = (num//100)%10
    if y == 0:
        pass
    else:
        if x != 0:
            pass#words.append('and')
        words.append('hundred')
        words.append(units[y])

    #4th digit and above
    next = num2words(num//1000,depth+1)
    if next == 'zero':
        pass
    else:
        words.append(thousands[depth])
        words.append(next)
        
    return ' '.join(reversed(words))

def main():
    sum = 0
    #for i in range(1,1001):
        #words = num2words(i)
        #print words
        #sum += len(filter(lambda x:x!=' ',list(words)))
    argvs = sys.argv
    tmppoint = argvs[1].split('.')
    words = num2words(int(tmppoint[0]))
    #print (tmppoint[1])
    if len(tmppoint) == 2:
        tmp2point = tmppoint[1]
        #words.append('point')
        words += ' point'
        for i in range(len(tmp2point)):
            words += ' ' + units[int(tmp2point[i])]
    print(words)

if __name__ == '__main__':
    main()