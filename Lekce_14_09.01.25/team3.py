class Company:
    def __init__(self, name: str):
        self.name = name


class Team:
    def __init__(self, name: str, company: Company):
        self.name = name
        self.company = company
        self.members = set()
    
    def __str__(self):
        return self.name
    
    def add_member(self, human: 'Human'):
        if human.team and human.team != self:
            raise ValueError(f'This member is already in another team: {human}')

        human.team = self
        self.members.add(human)

    def remove_member(self, human: 'Human'):
        if human in self.members:
            self.members.remove(human)
        
        if human.team is self:
            human.team = None


class Human:
    def __init__(self, name: str):
        self.name = name
        self.team: Team = None

    def __str__(self):
        return self.name

    def __repr__(self):
        # Human('Petr')
        return f"{self.__class__.__name__}('{self.name}')"


print(__name__, '<<<<<<<<<<<<<<<<<<<<<')
if __name__ == '__main__':
    firma1 = Company('Moje Firma 1')

    teamA = Team('Team A', firma1)
    teamB = Team('Team B', firma1)

    petr = Human('Petr')
    alex = Human('Alex')

    teamA.add_member(petr)
    teamA.add_member(alex)

    teamA.remove_member(alex)
    teamA.remove_member(petr)

    teamB.add_member(alex)
    teamB.add_member(petr)

    print(teamA.members)
    print(teamB.members)

    print(petr.team)
    print(alex.team)