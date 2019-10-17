from EP2_Principal import main

# 1º teste
try: assert(main('2 + 2') == 4.0)
except: print ("Erro no 1º teste")
# 2º teste
try: assert(main('2 - 2') == 0.0)
except: print ("Erro no 2º teste")
# 3º teste
try: assert(main('(-2)*3') == -6)
except: print ("Erro no 3º teste")
# 4º teste
try: assert(main('-2 + 5') == 3.0)
except: print ("Erro no 4º teste")