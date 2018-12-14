from surprise import SVD, NMF, SVDpp, SlopeOne, KNNWithMeans, KNNWithZScore, CoClustering
from surprise import Dataset, Reader
from surprise.model_selection import cross_validate
from collections import defaultdict

sim_options = {'name': 'pearson_baseline',
               'shrinkage': 0  # no shrinkage
               }


def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.
    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.
    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


# Load the movielens-100k dataset (download it if needed).
reader = Reader(line_format='user item rating', sep='\t',
                rating_scale=(0, 2))
data = Dataset.load_from_file('classification/data/cf_rec/u.train', reader=reader, rating_scale=(0, 2))
trainset = data.build_full_trainset()

algo = SVDpp(lr_all=.0001,reg_all=0.0001,verbose=True,init_std_dev=.0001,n_epochs=30)
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
algo.fit(trainset)
# print(algo.estimate('5218791','100642618'))
# algo = SVDpp()
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
# algo.fit(trainset)
# print(algo.predict('5218791','100642618'))
# algo = NMF()
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
# algo.fit(trainset)
# print(algo.predict('5218791','100642618'))
# # Use the famous SVD algorithm.
# algo = SlopeOne()
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
# algo.fit(trainset)
# print(algo.predict('5218791','100642618'))
# algo = KNNWithMeans(sim_options=sim_options)
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
# algo.fit(trainset)
# print(algo.predict('5218791','100642618'))
# algo = KNNWithZScore(sim_options=sim_options)
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# # Run 5-fold cross-validation and print results.
# algo.fit(trainset)
# print(algo.predict('5218791','100642618'))
# algo = CoClustering(n_cltr_u=300, n_cltr_i=600, n_epochs=100, verbose=True)
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
# Run 5-fold cross-validation and print results.
# algo.fit(trainset)
print(algo.predict('5218791', '100648984'))
print(algo.estimate('5218791', '100648984'))
print(algo.predict('52550', '100644648'))
print(algo.estimate('52550', '100644648'))
print(algo.predict('10663402', '100651469'))
print(algo.estimate('10663402', '100651469'))
