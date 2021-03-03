import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


class Linearity:
    DataAddress = ""
    sigma = 0.01
    title = ""
    x_label = "B-Field"
    x_units = "Teslas"
    y_label = "Rxx"
    y_units = "Ohms"
    guess_neg = []
    guess_pos = []
    params_neg = []
    params_pos = []

    def __init__(self, dataaddress, guessslope, guessoffset):
        self.DataAddress = dataaddress[:-8] + "_Rxx" + dataaddress[-8:]
        self.guess_neg = [-1*guessslope, guessoffset]
        self.guess_pos = [guessslope, guessoffset]
        self.title = dataaddress[90:99]

    @staticmethod
    def linearfunc(bfield, slope, offset):
        return slope*bfield + offset

    def chisquared(self, params, bfield, rxy):
        return np.sum((rxy - self.linearfunc(bfield, *params)) ** 2 / self.sigma ** 2)

    def pltinitial(self, data, neg):
        bfieldguess = np.linspace(min(data[1, :]), max(data[1, :]), 500)
        if neg:
            rguess = self.linearfunc(bfieldguess, *self.guess_neg)
        else:
            rguess = self.linearfunc(bfieldguess, *self.guess_pos)

        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldguess, rguess, marker="", linestyle="-", linewidth=1, color="g", label="initial guess")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('{} [{}]'.format(self.y_label, self.y_units))
        plt.title(self.title + " Rxy Initial Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 1 for ' + self.title)

        if "OutPlane" in self.DataAddress:
            if neg:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Initial_Neg" + ".png"
            else:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Initial_Pos" + ".png"
        elif neg:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Initial_Neg" + ".png"
        else:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Initial_Pos" + ".png"
        plt.savefig(address)
        plt.clf()

    def pltfit(self, data, neg):
        if neg:
            self.params_neg, cov = cf(self.linearfunc, data[1, :], data[0, :],
                                      sigma=self.sigma * np.ones(len(data[1, :])), p0=self.guess_neg, maxfev=10 ** 5)
            chi2 = self.chisquared(self.params_neg, data[1, :], data[0, :])
            dof = len(data[1, :]) - len(self.params_neg)
        else:
            self.params_pos, cov = cf(self.linearfunc, data[1, :], data[0, :],
                                      sigma=self.sigma * np.ones(len(data[1, :])), p0=self.guess_pos, maxfev=10 ** 5)
            chi2 = self.chisquared(self.params_pos, data[1, :], data[0, :])
            dof = len(data[1, :]) - len(self.params_pos)

        print("\nGoodness of fit - chi square measure:")
        print("Chi2 = {}, Chi2/dof = {}\n".format(chi2, chi2 / dof))
        cov = cov * dof / chi2
        paramserr = np.sqrt(np.diag(cov))

        print("Fit parameters:")
        param_names = ['Slope', 'Offset']
        if neg:
            for i in range(len(self.params_neg)):
                print('{} = {:.3e} +/- {:.3e}'.format(param_names[i], self.params_neg[i], paramserr[i]))
            bfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
            rxyfit = self.linearfunc(bfieldfit, *self.params_neg)
        else:
            for i in range(len(self.params_pos)):
                print('{} = {:.3e} +/- {:.3e}'.format(param_names[i], self.params_pos[i], paramserr[i]))
            bfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
            rxyfit = self.linearfunc(bfieldfit, *self.params_pos)

        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldfit, rxyfit, marker="", linestyle="-", linewidth=2, color="r", label=" fit")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('{} [{}]'.format(self.y_label, self.y_units))
        plt.title(self.title + " Rxx Fitted Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 2 for ' + self.title)

        if "OutPlane" in self.DataAddress:
            if neg:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Fitted_Neg" + ".png"
            else:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Fitted_Pos" + ".png"
        elif neg:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Fitted_Neg" + ".png"
        else:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Fitted_Pos" + ".png"
        plt.savefig(address)
        plt.clf()

    def pltresiduals(self, data, neg):
        if neg:
            rfit = self.linearfunc(data[1, :], *self.params_neg)
        else:
            rfit = self.linearfunc(data[1, :], *self.params_pos)
        residual = data[0, :] - rfit

        plt.title(self.title + " Rxx Residuals")
        plt.scatter(data[1, :], residual, marker='.', label="residual (y-y_fit)")
        plt.hlines(0, np.min(data[1, :]), np.max(data[1, :]), lw=2, alpha=0.8)
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('y-y_fit [{}]'.format(self.y_units))
        plt.legend(loc='best', numpoints=1)

        print('\nSaving plot 3 for ' + self.title)
        if "OutPlane" in self.DataAddress:
            if neg:
                plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Residuals_Neg" + ".png")
            else:
                plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Linear_Residuals_Pos" + ".png")
        elif neg:
            plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Residuals_Neg" + ".png")
        else:
            plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Linear_Residuals_Pos" + ".png")
        plt.clf()

    def main(self, cutoff, is236):
        rxxdata = np.loadtxt(self.DataAddress)
        rxxdatapos = rxxdata[:, np.where(rxxdata[1] > cutoff)][:, 0, :]
        rxxdataneg = rxxdata[:, np.where(rxxdata[1] < -1*cutoff)][:, 0, :]
        if is236:
            rxxdatapos = rxxdatapos[:, np.where(rxxdatapos[1] < 8)][:, 0, :]
            rxxdataneg = rxxdataneg[:, np.where(rxxdataneg[1] > -8)][:, 0, :]

        self.pltinitial(rxxdatapos, False)
        self.pltfit(rxxdatapos, False)
        self.pltresiduals(rxxdatapos, False)

        self.pltinitial(rxxdataneg, True)
        self.pltfit(rxxdataneg, True)
        self.pltresiduals(rxxdataneg, True)

        return [self.params_neg, self.params_pos]
