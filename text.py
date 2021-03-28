# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:50:24 2021

@author: User
"""

def revword(word:str) -> str:
    word=word.lower()
    return (word [::-1])
   
    
def countword()->int: 
    name='text.txt'    
    fhand=open(name)
    File=fhand.read().split()
    countWord=1
    for i in range(1,len(File)):
        File[i]=revword(File[i])
        if File[i] == File[0] :
            countWord=countWord+1
    print(countWord)
    return countWord
    
 


