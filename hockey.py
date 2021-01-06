import csv

class League:
    def __init__(self, teams=None):
        self.teams = [] if teams is None else teams

    def add_team(self, team):
        self.teams.append(team)
        
    def get_team(self, owner):
        for team in self.teams:
            if team.get_owner() == owner:
                return team
            
    def show_league(self):
        for team in self.teams:
            team.get_roster()
            print()

class Team:
    def __init__(self, owner, budget=20, players=None, keepers=None, prospects=None, load=False):
        self.owner = owner
        self.players = [] if players is None else players
        self.keepers = [] if keepers is None else keepers
        self.prospects = [] if prospects is None else prospects
        self.budget = 350
        self.trade_budget = budget
        
        if load:
            self.load_from_file()

    def calculate_auction_budget(self):
        keeper_cost = sum(keeper.get_cost() for keeper in self.keepers)
        return self.budget - keeper_cost + self.trade_budget
    
    def load_from_file(self):
        with open("teams/" + self.owner + ".csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == 'True':
                    self.keepers.append(Player(row[0], row[1], True, row[3], False))
                elif row[4] == 'True':
                    self.prospects.append(Player(row[0], row[1], False, row[3], True))
                else:
                    self.players.append(Player(row[0], row[1], False, row[3], False))
    
    def get_owner(self):
        return self.owner
    
    def add_player(self, player):
        self.players.append(player)
    
    def add_keeper(self, player):
        self.keepers.append(player)
        
    def add_prospect(self, player):
        self.prospects.append(player)
        
    def get_roster(self):
        print("Roster for {}".format(self.owner))
        print()
        print("Players: ")
        for player in self.players:
            print(player)
        print()
        print("Keepers: ")
        for keeper in self.keepers:
            print(keeper)
        print()
        print("Prospects: ")
        for prospect in self.prospects:
            print(prospect)
            
    def write_to_file(self):
        with open("teams/" + self.owner + ".csv", "w") as f:
            for player in self.players:
                f.write(player.info_for_file() + "\n")
            for keeper in self.keepers:
                f.write(keeper.info_for_file() + "\n")
            for prospect in self.prospects:
                f.write(prospect.info_for_file() + "\n")

class Player:
    def __init__(self, name, cost, keeper=False, contract_length=0, prospect=False):
        self.name = name
        self.cost = cost
        self.keeper = keeper
        self.contract_length = contract_length
        self.prospect = prospect

    def info_for_file(self):
        return "{0},{1},{2},{3},{4}".format(self.name, self.cost, self.keeper, self.contract_length, self.prospect)
    
    def get_cost(self):
        return int(self.cost)
    
    def is_keeper(self):
        return self.keeper
    
    def __repr__(self):
        if self.keeper:
            return "{0} costs ${1} and is signed to a {2} year contract".format(self.name, self.cost, self.contract_length)
        elif self.prospect:
            return "{0} is a prospect".format(self.name)
        else:
            return "{0} costs ${1}".format(self.name, self.cost)
        
    def __str__(self):
        if self.keeper:
            return "{0} costs ${1} and is signed to a {2} year contract".format(self.name, self.cost, self.contract_length)
        elif self.prospect:
            return "{0} is a prospect".format(self.name)
        else:
            return "{0} costs ${1}".format(self.name, self.cost)
        
class DraftPick:
    def __init__(self, original_owner, round):
        self.original_owner = original_owner
        self.current_owner = original_owner
        self.round = round
    
    def __repr__(self):
        return "Round {0} pick belongs to {1}".format(self.round, self.current_owner)
