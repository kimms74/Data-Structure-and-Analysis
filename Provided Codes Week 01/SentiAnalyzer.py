import math

class SentiAnalyzer:

    # Make the method signature to accept "sentidata" and "word"
    def __init__(self):
        print('This is a senti analyzer')

    def probWordPositiveAndNegative(self, sentidata, word, idxWord):
        pointedWord = word[idxWord]
        reviews = [int(float(row[-1])) for row in sentidata]
        occurrence = [int(float(row[idxWord])) for row in sentidata]

        # Calculate the number of positive review occurrence with the pointed word, and assign the calculated value to 'positive'
        positive = 0
        for i in range(len(occurrence)):
            positive = positive + occurrence[i] * reviews[i]

        # Calculate the number of positive reviews from the entire review set
        numPositiveReviews = sum(reviews)

        # Calculate the number of negative review occurrence with the pointed word, and assign the calculated value to 'negative'
        negative = 0
        for i in range(len(occurrence)):
            negative = negative + occurrence[i] * (1 - reviews[i])

        rowCount = len(sentidata)
        positiveProb = float(positive) / float(numPositiveReviews)
        negativeProb = float(negative) / float(rowCount - numPositiveReviews)

        if positiveProb == 0:
            positiveProb = 0.00001
        if negativeProb == 0:
            negativeProb = 0.00001
        return pointedWord, positiveProb, negativeProb

    def probPositiveAndNegative(self, sentidata):
        positive = sum([int(float(row[-1])) for row in sentidata])
        numReviews = len(sentidata)
        negative = numReviews - positive
        positiveProb = float(positive) / float(numReviews)
        negativeProb = float(negative) / float(numReviews)
        return positiveProb, negativeProb

    def findUsedWords(self, sentidata, word, idx):
        # Return the index of the used words in 'idx'th review
        temp = [int(float(x)) for x in sentidata[idx][:-1]]                         # [i for i in v]: print i with list
        idxUsedWords = [index for index, value in enumerate(temp) if value == 1]    # [i for in v if ( )]: print i with list only if true
        # Return the actual words in 'idx'th review                                 # enumerate: return index and value
        usedWords = [word[idx] for idx in idxUsedWords]
        return idxUsedWords, usedWords

    def runAnalysis(self, sentidata, word, idxReview):
        probLogPositive = 0
        probLogNegative = 0
        idxUsedWords, usedWords = self.findUsedWords(sentidata, word, idxReview)

        # Make a for-loop to run from the first word to the last word
        for i in range(len(idxUsedWords)):
            # get the first word from the used word set
            idxWord = idxUsedWords[i]
            # calculate the word's probability to be positive or negative
            pointedWord, positive, negative = self.probWordPositiveAndNegative(sentidata, word, idxWord)
            probLogPositive += math.log(positive)   # reason to use log: if you keep producting probability, then total probability goes to zero. So using log, we can just add them to represent product
            probLogNegative += math.log(negative)

        positiveProb1, negativeProb1 = self.probPositiveAndNegative(sentidata)
        probLogPositive += math.log(positiveProb1)
        probLogNegative += math.log(negativeProb1)

        if probLogPositive > probLogNegative:
            sentiment = 'Positive'
            print('Positive')
        else:
            sentiment = 'Negative'
            print('Negative')

        return probLogPositive, probLogNegative, sentiment

