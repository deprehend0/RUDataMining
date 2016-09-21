#Exercise 1.3.1
#When changing the query image the most and least similar images change as well.
#In that way you'll always see the five most and least similar images.

#I used query image 138.

#ExtendedJaccard, Cosine and correlation give about the same results as the 
#query image. The other measures give results mainly based on the grey values
#therefore the facial expressions look really different and sexes don't match.

#I think correlation gives the best results. Most of the similar pictures are
#of the same sex as the query image and most of them have plus minus the same
#facial expression as the query image. With other measures the similarity 
#depended more on the grey values of the picture or even gave opposite facial
#expressions as most similar results.
#So with correlation sex, facial expresison and even greyvalues match the best
#with the query image.

#Exercise 1.3.2
#In the statements I use. My b = 123 and the similarity_measure is either
#Cosine, ExtendedJaccard or Correlation. For the notation if they are the same
#I use the same syntax as given in the exercise.
#sim = similarity(b + X[i,:], X[noti,:], similarity_measure)

#Cosine(123+X, Y) = Cosine(X, Y): This statement is true
#ExtendedJaccard(123+X, Y) = ExtendedJaccard(X, Y): This statement is false
#Correlation(123+X, Y) = Correlation(X, Y): This statement is true


# exercise 3.2.1

from pylab import *
from scipy.io import loadmat
from similarity import similarity

# Image to use as query
i = 1

#similarity_measure = 'Cosine'
#similarity_measure = 'ExtendedJaccard'
similarity_measure = 'Correlation'

# Load the CBCL face database
# Load Matlab data file to python dict structure
X = loadmat('Data/wildfaces_grayscale.mat')['X']
N, M = shape(X)


# Search the face database for similar faces
# Index of all other images than i
noti = range(0,i) + range(i+1,N) 
# Compute similarity between image i and all others
sim = similarity(123 + X[i,:], X[noti,:], similarity_measure)
sim = sim.tolist()[0]
# Tuples of sorted similarities and their indices
sim_to_index = sorted(zip(sim,noti))


# Visualize query image and 5 most/least similar images
figure(figsize=(12,8))
subplot(3,1,1)
imshow(np.reshape(X[i],(40,40)).T, cmap=cm.gray)
xticks([]); yticks([])
title('Query image')
ylabel('image #{0}'.format(i))


for ms in range(5):

    # 5 most similar images found
    subplot(3,5,6+ms)
    im_id = sim_to_index[-ms-1][1]
    im_sim = sim_to_index[-ms-1][0]
    imshow(np.reshape(X[im_id],(40,40)).T, cmap=cm.gray)
    xlabel('sim={0:.3f}'.format(im_sim))
    ylabel('image #{0}'.format(im_id))
    xticks([]); yticks([])
    if ms==2: title('Most similar images')

    # 5 least similar images found
    subplot(3,5,11+ms)
    im_id = sim_to_index[ms][1]
    im_sim = sim_to_index[ms][0]
    imshow(np.reshape(X[im_id],(40,40)).T, cmap=cm.gray)
    xlabel('sim={0:.3f}'.format(im_sim))
    ylabel('image #{0}'.format(im_id))
    xticks([]); yticks([])
    if ms==2: title('Least similar images')
    
show()
