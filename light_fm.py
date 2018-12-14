from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.evaluation import precision_at_k
import numpy as np
# Load the MovieLens 100k dataset. Only five
# star ratings are treated as positive.
data=[]
with open('classification/data/cf_rec/u.train','r') as f:
    for line in f.readlines():
        data.append(line.split('\t'))
# data = fetch_movielens(min_rating=4.0)
dataset = Dataset()
dataset.fit(users=np.unique(data[:, 0]), items=np.unique(data[:, 1]))
train_interactions, train_weights = dataset.build_interactions((i[0], i[1], i[2]) for i in data)

# Instantiate and train the model
model = LightFM(loss='warp')
model.fit(data, epochs=30, num_threads=2)

# Evaluate the trained model
test_precision = precision_at_k(model, data['test'], k=5).mean()
print(test_precision)