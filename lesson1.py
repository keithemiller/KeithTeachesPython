# -*- coding: utf-8 -*-
"""
Lesson 1 Script for KeithTeachesPython

Created on Wed Feb 17 21:01:59 2016

@author: Keith
"""

class AnswerChecker(object):
    
    answer_key = [42, 233168, 4613732]    
    
    def __init__(self):
        pass
    
    def check(self, question, answer):
        corr_ans = self.answer_key[question]     
        if answer is corr_ans:
            print "CORRECT!"
            return True
        elif type(answer) is not type(corr_ans):
            print "Your answer is not the correct type"
            return False
        else:
            print "INCORRECT"
            return False


if __name__=='__main__':
    print "This module is meant to be imported in the Lesson1 IPython Notebook"