## import modules here 
import numpy as np


def precalc(train_data):
    dd={'spam':{}, 'ham':{}}
    
    convert={'spam':0, 'ham':1}
    prior=[0,0,0]

    for msg in train_data:
        txt_dict, label= msg
        prior[convert[label]]+=1
        prior[2]+=1
        dd[label]={ k: dd[label].get(k, 0) + txt_dict.get(k, 0) for k in set(dd[label]) | set(txt_dict) }
     
    prior=(prior[0]/prior[2])/(prior[1]/prior[2])

    return prior, dd

def uniq_total(train_data):
    d={}
    for msg in train_data:
        txt=msg[0]
        for i in txt:
            if i not in d:
                d[i]=1
    
    return d

def occ(word, data):
    if word in data:
        return data[word]+1
    return 1


################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
    
    prior, word_dict= precalc(training_data)
    total_spam=sum(word_dict['spam'].values())
    total_ham=sum(word_dict['ham'].values())
    all_words=uniq_total(training_data)
    total_all= len(all_words)
    posterior=prior
    
    sms_words={}
    for w in sms:
        if w not in sms_words:
            sms_words[w]=1
        else:
            sms_words[w]+=1
        
    for w in all_words:
        ham_occ= occ(w, word_dict['ham'])
        spam_occ= occ(w, word_dict['spam'])
        ham_prob= ham_occ/ (total_ham+total_all)
        spam_prob=spam_occ/ (total_spam+total_all)
        
        if w in sms:
            posterior= posterior * (spam_prob/ham_prob)**sms_words[w]
        else:
            posterior= posterior * (spam_prob/ham_prob)**0
    
    return posterior