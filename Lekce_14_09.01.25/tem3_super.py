from team3 import Team, Human, Company

class SuperTeam(Team):
    def add_member(self, human: 'SuperHuman'):
        if type(human) is not SuperHuman:
            raise TypeError('SuperTeam member must be SuperHuman')

        super().add_member(human)


class SuperHuman(Human):
    pass


if __name__ == '__main__':
    my_company = Company('My Company')

    super_team = SuperTeam('Avanger', my_company)

    petr = SuperHuman('Petr')

    print(super_team)
    super_team.add_member(petr)

    print(super_team.members)
    print(petr.team)
