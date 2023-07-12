def lista_cadastros():
    def atualizar_cpf():
        def gravar_alteracao():
            conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados_Cadastrais_DB.db')
            cursor1 = conexao.cursor()
            cursor1.execute(f'''
                update dados_pessoais set
                nome = '{enome_up.get()}',
                cpf = '{et_cpf.get()}',
                telefone = '{etelefone_up.get()}',
                data = '{edata_up.get()}'
                where cpf = '{et_cpf.get()}';
            ''')
            cursor2 = conexao.cursor()
            cursor2.execute(f'''
                update dados_enderecos set
                rua = '{erua_up.get()}',
                numero = '{enumero_up.get()}',
                bairro = '{ebairro_up.get()}',
                cidade = '{ecidade_up.get()}',
                uf = '{euf_up}'
            ''')
            conexao.commit()
            conexao.close()

        

    def deletar_cpf():
        global lb_pessoas
        global lb_enderecos

        conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados_Cadastrais_DB.db')
        cursor1 = conexao.cursor()
        cursor1.execute(f'DELETE FROM dados_pessoais WHERE cpf = "{et_cpf.get()}"')
        cursor2 = conexao.cursor()
        cursor2.execute(f'delete from dados_enderecos where dados_pessoas_cpf = "{et_cpf.get()}"')
        conexao.commit()
        conexao.close()

        lb_deletado = Label(lf_resultado, text='Dados Deletados', anchor='center')
        lb_deletado.grid(row=0, column=0, columnspan=2, sticky='we')
        lb_pessoas.config(text='(' + str(et_cpf.get()) + ') - Dados DELETATOS', anchor='center')
        lb_enderecos.config(text='(' + str(et_cpf.get()) + ') - Dados DELETATOS', justify='center')

        et_cpf.delete(0, 'end')

    def search():
        global lb_deletado
        global lb_pessoas
        global lb_enderecos


        conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados_Cadastrais_DB.db')
        cursor1 = conexao.cursor()
        cursor1.execute(f'select * from dados_pessoais WHERE cpf = "{et_cpf.get()}"')
        dados_pessoas = cursor1.fetchall()
        lb_pessoas = Label(lf_resultado, text='Leitura de Dados', justify='center')
        lb_pessoas.grid(row=1, column=0)
        for dados_pessoa in dados_pessoas:
            lb_pessoas['text'] += '\n' + str(dados_pessoa)

        cursor2 = conexao.cursor()
        cursor2.execute(f'select rua, numero, bairro, cidade, uf from dados_enderecos where dados_pessoas_cpf = "{et_cpf.get()}"')
        dados_enderecos = cursor2.fetchall()
        lb_enderecos = Label(lf_resultado, text='Leitura de Endereços', justify='center')
        lb_enderecos.grid(row=1, column=1)
        for dados_endereco in dados_enderecos:
            lb_enderecos['text'] += '\n' + str(dados_endereco)


    def bc_pessoas():
        conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select * from dados_pessoais')
        dados_pessoas = cursor.fetchall()

        lb_pessoas = Label(lf_pessoas, text='Leitura de Dados', justify='center')
        lb_pessoas.grid(row=1, column=0)

        for dados_pessoa in dados_pessoas:
            lb_pessoas['text'] += '\n' + str(dados_pessoa)
        conexao.close()

    def bc_endereco():
        conexao = sqlite3.connect('Senac-Minas\Banco de Dados\Bancos_Dados\Dados_Cadastrais_DB.db')
        cursor = conexao.cursor()
        cursor.execute('select rua, numero, bairro, cidade, uf from dados_enderecos')
        dados_enderecos = cursor.fetchall()

        lb_endereco = Label(lf_enderecos, text='Leitura de Endereços', justify='center')
        lb_endereco.grid(row=1, column=0)

        for dados_endereco in dados_enderecos:
            lb_endereco['text'] += '\n' + str(dados_endereco)




criar_banco()

janela.mainloop()
