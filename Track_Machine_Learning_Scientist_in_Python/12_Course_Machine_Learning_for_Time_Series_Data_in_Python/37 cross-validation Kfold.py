import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.linear_model import LinearRegression
from sklearn.utils.multiclass import type_of_target
from sklearn.utils import column_or_1d
import warnings

def check_reg_targets(y_true, y_pred):
    # Check if both y_true and y_pred are regression targets
    y_true_type = type_of_target(y_true)
    y_pred_type = type_of_target(y_pred)
    if y_true_type not in ["continuous", "continuous-multioutput"] or \
       y_pred_type not in ["continuous", "continuous-multioutput"]:
        raise ValueError("y_true and y_pred should be continuous values for regression.")
    return y_true, y_pred

def r2_score(y_true, y_pred, *, sample_weight=None, multioutput="uniform_average"):
    """:math:`R^2` (coefficient of determination) regression score function.

    Best possible score is 1.0 and it can be negative (because the
    model can be arbitrarily worse). A constant model that always
    predicts the expected value of y, disregarding the input features,
    would get a :math:`R^2` score of 0.0.

    Read more in the :ref:`User Guide <r2_score>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Estimated target values.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    multioutput : {'raw_values', 'uniform_average', 'variance_weighted'}, \
            array-like of shape (n_outputs,) or None, default='uniform_average'

        Defines aggregating of multiple output scores.
        Array-like value defines weights used to average scores.
        Default is "uniform_average".

        'raw_values' :
            Returns a full set of scores in case of multioutput input.

        'uniform_average' :
            Scores of all outputs are averaged with uniform weight.

        'variance_weighted' :
            Scores of all outputs are averaged, weighted by the variances
            of each individual output.

        .. versionchanged:: 0.19
            Default value of multioutput is 'uniform_average'.

    Returns
    -------
    z : float or ndarray of floats
        The :math:`R^2` score or ndarray of scores if 'multioutput' is
        'raw_values'.

    Notes
    -----
    This is not a symmetric function.

    Unlike most other scores, :math:`R^2` score may be negative (it need not
    actually be the square of a quantity R).

    This metric is not well-defined for single samples and will return a NaN
    value if n_samples is less than two.

    References
    ----------
    .. [1] `Wikipedia entry on the Coefficient of determination
            <https://en.wikipedia.org/wiki/Coefficient_of_determination>`_

    Examples
    --------
    >>> from sklearn.metrics import r2_score
    >>> y_true = [3, -0.5, 2, 7]
    >>> y_pred = [2.5, 0.0, 2, 8]
    >>> r2_score(y_true, y_pred)
    0.948...
    >>> y_true = [[0.5, 1], [-1, 1], [7, -6]]
    >>> y_pred = [[0, 2], [-1, 2], [8, -5]]
    >>> r2_score(y_true, y_pred,
    ...          multioutput='variance_weighted')
    0.938...
    >>> y_true = [1, 2, 3]
    >>> y_pred = [1, 2, 3]
    >>> r2_score(y_true, y_pred)
    1.0
    >>> y_true = [1, 2, 3]
    >>> y_pred = [2, 2, 2]
    >>> r2_score(y_true, y_pred)
    0.0
    >>> y_true = [1, 2, 3]
    >>> y_pred = [3, 2, 1]
    >>> r2_score(y_true, y_pred)
    -3.0
    """
    # y_type, y_true, y_pred, multioutput = _check_reg_targets(
    #     y_true, y_pred, multioutput
    # )

    # y_type, y_true, y_pred, multioutput = check_reg_targets(y_true, y_pred)
    # check_consistent_length(y_true, y_pred, sample_weight)

    y_true, y_pred = check_reg_targets(y_true, y_pred)

    # if _num_samples(y_pred) < 2:
    #     msg = "R^2 score is not well-defined with less than two samples."
    #     warnings.warn(msg, UndefinedMetricWarning)
    #     return float("nan")
    if len(y_pred) < 2:
        warnings.warn("R^2 score is not well-defined with less than two samples.")
        return float("nan")

    if sample_weight is not None:
        sample_weight = column_or_1d(sample_weight)
        weight = sample_weight[:, np.newaxis]
    else:
        weight = 1.0

    numerator = (weight * (y_true - y_pred) ** 2).sum(axis=0, dtype=np.float64)
    denominator = (
        weight * (y_true - np.average(y_true, axis=0, weights=sample_weight)) ** 2
    ).sum(axis=0, dtype=np.float64)
    nonzero_denominator = denominator != 0
    nonzero_numerator = numerator != 0
    valid_score = nonzero_denominator & nonzero_numerator
    output_scores = np.ones([y_true.shape[1]])
    output_scores[valid_score] = 1 - (numerator[valid_score] / denominator[valid_score])
    # arbitrary set to zero to avoid -inf scores, having a constant
    # y_true is not interesting for scoring a regression anyway
    output_scores[nonzero_numerator & ~nonzero_denominator] = 0.0
    if isinstance(multioutput, str):
        if multioutput == "raw_values":
            # return scores individually
            return output_scores
        elif multioutput == "uniform_average":
            # passing None as weights results is uniform mean
            avg_weights = None
        elif multioutput == "variance_weighted":
            avg_weights = denominator
            # avoid fail on constant y or one-element arrays
            if not np.any(nonzero_denominator):
                if not np.any(nonzero_numerator):
                    return 1.0
                else:
                    return 0.0
    else:
        avg_weights = multioutput

    return np.average(output_scores, weights=avg_weights)

def visualize_predictions(results):
    fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    cmap = plt.get_cmap('viridis')
    norm = mcolors.Normalize(vmin=0, vmax=len(results)-1)
    
    # Loop through our model results to visualize them
    for ii, (prediction, score, indices) in enumerate(results):
        # Plot the predictions of the model in the order they were generated
        offset = len(prediction) * ii
        # axs[0].scatter(np.arange(len(prediction)) + offset, prediction, label='Iteration {}'.format(ii))
        axs[0].scatter(np.arange(len(prediction)) + offset, prediction, c=[ii] * len(prediction), cmap=cmap, norm=norm)
        # Plot the predictions of the model according to how time was ordered
        # axs[1].scatter(indices, prediction)
        axs[1].scatter(indices, prediction, c=[ii] * len(prediction), cmap=cmap, norm=norm)
    axs[0].legend(loc="best")
    axs[0].set(xlabel="Test prediction number", title="Predictions ordered by test prediction number")
    axs[1].set(xlabel="Time", title="Predictions ordered by time")
    plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs, label="Iteration")
    plt.show()

model = LinearRegression()
X = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\cv_X.csv'))
y = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\cv_y.csv'))

# Create KFold cross-validation object
from sklearn.model_selection import KFold
cv = KFold(n_splits=10, shuffle=False)

# Iterate through CV splits
results = []
for tr, tt in cv.split(X, y):
    # Fit the model on training data
    model.fit(X[tr], y[tr])
    
    # Generate predictions on the test data and collect
    prediction = model.predict(X[tt])
    score = r2_score(y[tt], prediction)
    # results.append((prediction, tt))
    results.append((prediction, score, tt))
    
# Custom function to quickly visualize predictions
visualize_predictions(results)