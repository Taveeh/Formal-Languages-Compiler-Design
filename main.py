from SymbolTable import SymbolTable
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    symbol_table = SymbolTable()
    symbol_table.add('esteban')
    print(symbol_table)
    symbol_table.add('istvan')
    print(symbol_table)
    symbol_table.add('etienne')
    print(symbol_table)
    symbol_table.add('stefan')
    print(symbol_table)
    symbol_table.add('steven')
    print(symbol_table)

    symbol_table.add(2)
    symbol_table.add('2')
    print(symbol_table)
    print("The element \'etienne\' is at position ", symbol_table.get('etienne'))
