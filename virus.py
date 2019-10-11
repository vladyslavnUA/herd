class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_num == 0.8
    assert virus.mortality_rate == 0.3

    malaria = Virus('malaria', 0.6, 0.1)
    assert malaria.name == "malaria"
    assert malaria.repro_num == 0.6
    assert malaria.mortality_rate == 0.1

    blackDeath = Virus('blackDeath', 0.8, 0.7)
    assert blackDeath.name == "blackDeath"
    assert blackDeath.repro_num == 0.8
    assert blackDeath.mortality_rate == 0.7

    chickenPox = Virus('chickenPox', 0.2, 0.275)
    assert chickenPox.name == "chickenPox"
    assert chickenPox.repro_rate == 0.2
    assert chickenPox.mortality_rate == 0.275

    ebola = Virus('ebola', 0.5, 0.8)
    assert ebola.name == "ebola"
    assert ebola.repro_rate == 0.5
    assert ebola.mortality_rate == 0.8

    measles = Virus('measles', 0.6, 0.9)
    assert measles.name == "measles"
    assert measles.repro_rate == 0.6
    assert measles.mortality_rate == 0.9
