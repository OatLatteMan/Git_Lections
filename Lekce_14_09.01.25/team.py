# team.py


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

    def add_member(self, employee: 'Employee'):
        employee.set_team(self)
        self.members.add(employee) # 

    def remove_member(self, employee: 'Employee'):
        self.members.remove(employee)

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.team = None

    def __str__(self):
        """ string reprezentace, která použije pro tisk nebo pro převod na str """
        return self.name

    def __repr__(self):
        """ string reprezentace slouží pro reprodukci stejného prvku """
        return f"Employee('{self.name}')"

    def set_team(self, new_team):
        if self.team:
            self.team.remove_member(self)

        self.team = new_team

# Udělejte třídu Employee
# atributy: name, team

print(__name__, '<<<<<<<<<<<<<<<<<<<<<<<<<<<')

if __name__ == '__main__':
    it_security = Company('IT Guards s.r.o.')

    team_A = Team('Team A', it_security)
    team_B = Team('Team B', it_security)

    lena = Employee('Lena')
    petr = Employee('Petr')

    print(petr.team)
    print(team_A.members)

    team_A.add_member(petr)
    print(petr.team)
    print(team_A.members)

    team_A.add_member(lena)
    print(lena.team)
    print(team_A.members)

    team_B.add_member(lena)
    print(lena.team)
    print(team_A.members)
    print(team_B.members)