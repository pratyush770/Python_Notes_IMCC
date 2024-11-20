class Student:
    def __init__(self, name, rollNumber, mathsMks, scienceMks, engMks):
        self._name = name  # non public attributes
        self._rollNumber = rollNumber
        self._mathsMks = mathsMks
        self._scienceMks = scienceMks
        self._engMks = engMks

    def setName(self, name):   # setter to set the value
        if len(name.strip()) == 0:
            print("Name field should not be empty.")
        else:
            self._name = name

    def getName(self):  # getter to get the value
        return self._name

    def setRollNumber(self, rollNumber):
        if len(rollNumber.strip()) == 0:
            print("Roll number should not be empty.")
        else:
            self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber

    def setMathsMks(self, mathsMks):
        if mathsMks < 0:
            print("Math marks should not be negative.")
        else:
            self._mathsMks = mathsMks

    def getMathsMks(self):
        return self._mathsMks

    def setScienceMks(self, scienceMks):
        if scienceMks < 0:
            print("Science marks should not be negative.")
        else:
            self._scienceMks = scienceMks

    def getScienceMks(self):
        return self._scienceMks

    def setEngMks(self, engMks):
        if engMks < 0:
            print("English marks should not be negative.")
        else:
            self._engMks = engMks

    def getEngMks(self):
        return self._engMks
