import sys
sys.path.append('/p/home/lnichols/multiphonon-capture/')
from Modules.tools import SjCalculator

def main():
    initial_file = '/p/work/lnichols/SiVH3/GaNPaper/neutToNeg/initialChargeState/PBE/CONTCAR'
    final_file = '/p/work/lnichols/SiVH3/GaNPaper/neutToNeg/finalChargeState/finalPositions/CONTCAR'
    phonon_file = '/p/work/lnichols/SiVH3/GaNPaper/Phonons/4x4x4/mesh.yaml'
    
    calc = SjCalculator(initial_file, final_file, phonon_file)
    calc.write('Sj.out')
    
if __name__ == '__main__':
    main()
