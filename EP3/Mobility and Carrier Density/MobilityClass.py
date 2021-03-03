import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


class Mobility:
    DataAddress = ""
    sigma = 0.01
    title = ""
    x_label = "B-Field"
    x_units = "Teslas"
    y_label_nonlinear = "Rxx"
    y_label_linear = "Rxy"
    y_units = "Ohms"
    guess_xx = []
    guess_xy = []
    params_xx = []
    params_xy = []

    def __init__(self, address, guesscoefficientxx, guessoffsetxx, guesscoefficientxy, guessoffsetxy):
        self.DataAddress = address[:-8] + "_Rxx" + address[-8:]
        self.guess_xx = [guesscoefficientxx, guessoffsetxx]
        self.guess_xy = [guesscoefficientxy, guessoffsetxy]
        self.title = address[90:99]

    @staticmethod
    def linearfunc(bfield, coefficient, offset):
        return coefficient*bfield+offset

    @staticmethod
    def parabolicfunc(bfield, coefficient, offset):
        return coefficient*(bfield**2.0)+offset

    def chisquared(self, params, bfield, rxy):
        return np.sum((rxy - self.linearfunc(bfield, *params)) ** 2 / self.sigma ** 2)

    def pltinitial(self, data, xx, linearplot):
        bfieldguess = np.linspace(min(data[1, :]), max(data[1, :]), 500)
        if linearplot:
            rguess = self.linearfunc(bfieldguess, *self.guess_xy)
        else:
            rguess = self.parabolicfunc(bfieldguess, *self.guess_xx)

        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldguess, rguess, marker="", linestyle="-", linewidth=1, color="g", label="initial guess")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        if xx:
            plt.ylabel('{} [{}]'.format(self.y_label_nonlinear, self.y_units))
            plt.title(self.title + " Rxx Initial Guess")
        else:
            plt.ylabel('{} [{}]'.format(self.y_label_linear, self.y_units))
            plt.title(self.title + " Rxy Initial Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 1 for ' + self.title)
        if "OutPlane" in self.DataAddress:
            if xx:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxx_Initial" + ".png"
            else:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxy_Initial" + ".png"
        elif xx:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Rxx_Initial" + ".png"
        else:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Initial" + ".png"
        plt.savefig(address)
        plt.clf()

    def pltfit(self, data, xx, linearplot):
        if linearplot:
            self.params_xy, cov = cf(self.linearfunc, data[1, :], data[0, :],
                                     sigma=self.sigma * np.ones(len(data[1, :])), p0=self.guess_xy, maxfev=10 ** 5)
            chi2 = self.chisquared(self.params_xy, data[1, :], data[0, :])
            dof = len(data[1, :]) - len(self.params_xy)
        else:
            self.params_xx, cov = cf(self.parabolicfunc, data[1, :], data[0, :],
                                     sigma=self.sigma * np.ones(len(data[1, :])), p0=self.guess_xx, maxfev=10 ** 5)
            chi2 = self.chisquared(self.params_xx, data[1, :], data[0, :])
            dof = len(data[1, :]) - len(self.params_xx)

        print("\nGoodness of fit - chi square measure:")
        print("Chi2 = {}, Chi2/dof = {}\n".format(chi2, chi2 / dof))

        cov = cov * dof / chi2
        paramserr = np.sqrt(np.diag(cov))

        print("Fit parameters:")
        if linearplot:
            param_names = ['Slope', 'Offset']
            for i in range(len(self.params_xy)):
                print('{} = {:.3e} +/- {:.3e}'.format(param_names[i], self.params_xy[i], paramserr[i]))
            bfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
            rxyfit = self.linearfunc(bfieldfit, *self.params_xy)
        else:
            param_names = ['Coefficient', 'Offset']
            for i in range(len(self.params_xx)):
                print('{} = {:.3e} +/- {:.3e}'.format(param_names[i], self.params_xx[i], paramserr[i]))
            bfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
            rxyfit = self.parabolicfunc(bfieldfit, *self.params_xx)

        plt.scatter(data[1, :], data[0, :], marker='.', label="measured data")
        plt.plot(bfieldfit, rxyfit, marker="", linestyle="-", linewidth=2, color="r", label=" fit")
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        if xx:
            plt.ylabel('{} [{}]'.format(self.y_label_nonlinear, self.y_units))
            plt.title(self.title + " Rxx Fitted Guess")
        else:
            plt.ylabel('{} [{}]'.format(self.y_label_linear, self.y_units))
            plt.title(self.title + " Rxy Fitted Guess")
        plt.legend(loc='best', numpoints=1)
        print('\nSaving plot 2 for ' + self.title)
        if "OutPlane" in self.DataAddress:
            if xx:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxx_Fitted" + ".png"
            else:
                address = self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxy_Fitted" + ".png"
        elif xx:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Rxx_Fitted" + ".png"
        else:
            address = self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Fitted" + ".png"
        plt.savefig(address)
        plt.clf()

    def pltresiduals(self, data, xx, linearplot):
        if linearplot:
            rfit = self.linearfunc(data[1, :], *self.params_xy)
        else:
            rfit = self.parabolicfunc(data[1, :], *self.params_xx)
        residual = data[0, :] - rfit

        if xx:
            plt.title(self.title + " Rxx Residuals")
        else:
            plt.title(self.title + " Rxy Residuals")
        plt.scatter(data[1, :], residual, marker='.', label="residual (y-y_fit)")
        plt.hlines(0, np.min(data[1, :]), np.max(data[1, :]), lw=2, alpha=0.8)
        plt.xlabel('{} [{}]'.format(self.x_label, self.x_units))
        plt.ylabel('y-y_fit [{}]'.format(self.y_units))
        plt.legend(loc='best', numpoints=1)

        print('\nSaving plot 3 for ' + self.title)
        if "OutPlane" in self.DataAddress:
            if xx:
                plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxx_Residuals" + ".png")
            else:
                plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_InPlane_Rxy_Residuals" + ".png")
        elif xx:
            plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Rxx_Residuals" + ".png")
        else:
            plt.savefig(self.DataAddress[:90] + "Graphs/" + self.title + "_Rxy_Residuals" + ".png")
        plt.clf()

    def main(self, rxyzero):
        rxxdata = np.loadtxt(self.DataAddress)
        address = list(self.DataAddress)
        address[-9] = 'y'
        rxyinit = np.loadtxt("".join(address))

        if self.title == "PST236 R5":
            rxxdataprime = rxxdata[:, np.where(np.abs(rxxdata[1]) < 1)][:, 0, :]
        elif not self.title == "PST380 I2":
            rxxdataprime = rxxdata[:, np.where(np.abs(rxxdata[1]) > 0.2)][:, 0, :]
            rxxdataprime = rxxdataprime[:, np.where(np.abs(rxxdataprime[1]) < 3)][:, 0, :]
        else:
            rxxdataprime = rxxdata

        self.pltinitial(rxxdataprime, True, False)
        self.pltfit(rxxdataprime, True, False)
        self.pltresiduals(rxxdataprime, True, False)

        rxyprime = rxyinit - (rxyzero / self.parabolicfunc(0, *self.params_xx)) * rxxdata

        self.pltinitial(rxyprime, False, True)
        self.pltfit(rxyprime, False, True)
        self.pltresiduals(rxyprime, False, True)

        return [self.params_xx, self.params_xy]
