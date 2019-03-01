import random


class BayesDice:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.prior = {die: 0.20 for die in self.dice}
    # ------------------------------------------------------------ #

    def choose_die(self):
        self.die = random.choice(self.dice)
        print('Our belief before starting the experiment is equally distributed', self.prior)
        print('-' * 50)
        print('selected die is {}, we dont know this, we need to find through experiment and verify'.format(self.die))
        print('-' * 50)
    # ------------------------------------------------------------ #

    def roll_die(self):
        return random.randint(1, self.die)
    # ------------------------------------------------------------ #

    def update_priors(self, roll):
        evidence = list(map(lambda die: (0 if roll > die else (1 / die)) * self.prior[die], self.dice))
        self.prior = {self.dice[i]: individual_evidence / sum(evidence) for i, individual_evidence in enumerate(evidence)}
        self.debug(roll, evidence)
    # ------------------------------------------------------------ #

    def debug(self, roll, evidence):
        print('roll a die')
        print('roll:', roll)
        print('evidence of getting {} based on our belief is: {}'.format(roll, evidence))
        print(' ')
        print('updating our belief based on evidence', self.prior)
        print('-' * 50)
    # ------------------------------------------------------------ #
