
                        processo_a = self.instancia[self.keysdic[i]][j][teste][0]
                        while (processo_a + momento_a > d):  # pego o primeiro disponível para alocar-
                            k = k + 1
                            teste = ordem_p_alfa[k][0]
                            processo_a = self.instancia[self.keysdic[i]][j][teste][0]
                        alfa_a = self.instancia[self.keysdic[i]][j][teste][1]
                        soma_antes = (d - momento_a - processo_a) * alfa_a

                        aux = 0  # auxiliar para varrer a pilha B

                        momento_b = 0  # self.instancia[self.keysdic[i]][j][ordem_p_beta[aux][0]][0]
                        soma_depois = 0
                        while (ordem_p_beta[aux][0] != teste and aux < self.keysdic[
                            i]):  # busco na pilha b o elemento teste da pilha A
                            teste_b = ordem_p_beta[aux][0]  # talvez não precise da segunda parte
                            if aux_instancia[self.keysdic[i]][j][teste_b][3] == -1 or \
                                    aux_instancia[self.keysdic[i]][j][teste_b][3] == 1:
                                # posso alocar no segundo de duas formas-ele existe=1
                                # ou ele ainda não foi inserido em nenhum lugar=-1
                                beta_b = self.instancia[self.keysdic[i]][j][teste_b][2]
                                processo_b = self.instancia[self.keysdic[i]][j][teste_b][0]
                                momento_b = momento_b + processo_b
                                soma_depois = soma_depois + (momento_b) * beta_b
                                # momento vc anda no vetor
                                # soma_depois vc tem a somatoria dos  momentos * seus respectivos betas
                            aux = aux + 1
                        # achou na pilha B
                        # soma o valor na pilha b- vale para se for em 0 ou no final
                        beta_b = self.instancia[self.keysdic[i]][j][teste_b][2]
                        processo_b = self.instancia[self.keysdic[i]][j][teste_b][0]
                        momento_b = momento_b + processo_b
                        soma_depois = soma_depois + (momento_b) * beta_b

                        if soma_antes < soma_depois:
                            grupo_A.append(teste)
                            momento_a += processo_a
                            aux_instancia[self.keysdic[i]][j][teste][3] = 0
                        else:
                            grupo_B.append(teste)
                            momento_b += processo_b
                            aux_instancia[self.keysdic[i]][j][teste][3] = 1

                        foitudoo = 1
                        # verificação se ainda tem gente que não está inserido no fluxo- ei
                        for zz in range(self.keysdic[i]):
                            if (aux_instancia[self.keysdic[i]][j][zz][3] == -1):
                                if (aux_instancia[self.keysdic[i]][j][zz][
                                    0]) + momento_a <= d:  # se ainda da pra encaixar alguem nessa seleção
                                    foitudoo = 0
                                    break
                        k += 1

                        # aqui adiciona quem sobrou no final do vetor
                        for k in range(self.keysdic[i]):
                            teste_b = ordem_p_beta[k][0]
                            if (aux_instancia[self.keysdic[i]][j][teste_b][3] == -1):
                                grupo_B.append(teste_b)
                                aux_instancia[self.keysdic[i]][j][teste_b][3] = 1
                        # soma=self.soma_valores_grupo_a(self.instancia[self.keysdic[i]][j], grupo_A,d)+self.soma_valores_grupo_b( self.instancia[self.keysdic[i]][j],grupo_B) # b começa em D, logo não preciso do D
                        # adicionar todo mundo no vetor solucao geral

                        k = 0
                        ki = 0
                        while k < len(grupo_A):
                            a = grupo_A
                            b = grupo_B
                            self.sol_construtiva[self.keysdic[i]][j][0][sequencia_momento][0][k] = grupo_A[ki]
                            ki += 1
                            k += 1
                        ki = 0
                        while ki < len(grupo_B):
                            self.sol_construtiva[self.keysdic[i]][j][0][sequencia_momento][0][k] = grupo_B[ki]
                            k += 1
                            ki += 1
                        # adiciona a soma
                        self.sol_construtiva[self.keysdic[i]][j][0][titulo_sequencia_momento][
                            0] = self.soma_valores_grupo(self.instancia[self.keysdic[i]][j],
                                                         self.sol_construtiva[self.keysdic[i]][j][0][sequencia_momento][
                                                             0], d)
                        xa = self.sol_construtiva[self.keysdic[i]][j][0][titulo_sequencia_momento][0]
                        xb = self.refs[valor_titulo_sequencia_momento][self.keysdic[i]][j + 1]

                        fracao = (xa - xb) / xb
                        self.sol_construtiva_comparativa[self.keysdic[i]][j][0][titulo_sequencia_momento][0] = fracao
                        soma_grupo += fracao
