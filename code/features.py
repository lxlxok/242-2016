import data
from sklearn.feature_extraction import DictVectorizer
import numpy as np
import sys

# This is mainly for deciding if we are getting real or fake data.
DEBUG = False

# TODO(dhawal): Do some feature engineering.
def getFeatures():
    features = []
    businesses = data.getBusinesses(DEBUG)

    # print businesses[0]
    # sys.exit()

    # one-hot encoding of active, city, and state variables + numeric features
    vec = DictVectorizer()
    cityStateMatrix = vec.fit_transform([{"active": b[1], "city":b[2], "state":b[3]} for b in businesses]).toarray()
    businesses = np.array([business[4:] for business in businesses])
    features = np.hstack((cityStateMatrix, businesses))
    return features
   
    # For now, just pick out the numeric features.
    # return [business[3:] for business in businesses]

if __name__ == '__main__':
    getFeatures()