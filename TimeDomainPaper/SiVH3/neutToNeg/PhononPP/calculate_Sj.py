import sys
sys.path.append('../../../../../multiphonon-capture/')
from Modules.tools import SjCalculator

def main():
    initial_file = 'CONTCAR_initial'
    final_file = 'CONTCAR_final'
    phonon_file = 'mesh.yaml'
    
    calc = SjCalculator(initial_file, final_file, phonon_file)
    calc.write('Sj.out')
    
if __name__ == '__main__':
    main()
