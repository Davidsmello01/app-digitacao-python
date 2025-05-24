import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Teste de Janela")
janela.geometry("300x150")

# Texto exibido
rotulo = tk.Label(janela, text="Ambiente Python funcionando!", font=("Arial", 12))
rotulo.pack(pady=20)

# Inicia o loop da janela
janela.mainloop()
