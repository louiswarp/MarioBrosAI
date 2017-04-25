import numpy as np
from actionSelector import validDecisions as VD
from _random import Random


class QLearning(object):
    def __init__(self, name):
        self.name = name
    theQMap = {}

    thePreviousAction = VD.DO_NOTHING
    thePreviousQValue = 0
    thePreviousState=()
    ##constants
    theLearningRate = 0.7
    theGamma = 0.3

    def initializeQValuesForState(self, aState):
        myQValues = []
        for i in range(0,len(VD)):
            myQValues.append(np.random.uniform(0, 1) * 0.2 - 0.1)

        self.theQMap[aState]= myQValues
        return myQValues

    def updateQValues(self, aNewInstantReward, aNewState):
        if(not self.theQMap.get(self.thePreviousState)==None):
            self.thePreviousQValue=self.theQMap.get(self.thePreviousState)[self.thePreviousAction.value]
        else:
            self.initializeQValuesForState(self.thePreviousState)
            self.thePreviousQValue = self.theQMap.get(self.thePreviousState)[self.thePreviousAction.value]

        myNewValue = (1 - self.theLearningRate) * self.thePreviousQValue + self.theLearningRate * (
        aNewInstantReward + self.theGamma * self.getMaxQValue(aNewState))
        self.theQMap[self.thePreviousState][self.thePreviousAction.value]= myNewValue


        #####

    # SETTERS
    #####

    def setPreviousAction(self, aPreviousAction):
        self.thePreviousAction = aPreviousAction

    def setPreviousState(self, aPreviousState):
        self.thePreviousState = aPreviousState
    #####
    # GETTERS
    #####

    # return maximum QValue for a givenState
    def getMaxQValue(self, aState):
        myAllActionsQValues = self.theQMap.get(aState)
        if(myAllActionsQValues==None):
            myAllActionsQValues= self.initializeQValuesForState(aState)

        myBestQValue = np.max(myAllActionsQValues)

        return myBestQValue

    # return the best action for a given state
    # it should return an enum
    def getBestAction(self, aGame, aState):
        myAllActionsQValues = self.theQMap.get(aState)
        if(myAllActionsQValues is None):
            self.initializeQValuesForState(aState, aGame)
            myAllActionsQValues = self.theQMap.get(aState)
        myBestAction = myAllActionsQValues.index(np.max(myAllActionsQValues))

        return VD(myBestAction)