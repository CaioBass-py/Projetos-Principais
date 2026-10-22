import ollama

def iniciar_assistente():
    print("========================================")
    print("  CESAR / JARVIS - Assistente Local Ativo")
    print("  Conectado ao modelo: arquiteto-maquinas")
    print("========================================")
    print("Digite 'sair' ou 'exit' para encerrar.\n")

    # Histórico de mensagens para manter o contexto da conversa
    historico = [
        {
            'role': 'system',
            'content': 'Você é o CESAR, um Arquiteto de Sistemas Embarcados e Desenvolvedor Sênior.'
        }
    ]

    while True:
        try:
            prompt_usuario = input("\nVocê: ").strip()
            
            if prompt_usuario.lower() in ["sair", "exit"]:
                print("\nEncerrando o assistente. Até logo!")
                break
            
            if not prompt_usuario:
                continue

            # Adiciona a pergunta do usuário ao histórico
            historico.append({'role': 'user', 'content': prompt_usuario})

            print("\nCESAR está a pensar...")
            
            # Faz a chamada para o modelo local no Ollama
            resposta = ollama.chat(
                model='arquiteto-maquinas',
                messages=historico
            )

            conteudo_resposta = resposta['message']['content']
            print(f"\nCESAR:\n{conteudo_resposta}")

            # Adiciona a resposta do assistente ao histórico
            historico.append({'role': 'assistant', 'content': conteudo_resposta})

        except KeyboardInterrupt:
            print("\n\nOperação interrompida. Encerrando...")
            break
        except Exception as e:
            print(f"\nOcorreu um erro ao comunicar com o Ollama: {e}")
            print("Certifique-se de que o Ollama está a funcionar na sua máquina.")
            break

if __name__ == "__main__":
    iniciar_assistente()