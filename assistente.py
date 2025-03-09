print('Olá, eu sou a sua assistente, Pythrina. O que você quer fazer hoje?')

while True:
    comando = input('>>> ')

    match comando:
        case 'oi' | 'olá':
            print('Oi, como vai você?')
        case 'tchau' | 'sair' | 'fim' | 'exit':
            print('Tchau, foi bom conversar com você!')
            break
        case 'piada':
            print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
        case 'clima' | 'previsão do tempo':
            print('Tá muuuuuuuito quente!! Deve ter passado de 40°C! 🥵')
        case _:
            print('Desculpe, não entendi o comando.')