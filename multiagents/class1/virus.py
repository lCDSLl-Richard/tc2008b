import agentpy as ap
import networkx as nx
import random

import matplotlib.pyplot as plt
import seaborn as sns

from enum import Enum

from pprint import pprint


class PersonState(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2


class Person(ap.Agent):
    def setup(self):
        self.condition = PersonState.SUSCEPTIBLE

    def being_sick(self):
        rng = self.model.random

        for n in self.network.neighbors(self):
            if (
                n.condition == PersonState.SUSCEPTIBLE
                and self.p.infection_chance > rng.random()
            ):
                n.condition = PersonState.INFECTED

        if self.p.recovery_chance > rng.random():
            self.condition = PersonState.RECOVERED


class VirusModel(ap.Model):
    def setup(self):
        graph = nx.watts_strogatz_graph(
            self.p.population, self.p.number_of_neighbors, self.p.network_randomness
        )

        self.agents = ap.AgentList(self, self.p.population, Person)
        self.network = self.agents.network = ap.Network(self, graph)
        self.network.add_agents(self.agents, self.network.nodes)

        I0 = int(self.p.initial_infection_share * self.p.population)
        self.agents.random(I0).condition = PersonState.INFECTED

    def update(self):
        for i, c in enumerate(("S", "I", "R")):
            n_agents = len(self.agents.select(self.agents.condition == i))
            self[c] = n_agents / self.p.population
            self.record(c)

        # Stop simulation if disease is gone
        if self.I == 0:
            self.stop()

    def step(self):
        self.agents.select(self.agents.condition == PersonState.INFECTED).being_sick()

    def end(self):
        self.report("Total share infected", self.I + self.R)
        self.report("Peak share infected", max(self.log["I"]))


parameters = {
    "population": 1000,
    "infection_chance": 0.3,
    "recovery_chance": 0.1,
    "initial_infection_share": 0.1,
    "number_of_neighbors": 2,
    "network_randomness": 0.5,
}


def main():
    parameters = {
        "population": 1000,
        "infection_chance": 0.3,
        "recovery_chance": 0.1,
        "initial_infection_share": 0.1,
        "number_of_neighbors": 2,
        "network_randomness": 0.5,
    }
    model = VirusModel(parameters)
    results = model.run()
    pprint(results)


if __name__ == "__main__":
    main()
