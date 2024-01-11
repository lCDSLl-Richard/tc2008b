import agentpy as ap
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from pprint import pprint


class WealthAgent(ap.Agent):
    def setup(self):
        self.internal_states = [1]

    def see(self, e):
        return e.random()

    def next(self, i, p):
        if i > 0:
            self.internal_states[0] -= 1
            return list(p)[0]
        return None

    def action(self, o):
        if o:
            o.internal_states[0] += 1

    def step(self):
        self.action(
            self.next(
                self.internal_states[0],
                self.see(self.model.agents),
            )
        )


def gini(x):
    x = np.array(x)
    mad = np.abs(np.subtract.outer(x, x)).mean()  # Mean absolute difference
    rmad = mad / np.mean(x)  # Relative mean absolute difference
    return 0.5 * rmad


class WealthModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, WealthAgent)

    def step(self):
        self.agents.step()

    def update(self):
        internal_states = [agent.internal_states[0] for agent in self.agents]
        self.record("Gini Coefficient", gini(internal_states))

    def end(self):
        self.agents.record("internal_states")


def main():
    parameters = {"agents": 100, "steps": 100, "seed": 42}

    model = WealthModel(parameters)
    results = model.run()

    pprint(results)
    pprint(results.info)
    pprint(results.variables.WealthModel.head())

    _, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(12, 6))

    data = results.variables.WealthModel
    data.plot(ax=ax1)
    agent_data = results.variables.WealthAgent["internal_states"].apply(lambda x: x[0])

    sns.histplot(data=agent_data, binwidth=1, ax=ax2)
    ax3.scatter(range(len(agent_data)), agent_data.reset_index().iloc[:, 2], alpha=0.5)

    plt.show()


if __name__ == "__main__":
    main()
