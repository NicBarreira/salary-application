import tkinter as tk
from tkinter import messagebox

def verificar_aumento():
    try:
        salario = float(entry_salario.get())
        aumento_desejado = float(entry_aumento.get())

        if aumento_desejado > 15:
            messagebox.showinfo('Resultado', 'Não será possível conceder um aumento maior que 15%.')
        else:
            novo_salario = salario + (salario * aumento_desejado / 100)
            messagebox.showinfo('Resultado', f'Novo salário será: R${novo_salario:.2f}')
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira valores válidos.')

# Criando a janela principal
root = tk.Tk()
root.title('Calculadora de Aumento de Salário')

# Criando os rótulos e entradas
label_salario = tk.Label(root, text='Qual seu salário atual?')
label_salario.pack()

entry_salario = tk.Entry(root)
entry_salario.pack()

label_aumento = tk.Label(root, text='Qual aumento desejado (em porcentagem)?')
label_aumento.pack()

entry_aumento = tk.Entry(root)
entry_aumento.pack()

# Botão para verificar o aumento
button_calcular = tk.Button(root, text='Calcular Novo Salário', command=verificar_aumento)
button_calcular.pack()

# Iniciar o loop da interface
root.mainloop()

