# -*- coding: utf-8 -*-
"""Example for R-graph
"""
# Author: Michiel Bongaerts (but not author of the R-graph method)
# License: BSD 2 clause


from __future__ import division
from __future__ import print_function

import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pyod.models.rgraph import RGraph
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print


if __name__ == "__main__":

    contamination = 0.1  # percentage of outliers
    n_train = 100  # number of training points
    n_test = 25  # number of testing points

    # Generate sample data
    X_train, X_test, y_train, y_test = generate_data(
        n_train=n_train,
        n_test=n_test,
        n_features=70,
        contamination=contamination,
        behaviour="new",
        random_state=42,
    )

<<<<<<< HEAD:examples/rgraph_example.py
    # train R-graph detector
    clf_name = 'R-graph'
    clf = RGraph(n_nonzero = 100, transition_steps = 20 , gamma = 50, blocksize_test_data = 5,
                 tau = 1, preprocessing=True, active_support = False, gamma_nz = False,
                 algorithm= 'lasso_lars', maxiter= 40, verbose =1 )

    clf.fit(X_train)


=======
    # train AutoEncoder detector
    clf_name = 'AnoGAN'
    clf = AnoGAN(G_layers=[10, 20], D_layers=[20, 2],
                 preprocessing=True, index_D_layer_for_recon_error=1,
                 epochs=200, contamination=contamination, verbose=1)

    clf.fit(X_train)

>>>>>>> c2839e0c6acd08b219398804326b43ba3e262af4:examples/anogan_example.py
    # get the prediction labels and outlier scores of the training data
    y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
    y_train_scores = clf.decision_scores_  # raw outlier scores

    # # get the prediction on the test data
    y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
    y_test_scores = clf.decision_function(X_test)  # outlier scores

    # evaluate and print the results
    print("\nOn Training Data:")
    evaluate_print(clf_name, y_train, y_train_scores)
    print("\nOn Test Data:")
    evaluate_print(clf_name, y_test, y_test_scores)
<<<<<<< HEAD:examples/rgraph_example.py


=======

    # visualize the results
    visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
              y_test_pred, show_figure=True, save_figure=False)

    clf.plot_learning_curves(window_smoothening=30)
>>>>>>> c2839e0c6acd08b219398804326b43ba3e262af4:examples/anogan_example.py
