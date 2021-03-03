import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


class Density:
    DataAddress = ""
    sigma = 0.01
    title = ""
    x_label = "B-Field"
    x_units = "Teslas"
    y_label = "Rxy"
    y_units = "Ohms"
    guess = []
    params = []

    def __init__(self, address, guesscoefficient, guessoffset):
        self.DataAddress = address[:-8] + "_Rxy" + address[-8:]
        self.guess = [guesscoefficient, guessoffset]
        self.title = address[90:99]

    @staticmethod
    def linearfunc(bfield, coefficient, offset):
        return coefficient*bfield+offset

    def chisquared(self, params, bfield, rxy):
        return np.sum((rxy - self.linearfunc(bfield, *params)) ** 2 / self.sigma ** 2)

    def pltinitial(self, data):
        bfieldguess = np.linspace(min(data[1, :]), max(data[1, :]), 500)
        rxyguess = self.linearfunc(bfieldguess, *self.guess)
        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldguess, rxyguess, marker="", linestyle="-", linewidth=1, color="g", label="initial guess")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('{} [{}]'.format(self.y_label, self.y_units))
        plt.title(self.title + " Rxy Initial Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 1 for ' + self.title)
        plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Initial_Density" + ".png")
        plt.clf()

    def pltfit(self, data):
        self.params, cov = cf(self.linearfunc, data[1, :], data[0, :],
                              sigma=self.sigma * np.ones(len(data[1, :])),
                              p0=self.guess, maxfev=10 ** 5)

        chi2 = self.chisquared(self.params, data[1, :], data[0, :])
        dof = len(data[1, :]) - len(self.params)
        print("\nGoodness of fit - chi square measure:")
        print("Chi2 = {}, Chi2/dof = {}\n".format(chi2, chi2 / dof))

        cov = cov * dof / chi2
        paramserr = np.sqrt(np.diag(cov))

        param_names = ['Slope', 'Offset']

        print("Fit parameters:")
        for i in range(len(self.params)):
            print('{} = {:.3e} +/- {:.3e}'.format(param_names[i], self.params[i], paramserr[i]))

        bfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
        rxyfit = self.linearfunc(bfieldfit, *self.params)

        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldfit, rxyfit, marker="", linestyle="-", linewidth=2, color="r", label=" fit")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('{} [{}]'.format(self.y_label, self.y_units))
        plt.title(self.title + " Rxy Fitted Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 2 for ' + self.title)
        plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Fitted_Density" + ".png")
        plt.clf()

    def pltresiduals(self, data):
        rxyfit = self.linearfunc(data[1, :], *self.params)
        residual = data[0, :] - rxyfit

        plt.title(self.title + " Rxy Residuals")
        plt.scatter(data[1, :], residual, marker='.', label="residual (y-y_fit)")
        plt.hlines(0, np.min(data[1, :]), np.max(data[1, :]), lw=2, alpha=0.8)
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('y-y_fit [{}]'.format(self.y_units))
        plt.legend(loc='best', numpoints=1)

        print('\nSaving plot 3 for ' + self.title)
        plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Residuals_Density" + ".png")
        plt.clf()

    def main(self):
        data = np.loadtxt(self.DataAddress)

        self.pltinitial(data)
        self.pltfit(data)
        self.pltresiduals(data)
        return self.params
