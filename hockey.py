import csv

class League:
    def __init__(self, teams=None):
        self.teams = teams


class Team:
    def __init__(self, owner, players=None, keepers=None, prospects=None):
        self.owner = owner
        self.players = [] if players is None else players
        self.keepers = [] if keepers is None else keepers
        self.prospects = [] if prospects is None else prospects

    def load_from_file(self, name):
        with open(name + ".txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] is True:
                    self.keepers.append(Player(row[0], row[1], row[2], row[3]))
                else:
                    self.players.append(Player(row[0], row[1], row[2], row[3]))
    
    def add_player(self, player):
        self.players.append(player)
    
    def add_keeper(self, player):
        self.keepers.append(player)
        
    def add_prospect(self, player):
        self.prospects.append(player)
        
    def get_roster(self):
        for player in self.players:
            print(player)
        for keeper in self.keepers:
            print(keeper)
        for prospect in self.prospects:
            print(prospect)
            
    def write_to_file(self):
        with open(self.owner + ".txt", "w") as f:
            for player in self.players:
                f.write(player.info_for_file())
            for keeper in self.keepers:
                f.write(keeper.info_for_file())

class Player:
    def __init__(self, name, cost, keeper=False, contract_length=0):
        self.name = name
        self.cost = cost
        self.keeper = keeper
        self.contract_length = contract_length

    def info_for_file(self):
        return "{0},{1},{2},{3}".format(self.name, self.cost, self.keeper, self.contract_length)
    
    def is_keeper(self):
        return self.keeper
    
    def __repr__(self):
        if self.keeper:
            return "{0} costs ${1} and is signed to a {2} year contract".format(self.name, self.cost, self.contract_length)
        else:
            return "{0} costs ${1}".format(self.name, self.cost)
        
    def __str__(self):
        if self.keeper:
            return "{0} costs ${1} and is signed to a {2} year contract".format(self.name, self.cost, self.contract_length)
        else:
            return "{0} costs ${1}".format(self.name, self.cost)