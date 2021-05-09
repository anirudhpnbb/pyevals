from pyevals import BuildClassification
from pyevals import BuildRegression
from pyevals import Plots
import warnings
from pkgutil import find_loader

pandas_installed = find_loader("pandas") is not None

if pandas_installed:
    import pandas as pd

warnings.filterwarnings('ignore')


class BuildPlots:
    def __init__(self, data, CategoricalFeatures, ContinuousFeatures):
        """
        :param data: Your DataSet
        :param CategoricalFeatures: List of Categorical Features of the DataSet
        :param ContinuousFeatures: List of Continuous Features of the DataSet
        """
        self.data = data
        self.CategoricalFeatures = CategoricalFeatures
        self.ContinuousFeatures = ContinuousFeatures

        print("Building the plots and a folder is being generated."
              " Keep watching your current directory for any changes.")
        Plots.MakePlots(self.data, self.CategoricalFeatures, self.ContinuousFeatures)
        print("Folder with various plots created.")


class build:

    def __init__(self, X_train, X_test, y_train, y_test, model):
        """
        :param X_train: Your X_train training data
        :param X_test:  Your X_test to test
        :param y_train: your y_train training data
        :param y_test:  Actual outcomes
        :parm model:   Which model you want to pass either Classification or Regression
        :return:  Will Return you a data frame with all classification algorithms.
        """
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model = model

    def evaluate(self):
        """
        This will evaluate the accuracy , recall score ,
        precision score , RocAuc score , f1 score for the
        13 algorithms in classification and will evaluate the 
        RSquaredError , AdjustedRSquaredError , MeanAbsoluteError ,
        MeanSquaredError , RootMeanSquaredError.
        Classification Algorithms : 
        kNearestNeighbor , LogisticRegression , DecisionTree Classifier
        , SupportVector Classifier , QuadraticDiscriminant Analysis ,
        SGD Classifier , AdaBoost , Caliberated Classifier , 
        Multinomial NavieBayes ,  Bernoulli NavieBayes , Gaussian NaiveBayes.
        
        Regression Algorithms :
        LinearRegression, PolynomialRegression, RidgeRegression,
        LassoRegression, SupportVectorRegressor, GradientBoostingRegression, 
        PLSRegression.
        """
        try:

            if self.model.lower() == 'classification':
                algorithms = ["KNN", "LogisticRegression", "DecisionTreeClassifier",
                              "RandomForestClassifier", "SupportVectorClassifier", "QuadraticDiscriminantSnalysis",
                              "SGDClassifier", "AdaBoost", "CalibratedClassifier", "MultinomialNB",
                              "BernoulliNB", "GaussianNB"]

                KNearestNeighbor = BuildClassification.KNearestNeighbor(self.X_train, self.X_test, self.y_train,
                                                                        self.y_test)
                LogisticReg = BuildClassification.LogisticReg(self.X_train, self.X_test, self.y_train, self.y_test)
                DecisionTree = BuildClassification.DecisionTree(self.X_train, self.X_test, self.y_train, self.y_test)
                RandomForest = BuildClassification.RandomForest(self.X_train, self.X_test, self.y_train, self.y_test)
                SupportVector = BuildClassification.SupportVector(self.X_train, self.X_test, self.y_train, self.y_test)
                QuadraticDiscriminant = BuildClassification.QuadraticDiscriminant(self.X_train, self.X_test,
                                                                                  self.y_train, self.y_test)
                SophisticatedGradientDescent = BuildClassification.SophisticatedGradientDescent(self.X_train,
                                                                                                self.X_test,
                                                                                                self.y_train,
                                                                                                self.y_test)
                AdaBoost = BuildClassification.AdaBoost(self.X_train, self.X_test, self.y_train, self.y_test)
                CalibratedClassifier = BuildClassification.CalibratedClassifier(self.X_train, self.X_test, self.y_train,
                                                                                self.y_test)
                MultinomialNaiveBayes = BuildClassification.MultinomialNaiveBayes(self.X_train, self.X_test,
                                                                                  self.y_train, self.y_test)
                BernoulliNaiveBayes = BuildClassification.BernoulliNaiveBayes(self.X_train, self.X_test, self.y_train,
                                                                              self.y_test)
                GaussianNaiveBayes = BuildClassification.GaussianNaiveBayes(self.X_train, self.X_test, self.y_train,
                                                                            self.y_test)

                functions = [KNearestNeighbor, LogisticReg, DecisionTree, RandomForest,
                             SupportVector, QuadraticDiscriminant, SophisticatedGradientDescent,
                             AdaBoost, CalibratedClassifier, MultinomialNaiveBayes,
                             BernoulliNaiveBayes, GaussianNaiveBayes]

                Accuracy = [functions[algorithm][0] for algorithm in range(len(functions))]
                RecallScore = [functions[algorithm][1] for algorithm in range(len(functions))]
                PresicionScore = [functions[algorithm][2] for algorithm in range(len(functions))]
                RocAucScore = [functions[algorithm][3] for algorithm in range(len(functions))]
                f1Score = [functions[algorithm][4] for algorithm in range(len(functions))]

                df = {"Accuracy": Accuracy, "RecallScore": RecallScore,
                      "PresicionScore": PresicionScore, "RocAucScore": RocAucScore,
                      "f1Score": f1Score}

                df = pd.DataFrame(df, index=algorithms)

                def highlight_max(s):
                    is_max = s == s.max()
                    return ['background-color: yellow' if v else ' ' for v in is_max]

                return df.style.apply(highlight_max)

            elif self.model.lower() == 'regression':

                algorithms = ["LinearRegression", "PolynomialRegression", "RidgeRegression", "LassoRegression",
                              "SupportVectorRegressor", "GradientBoostingRegression", "PLSRegression", "DTRegressor",
                              "KNNRegressor", "RFRegressor"]

                LinearReg = BuildRegression.LinearReg(self.X_train, self.X_test, self.y_train, self.y_test)
                PolynomialRegression = BuildRegression.PolynomialRegression(self.X_train, self.X_test, self.y_train,
                                                                            self.y_test)
                RidgeRegression = BuildRegression.RidgeRegression(self.X_train, self.X_test, self.y_train, self.y_test)
                LassoRegression = BuildRegression.LassoRegression(self.X_train, self.X_test, self.y_train, self.y_test)
                SupportVectorRegressor = BuildRegression.SupportVectorRegressor(self.X_train, self.X_test, self.y_train,
                                                                                self.y_test)
                GradientBoostingRegression = BuildRegression.GradientBoostingRegression(self.X_train, self.X_test,
                                                                                        self.y_train, self.y_test)
                PartialLeastSquares = BuildRegression.PartialLeastSquares(self.X_train, self.X_test, self.y_train,
                                                                          self.y_test)
                DecisionTreeReg = BuildRegression.DTRegressor(self.X_train, self.X_test, self.y_train, self.y_test)
                RandomForestReg = BuildRegression.RFRegressor(self.X_train, self.X_test, self.y_train, self.y_test)
                KNNReg = BuildRegression.KNNRegressor(self.X_train, self.X_test, self.y_train, self.y_test)

                functions = [LinearReg, PolynomialRegression, RidgeRegression, LassoRegression, SupportVectorRegressor,
                             GradientBoostingRegression, PartialLeastSquares, DecisionTreeReg, RandomForestReg, KNNReg]

                R2Score = [functions[algorithm][0] for algorithm in range(len(functions))]
                AdjustedR2 = [functions[algorithm][1] for algorithm in range(len(functions))]
                MeanAbsoluteError = [functions[algorithm][2] for algorithm in range(len(functions))]
                MeanSquaredError = [functions[algorithm][3] for algorithm in range(len(functions))]
                RootMeanSquaredError = [functions[algorithm][4] for algorithm in range(len(functions))]

                df = {"1-R2Score": R2Score, "1-AdjustedR2": AdjustedR2, "MeanAbsoluteError": MeanAbsoluteError,
                      "MeanSquaredError": MeanSquaredError, "RootMeanSquaredError": RootMeanSquaredError}

                df = pd.DataFrame(df, index=algorithms)

                def highlight_min(s):
                    is_min = s == s.min()
                    return ['background-color: yellow' if v else ' ' for v in is_min]

                return df.style.apply(highlight_min)

            else:
                print("Check the Arguments Passed.\nPlease Check the 'Usage' in the PyPi.")

        except Exception as ex:
            print("Please check the arguments Passed.{0}".format(ex))
