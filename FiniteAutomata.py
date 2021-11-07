class FiniteAutomata:
    def __init__(self, file_name):
        self._states = []
        self._alphabet = []
        self._initial = None
        self._final = []
        self._transitions = {}
        self.parse_file(file_name)

    def parse_file(self, file_name):
        file = open(file_name, 'r')
        states = file.readline()
        states = states.strip()
        states = states.split(', ')
        self._states = states

        alpha = file.readline()
        alpha = alpha.strip()
        alpha = alpha.split(', ')
        self._alphabet = alpha

        initial = file.readline()
        initial = initial.strip()
        self._initial = initial

        final = file.readline()
        final = final.strip()
        final = final.split(', ')
        self._final = final

        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip()
            line = line.split(', ')
            if not (line[0], line[1]) in self._transitions.keys():
                self._transitions[(line[0], line[1])] = []
            self._transitions[(line[0], line[1])].append(line[2])

    def __str__(self):
        res = ''
        res += 'States ' + str(self._states) + '\n'
        res += 'Alphabet ' + str(self._alphabet) + '\n'
        res += 'Initial state ' + str(self._initial) + '\n'
        res += 'Final states ' + str(self._final) + '\n'
        res += 'Transitions ' + str(self._transitions) + '\n'
        return res

    def is_dfa(self):
        for key in self._transitions.keys():
            if len(self._transitions[key]) > 1:
                return False
        return True

    def verify(self, word):
        if not self.is_dfa():
            return False
        current = self._initial
        for letter in word:
            if (current, letter) in self._transitions.keys():
                current = self._transitions[(current, letter)][0]
            else:
                return False
        return True
