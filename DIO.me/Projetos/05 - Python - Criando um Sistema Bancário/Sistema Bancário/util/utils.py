from pathlib import Path
from datetime import datetime

def realizar_log(func): 

    def envelope(*args, **kwargs):

        ROOT_PATH = Path(__file__).parent.parent
        LOG_PATH = Path(ROOT_PATH / "logs/log.txt")

        resultado = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        try:
            with open(LOG_PATH, "a", encoding="utf-8") as log:
                log.write(
                    f"""->{data_hora}. Função: {func.__name__}.
                    Executada com argumentos {args} e {kwargs}. Retornou: {resultado}\n"""
                )

        except Exception as exc:
            print(f"\nERRO - - -> `{exc}")

        print(
            f"\n- - -> Data da transação: {datetime.now()}, Tipo da transação: {func.__name__.upper()}"
        )
        return resultado

    return envelope


def ler_string(msg: str) -> str:

    while True:
        try:
            str_input = str(input(msg))

            if not str_input or str_input.isspace():
                raise ValueError

            return str_input

        except ValueError:
            print("\nERRO - - -> Input inválido. Por favor, tente novamente!")


def ler_int(msg: str) -> int:

    while True:
        try:
            int_input = int(input(msg))
            return int_input

        except ValueError:
            print("\nERRO - - -> Input inválido. Por favor, tente novamente!")
