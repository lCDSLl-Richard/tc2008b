import agentpy as ap
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


class WealthAgent(ap.Agent):
    def setup(self):
        self.wealth = 1

    def wealth_transfer(self):
        if self.wealth > 0:
            partner = self.model.agents.random()
            partner.wealth += 1
            self.wealth -= 1


def gini(x):
    x = np.array(x)
    mad = np.abs(np.subtract.outer(x, x)).mean()  # Mean absolute difference
    rmad = mad / np.mean(x)  # Relative mean absolute difference
    return 0.5 * rmad


class WealthModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, WealthAgent)

    def step(self):
        self.agents.wealth_transfer()

    def update(self):
        self.record("Gini Coefficient", gini(self.agents.wealth))

    def end(self):
        self.agents.record("wealth")


def main():
    parameters = {"agents": 100, "steps": 100, "seed": 42}

    model = WealthModel(parameters)
    results = model.run()

    print(results)
    print(results.info)
    print(results.variables.WealthModel.head())

    _, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(12, 6))

    data = results.variables.WealthModel
    data.plot(ax=ax1)

    sns.histplot(data=results.variables.WealthAgent, binwidth=1, ax=ax2)
    agents_data = results.variables.WealthAgent
    ax3.scatter(range(len(agents_data)), agents_data["wealth"], alpha=0.5)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
