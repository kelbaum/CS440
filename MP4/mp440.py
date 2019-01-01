import inspect
import sys
import math

'''
Raise a "not defined" exception as a reminder
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit)
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    # Your code starts here
    for i in range(height):
        for j in range(width):
            if digit_data[i][j] != 0:
                features.append(1)
            else:
                features.append(0)
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    #_raise_not_defined()
    return features

'''
Extract advanced features that you will come up with
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    # Your code starts here
    # code - current, below
    """
    # '+' is only true
    for i in range(height):
        for j in range(width):
            if digit_data[i][j] == 1:
                features.append(1)
            else:
                features.append(0)
    """
    """
    # '#' is only true
    for i in range(height):
        for j in range(width):
            if digit_data[i][j] == 2:
                features.append(1)
            else:
                features.append(0)
    """
    """
    # Only checking current + below

    for i in range(height):
        for j in range(width):
            if i != height - 1:
                if digit_data[i][j] == 0:
                    if digit_data[i+1][j] == 0:
                        features.append(0)
                    else:
                        features.append(2)
                else:
                    if digit_data[i+1][j] == 0:
                        features.append(3)
                    else:
                        features.append(4)
            else:
                if digit_data[i][j] != 0:
                    features.append(3)
                else:
                    features.append(0)
    """

    # Combined Code
    # 0 - false, false
    # 2 - false, true
    # 3 - '#', false
    # 4 - '+', false
    # 5 - '#', true
    # 6 - '+', true
    for i in range(height):
        for j in range(width):
            if i != height - 1:
                if digit_data[i][j] == 0:
                    if digit_data[i+1][j] == 0:
                        features.append(0)
                    else:
                        features.append(2)
                else:
                    if digit_data[i+1][j] == 0:
                        if digit_data[i][j] == 1:
                            features.append(3)
                        else:
                            features.append(4)
                    else:
                        if digit_data[i][j] == 1:
                            features.append(5)
                        else:
                            features.append(6)
            else:
                if digit_data[i][j] != 0:
                    if digit_data[i][j] == 1:
                        features.append(3)
                    else:
                        features.append(4)
                else:
                    features.append(0)



    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    #_raise_not_defined()
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here

    # Only using third new feature set
    # 0 - false, false
    # 2 - false, true
    # 3 - True, false
    # 4 - False, true
    for i in range(height):
        for j in range(width):
            if i != height - 1:
                if digit_data[i][j] == 0:
                    if digit_data[i+1][j] == 0:
                        features.append(0)
                    else:
                        features.append(2)
                else:
                    if digit_data[i+1][j] == 0:
                        features.append(3)
                    else:
                        features.append(4)
            else:
                if digit_data[i][j] != 0:
                    features.append(3)
                else:
                    features.append(0)
    #_raise_not_defined()
    return features

'''
Compute the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training.
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # len(data) = 5000
    # len(data[0]) = 28
    # There are 14,000 lines in the file "trainingimages"
    global statistics
    statistics = [[[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], []]]
    global P_y
    P_y = []


    label_indexer = [[], [], [], [], [], [], [], [], [], []]
    # print len(label_indexer)
    # print label < - prints every label
    # iterate through percentage of given data
    data_size = math.trunc(len(label) * (percentage)/100)
    for i in range(data_size):
        label_indexer[label[i]].append(i)
    # print label_indexer

    # iterate through each label
    for i in range(len(label_indexer)):
        # store each feature array (image of booleans) into big array
        all_image_bool_arr = []

        for j in range(len(label_indexer[i])):
            all_image_bool_arr.append(feature_extractor(data[label_indexer[i][j]], width, height))

        k_value = 1
        for k in range(len(all_image_bool_arr[0])):
            # iterate through each pixel position
            true_count = 0.0
            counts = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            for j in range(len(all_image_bool_arr)):
                # iterate through each image
                counts[all_image_bool_arr[j][k]] += 1.0


            # append feature count to table
            #statistics[1][i].append(math.log((true_count * 1.0 + k_value) / (data_size + k_value)))
            statistics[1][i].append(math.log((counts[1] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            #statistics[0][i].append(math.log((len(all_image_bool_arr) - true_count * 1.0 + k_value) / (data_size + k_value)))
            statistics[0][i].append(math.log((counts[0] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            statistics[2][i].append(math.log((counts[2] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            statistics[3][i].append(math.log((counts[3] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            statistics[4][i].append(math.log((counts[4] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            statistics[5][i].append(math.log((counts[5] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
            statistics[6][i].append(math.log((counts[6] * 1.0 + k_value) / (len(all_image_bool_arr) + k_value)))
        # append the log of P(Y) of label Y
        P_y.append(len(all_image_bool_arr) * 1.0 / data_size)

    # Your code ends here
    #_raise_not_defined()

'''
For the given features for a single digit image, compute the class
'''
def compute_class(features):
    predicted = -1

    # Your code starts here
    predict_arr = []
    for i in range(len(statistics[0])):
        # iterate through labels 0-9
        pixel_prob = []
        for j in range(len(statistics[0][i])):
            # find max of feature 0 or 1
            pixel_prob.append(statistics[features[j]][i][j])
        predict_arr.append(sum(pixel_prob) + math.log(P_y[i]))
    predicted = predict_arr.index(max(predict_arr))
    #print predicted

    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    #_raise_not_defined()

    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]

    # Your code starts here
    # Find P(Label | Feature)
    for i in range(len(data)):
        predicted.append(compute_class(feature_extractor(data[i], width, height)))
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    #_raise_not_defined()

    return predicted
