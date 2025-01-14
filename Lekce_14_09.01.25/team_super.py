# team_super.py

from team import Company, Team, Employee


class SuperTeam(Team):
    def add_member(self, employee: Employee):
        if type(employee) != SuperEmployee:
            raise TypeError('employee must be instance of Employee')

        # super() se odkazuje na rodičovskou (třída) v tomto případě Team
        super().add_member(employee) # add_member si zavolá z Team

class SuperEmployee(Employee):
    pass

if __name__ == '__main__':
    marvel = Company('Marvel')
    super_team_1 = SuperTeam('Avengers', marvel)
    print(super_team_1)

    suche = Employee('Suche')
    thor = SuperEmployee('Thor')
    # super_team_1.add_member(suche)
    super_team_1.add_member(thor)
    print(thor.team)
    print(super_team_1.members)