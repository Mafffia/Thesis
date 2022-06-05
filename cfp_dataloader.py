import os
import pandas as pd


def pair_f():
    pdict = {}
    with open('./cfp-dataset/Protocol/Pair_list_F.txt', 'r') as f:
        for line in f.readlines():
            split = line.rstrip('\n').split(sep=' ')
            pdict[split[0]] = split[1].replace('..', './cfp-dataset')
    return pdict


def pair_p():
    pdict = {}
    with open('./cfp-dataset/Protocol/Pair_list_P.txt', 'r') as f:
        for line in f.readlines():
            split = line.rstrip('\n').split(sep=' ')
            pdict[split[0]] = split[1].replace('..', './cfp-dataset')
    return pdict


class front:
    def __init__(self):
        self.df = pair_f()

    def get_filename_via_index(self, index):
        query = self.df[self.df['index'] == index]
        if len(query) == 1:
            return str(query['file'])
        else:
            raise Exception


class profile:
    def __init__(self):
        self.df = pair_p()

    def get_filename_via_index(self, index):
        query = self.df[self.df['index'] == index]
        if len(query) == 1:
            return str(query['file'][0])
        else:
            raise Exception


# 10-fold for frontal-frontal pair
class ff:
    # load in pairs in folds, both diff and same, return in [(a1,b1),(a2,b2) ...] format
    def loadpairs(self, filename):
        ret = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                # getting rid of ending of line
                split = line.rstrip('\n').split(sep=',')
                ret.append((split[0], split[1]))
        return ret

    def __init__(self):
        self.currentFold = 1

    # generate dir of diff/same file for current fold
    def generatedir(self):
        foldstr = str(self.currentFold)
        if len(foldstr) == 1:
            foldstr = '0' + foldstr
        basedir = './cfp-dataset/Protocol/Split/FF/' + foldstr + '/'
        diffdir = basedir + 'diff.txt'
        samedir = basedir + 'same.txt'
        self.currentFold += 1
        if self.currentFold > 10:
            self.currentFold = 1
        return diffdir, samedir

    # return diff/same pairs of current fold
    def loadcurrentfold(self):
        diff, same = self.generatedir()
        diffpairs = self.loadpairs(diff)
        samepairs = self.loadpairs(same)
        diffdir = []
        samedir = []
        fdict = pair_f()
        for pair in diffpairs:
            diffdir.append((fdict[pair[0]], fdict[pair[1]]))
        for pair in samepairs:
            samedir.append((fdict[pair[0]], fdict[pair[1]]))
        return diffdir, samedir


class fp(ff):
    def generatedir(self):
        foldstr = str(self.currentFold)
        if len(foldstr) == 1:
            foldstr = '0' + foldstr
        basedir = './cfp-dataset/Protocol/Split/FP/' + foldstr + '/'
        diffdir = basedir + 'diff.txt'
        samedir = basedir + 'same.txt'
        self.currentFold += 1
        if self.currentFold > 10:
            self.currentFold = 1
        return diffdir, samedir
    def loadcurrentfold(self):
        diff, same = self.generatedir()
        diffpairs = self.loadpairs(diff)
        samepairs = self.loadpairs(same)
        diffdir = []
        samedir = []
        fdict = pair_f()
        pdict = pair_p()
        for pair in diffpairs:
            diffdir.append((fdict[pair[0]], pdict[pair[1]]))
        for pair in samepairs:
            samedir.append((fdict[pair[0]], pdict[pair[1]]))
        return diffdir, samedir

# front = pair_f()
# print(front)
# # print(str(front[front['index'] == 2]['file'][0]))
# front1 = front()
# print(front1.df.head())
# try:
#     print(front1.get_filename_via_index(0))
# except:
#     print('exception happened')
# profile1 = profile()
# # print(profile1.df.head())
# print(profile1.get_filename_via_index(1))


# ff1 = ff()
# ff1.loadcurrentfold()
# print(ff1.loadcurrentfold())
# ff1.loadpairs('./cfp-dataset/Protocol/Split/FF/01/diff.txt')
#
# fp1 = fp()
# fp1.loadcurrentfold()
# print(fp1.loadcurrentfold())
