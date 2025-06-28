"""
Application for update gold today
MODULARIZATION WITH FUNCTION
MODULARIZATION WITH PACKAGE
"""
import gold_today

if __name__ == '__main__':
    print('Main Application')
    print('\n')
    result = gold_today.data_extraction()
    gold_today.view_data(result)