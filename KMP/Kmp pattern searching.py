#kmp algorithm for Pattern Matching

def make_LPS(pat):
    lps=[]
    lps.append(0)
    j=0
    for i in range(1,len(pat)):
       if pat[i] == pat[j]:
           j+=1
           lps.append(j)
       else:
            if j!= 0:
                j=lps[j-1]
                i-=1
            elif j==0:
                lps.append(0)
    return lps

def KMP(phrase,pat):
    lps=make_LPS(pat)
    lps_index=0
    matches=[]
    for i in range(len(phrase)):
        if phrase[i] == pat[lps_index]:
            lps_index+=1
            if lps_index == len(pat):
                matches.append(i-lps_index+1)
                lps_index=0
        else:
            if lps_index != 0:
                lps_index=lps[lps_index-1]
                i-=1
            
    print(matches)

def main():
    phrase="algorithm to check pattern"
    pattern="rithm"
    KMP(phrase,pattern)

if __name__ == "__main__":
    main()
