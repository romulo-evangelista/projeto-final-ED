from tree import BinaryTree, Vacancy

class ParkingManagement:
    def __init__(self):
        self._bTree = BinaryTree()
        self._total_vacancies = 20
        self._motorcycle_vacancies = int(self._total_vacancies * 0.25)
        self._big_car_vacancies = int(self._total_vacancies * 0.25)
        self._common_car_vacancies = int(self._total_vacancies * 0.5)
        self._lost_motorcycle_customers_count = 0
        self._lost_big_car_customers_count = 0
        self._lost_common_car_customers_count = 0

    def numerating_vacancies(self):
        for i in range(self._motorcycle_vacancies):
            self._bTree.insert('M', i + 1, True)

        for i in range(self._big_car_vacancies):
            self._bTree.insert('G', i + 1, True)

        for i in range(self._common_car_vacancies):
            self._bTree.insert('C', i + 1, True)

    def show_available_vacancies(self):
        print("Vagas de moto: " + str(len(self._bTree.traversal_vacancies(True, False, False)[0])))
        print("Vagas de carro grande: " + str(len(self._bTree.traversal_vacancies(False, True, False)[1])))
        print("Vagas de carro comum: " + str(len(self._bTree.traversal_vacancies(False, False, True)[2])))
        print("\n")

    def show_vacancies(self):
        self._bTree.print_binary_tree()

    def get_vacancy(self, vacancy_type):
        available_vacancy = None

        if vacancy_type == 'M':
            if len(self._bTree.traversal_vacancies(True, False, False)[0]) > 0:
                available_vacancy = self._bTree.traversal_vacancies(True, False, False)[0][0]
                self._bTree.set_available(self._bTree.traversal_vacancies(True, False, False)[0][0])
            else:
                self._lost_motorcycle_customers_count += 1
                print("Não há mais vagas para motos \n")

        elif vacancy_type == 'G':
            if len(self._bTree.traversal_vacancies(False, True, False)[1]) > 0:
                available_vacancy = self._bTree.traversal_vacancies(False, True, False)[1][0]
                self._bTree.set_available(self._bTree.traversal_vacancies(False, True, False)[1][0])
            else:
                self._lost_big_car_customers_count += 1
                print("Não há mais vagas para carros grandes \n")

        elif vacancy_type == 'C':
            if len(self._bTree.traversal_vacancies(False, False, True)[2]) > 0:
                available_vacancy = self._bTree.traversal_vacancies(False, False, True)[2][0]
                self._bTree.set_available(self._bTree.traversal_vacancies(False, False, True)[2][0])
            else:
                self._lost_common_car_customers_count += 1
                print("Não há mais vagas para carros grandes \n")
        
        return available_vacancy

    def generate_ticket(self, vacancy_type):
        return self.get_vacancy(vacancy_type)

    def free_vacancy(self, vacancy_type, vacancy_number):
        if (len(self._bTree.traversal_vacancies(True, False, False)[0]) < self._motorcycle_vacancies) or (len(self._bTree.traversal_vacancies(False, True, False)[1]) < self._big_car_vacancies) or (len(self._bTree.traversal_vacancies(False, False, True)[2]) < self._common_car_vacancies):
            vacancy = Vacancy(vacancy_type, vacancy_number, False)
            self._bTree.set_available(vacancy)
            print("Vaga " + vacancy_type + str(vacancy_number) + " liberada \n")
        else:
            print("Nenhuma vaga foi liberada")


    def show_lost_customers_count(self):
        lost_customers_count = self._lost_motorcycle_customers_count + self._lost_big_car_customers_count + self._lost_common_car_customers_count
        print("Total de clientes não atendidos: " + str(lost_customers_count))
        print("Moto - clientes não atendidos: " + str(self._lost_motorcycle_customers_count))
        print("Carro grande - clientes não atendidos: " + str(self._lost_big_car_customers_count))
        print("Carro comum - clientes não atendidos: " + str(self._lost_common_car_customers_count))
        print("\n")

def menu(parking_management):
    parking_management.show_available_vacancies()
    print("Escolha uma das opções abaixo:")
    print("1 - estacionar")
    print("2 - sair")
    print("3 - relatório")
    print("9 - encerrar aplicação \n")
    opcao_menu = input()
    return int(opcao_menu)

def submenu():
    print("Qual tipo de veículo?")
    print("a - moto")
    print("b - carro grande")
    print("c - carro comun \n")
    opcao_submenu = input()
    return opcao_submenu

def submenu2():
    print("Digite o número da vaga: \n")
    opcao_submenu2 = input()
    return int(opcao_submenu2)

if __name__ == '__main__':
    parking_management = ParkingManagement()
    parking_management.numerating_vacancies()


    opt = menu(parking_management)

    while opt < 9:
        if opt == 1:
            opt2 = submenu()
            vacancy_type = ''

            if opt2 == 'a':
                vacancy_type = 'M'
            elif opt2 == 'b':
                vacancy_type = 'G'
            elif opt2 == 'c':
                vacancy_type = 'C'

            vacancy = parking_management.generate_ticket(vacancy_type)
            if vacancy != None:
                print("Estacione na vaga: " + vacancy.vacancy_type + str(vacancy.number) + "\n")

        elif opt == 2:
            opt2 = submenu()
            vacancy_type = ''

            if opt2 == 'a':
                vacancy_type = 'M'
            elif opt2 == 'b':
                vacancy_type = 'G'
            elif opt2 == 'c':
                vacancy_type = 'C'
            
            vacancy_number = submenu2()

            print(parking_management.free_vacancy(vacancy_type, vacancy_number))

        elif opt == 3: 
            parking_management.show_lost_customers_count()   

        opt = menu(parking_management)
