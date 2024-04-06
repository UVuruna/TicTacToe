from GameLogic.AI_Multiprocessing import BasicM,ImprovedM,SafeM,worker,MultiAnalyze
from GameLogic.AI_Threading import BasicT,ImprovedT,SafeT
from GameLogic.Logic import TicTacToe

# Much FASTER with MORE CALCULATIONS (Recursions)
    # Much SLOWER with LESS CALCULATIONS (Recursions)

# Prazan board 3x3 ; 255,168 resenja (vise od toga radi) ; 986,409 poteza (manje od toga radi)
    # Average 100 repeats Multiprocessing:
        # Improved je:  335.98 ms    vs     THREADING: 931.07 ms
        # Basic je:     322.91 ms    vs     THREADING: 903.51 ms
        # SafeM je:      323.15 ms    vs     THREADING: 910.05 ms

# Preostalo 8 poteza ; 25,872 resenja
    # Average 100 repeats both:
        # Improved je:  195.01 ms    vs     THREADING: 96.44 ms
        # Basic je:     192.81 ms    vs     THREADING: 93.02 ms
        # Safe je:      192.51 ms    vs     THREADING: 92.78 ms

# Preostala 4 poteza ; 21 resenje
    # Average 1,000 repeats Threading
        # Improved je:  161.15 ms    vs     THREADING: 0.63 ms
        # Basic je:     156.86 ms    vs     THREADING: 0.63 ms
        # Safe je:      155.15 ms    vs     THREADING: 0.64 ms