from tree import BinaryTree

class ParkingManagement:
    def __init__(self):
        self._bTree = BinaryTree()
        self._totalVacancies = 100
        self._motorcycleVacancies = int(self._totalVacancies * 0.25)
        self._bigCarVacancies = int(self._totalVacancies * 0.25)
        self._commonCarVacancies = int(self._totalVacancies * 0.5)

    def numeratingVacancies(self):
        for i in range(self._motorcycleVacancies):
            self._bTree.insert('M' + str(i + 1), True)

        for i in range(self._bigCarVacancies):
            self._bTree.insert('G' + str(i + 1), True)

        for i in range(self._commonCarVacancies):
            self._bTree.insert('C' + str(i + 1), True)

    def showVacancies(self):
        self._bTree.print_binary_tree()

if __name__ == '__main__':
    parkingManagement = ParkingManagement()
    parkingManagement.numeratingVacancies()
    parkingManagement.showVacancies()