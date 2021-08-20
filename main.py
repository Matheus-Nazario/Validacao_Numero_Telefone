# -------------------------------------------------------------
# Main REGEX TELEFONES
# ---------------------------------------------------------

from TelefonesBr import TelefonesBr

telefone = input(
    "Digite o número do seu celular com DDD e o código do seu país: "
)

telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)
