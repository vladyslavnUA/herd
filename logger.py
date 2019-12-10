import io
from person import Person
from virus import Virus

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

        log_textfile = open(self.file_name, mode='w+')
        print(log_textfile.read())
        log_textfile.close()

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_rate):
        with open(self.file_name, mode='w') as log_textfile:
            metadata = f'Population Size: {pop_size}\nVaccination Percentage: {vacc_percentage}\nVirus Name: {virus_name}\nMortality Rate: {mortality_rate}\nBasic Reproduction Number: {basic_repro_rate}\n'
            log_textfile.write(metadata)
        log_textfile.close()

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        with open(self.file_name, 'a') as log_textfile:
            log_textfile.write('Interaction Logs: \n')
            if did_infect:
                infection_stat = str(person._id) + \
                    'infects ' + str(person._id)
                    print(" ")
            elif random_person.is_vaccinated:
                infection_stat = str(person._id) + \
                    ' did not infect ' + str(random_person._id)
                    print(" ")
            else:
                infection_stat = str(person._id) + ' did not infect ' + str(random_person._id) + ' because ' + str(random_person._id) + ' is vaccinated or already sick.\n'
                # log_textfile.write(f"{person.ID} infects {random_person.ID} \n")
            # log_textfile.write(f"FATAL: random_person_vacc: {random_person_vacc}; random_person_sick: {random_person_sick}; did_infect: {did_infect}\n")
            
            log_textfile.write(infection_stat)
            log_textfile.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''

        with open(self.file_name, mode='a') as log_textfile:
            if did_die_from_infection:
                log_textfile.write(f"Person {person._id} died from infection\n")
            else:
                log_textfile.write(f"Person {person._id} survived infection.\n")
        log_textfile.close()

    def log_time_step(self, virus_name, time_step_counter, current_infected, additional_deaths, additional_vacc,
                                      total_infected, total_dead,
                                      total_vaccinated):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
