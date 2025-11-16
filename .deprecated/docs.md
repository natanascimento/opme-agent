# OPME AI Agent

Com o objetivo de auxiliar o controle eficaz de saídas e uso de OPME (Órteses, Próteses e Materiais Especiais), através de um método de verificação em dois fatores, fundamentado na consulta às diretrizes da portaria do Ministério da Saúde, possibilitando a detecção de valores abusivos e dispensas inadequadas.

# Roadmap

Este roadmap descreve as etapas principais para o desenvolvimento de um serviço de classificação de procedimentos médicos com base na tabela CBHPM.

## Fase 1: Levantamento e Análise

* **Objetivo:** Compreender a estrutura da tabela CBHPM e definir os requisitos iniciais do sistema.
* **Atividades:**
    * Levantamento detalhado dos requisitos funcionais e não funcionais (detalhado na tabela abaixo).
    * Análise aprofundada da estrutura e dos campos da tabela CBHPM.
    * Definição dos formatos de importação da tabela (CSV, Excel).
    * Escolha da estrutura de dados para armazenamento da tabela CBHPM.
* **Entregáveis:**
    * Tabela de requisitos detalhada (abaixo).
    * Modelo inicial da estrutura de dados da CBHPM.
* **Status:** ✅

## Fase 2: Prova de Conceito

* **Objetivo:** Validar a viabilidade da busca e da classificação inicial com base nos dados da CBHPM.
* **Atividades:**
    * Implementação de uma funcionalidade básica de busca na tabela CBHPM por termos.
    * Exibição dos resultados da busca (código e descrição).
    * Avaliação da relevância dos resultados da busca.
* **Entregáveis:**
    * Protótipo funcional da busca na tabela CBHPM.
    * Relatório da avaliação da prova de conceito.
* **Status:** ✅

## Fase 3: Arquitetura e Fluxo de Dados

* **Objetivo:** Definir a arquitetura do sistema e o fluxo de dados entre os componentes.
* **Atividades:**
    * Projeto da arquitetura modular do sistema.
    * Definição das interfaces entre os componentes (serviço de classificação, interface do usuário).
    * Diagrama do fluxo de dados desde a entrada do usuário até a saída da classificação.
    * Escolha das tecnologias a serem utilizadas.
* **Entregáveis:**
    * Documento de arquitetura do sistema.
    * Diagrama de fluxo de dados.
* **Status:** ✅

## Fase 4: Definição do Prompt para o Agente

* **Objetivo:** Criar e otimizar o prompt que guiará o agente de classificação.
* **Atividades:**
    * Elaboração de diferentes versões do prompt.
    * Testes do prompt com diversos exemplos de descrições de procedimentos.
    * Ajustes e refinamento do prompt com base nos resultados dos testes.
* **Entregáveis:**
    * Prompt final para o agente de classificação.
    * Relatório dos testes e otimizações do prompt.
* **Status:** ☐

## Fase 5: Desenvolvimento do Serviço de Classificação

* **Objetivo:** Implementar o serviço principal responsável pela classificação dos procedimentos.
* **Atividades:**
    * Desenvolvimento da lógica do serviço de classificação utilizando o prompt definido.
    * Implementação das APIs para comunicação com outros componentes.
    * Implementação de testes unitários e de integração.
* **Entregáveis:**
    * Serviço de classificação funcional.
    * Documentação da API do serviço de classificação.
    * Relatórios de testes.
* **Status:** ⏳

## Fase 6: Testes e Validação do Serviço de Classificação

* **Objetivo:** Garantir a qualidade e a precisão do serviço de classificação.
* **Atividades:**
    * Execução de testes abrangentes do serviço de classificação.
    * Validação dos resultados da classificação com dados reais.
    * Identificação e correção de bugs e inconsistências.
* **Entregáveis:**
    * Relatório de testes e validação do serviço de classificação.
    * Versão estável do serviço de classificação.
* **Status:** ⏳

## Fase 7: Implementação da Interface Amigável

* **Objetivo:** Desenvolver uma interface de usuário intuitiva para interação com o serviço de classificação.
* **Atividades:**
    * Projeto da interface do usuário.
    * Desenvolvimento da interface web.
    * Implementação das funcionalidades de entrada de texto e exibição de resultados.
    * Garantia da responsividade e acessibilidade da interface.
* **Entregáveis:**
    * Interface do usuário funcional.
    * Documentação da interface do usuário.
* **Status:** ⏳

## Fase 8: Validação da Integração

* **Objetivo:** Assegurar a integração correta e eficiente entre a interface do usuário e o serviço de classificação.
* **Atividades:**
    * Testes da comunicação entre a interface e o serviço.
    * Validação do fluxo completo da entrada do usuário até a exibição da classificação.
    * Otimização da integração para garantir um tempo de resposta adequado.
* **Entregáveis:**
    * Relatório de testes de integração.
    * Sistema integrado e validado.
* **Status:** ☐

---

## Requisitos Detalhados

| Etapa                                                | Tipo          | ID     | Descrição do Requisito                                                                                                                                                                                             | Finalizado |
| :--------------------------------------------------- | :------------ | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------: |
| **Levantamento de requisitos e análise da tabela CBHPM** | Funcional     | RF001  | O sistema deve permitir a importação da tabela CBHPM em formatos como CSV ou Excel.                                                                                                                               |    ✅     |
|                                                      | Funcional     | RF002  | O sistema deve permitir a leitura e o parsing dos dados da tabela CBHPM, identificando seus campos relevantes (código, descrição, porte, etc.).                                                                    |    ✅     |
|                                                      | Funcional     | RF003  | O sistema deve permitir o armazenamento dos dados da tabela CBHPM em uma estrutura de dados adequada para consulta e análise.                                                                                       |    ✅     |
|                                                      | Não Funcional | RNF001 | O processo de importação e análise da tabela CBHPM deve ser concluído em um tempo aceitável (a definir).                                                                                                              |    ✅     |
|                                                      | Não Funcional | RNF002 | O sistema deve garantir a integridade e a precisão dos dados importados da tabela CBHPM.                                                                                                                               |    ✅     |
| **Prova de conceito com base no que foi analisado anteriormente** | Funcional     | RF004  | O sistema deve permitir a entrada de termos ou descrições de procedimentos médicos pelo usuário.                                                                                                               |    ✅     |
|                                                      | Funcional     | RF005  | O sistema deve realizar uma busca nos dados da tabela CBHPM com base nos termos inseridos pelo usuário.                                                                                                                  |    ✅     |
|                                                      | Funcional     | RF006  | O sistema deve exibir os resultados da busca, mostrando os códigos e descrições correspondentes da CBHPM.                                                                                                            |    ✅     |
|                                                      | Não Funcional | RNF003 | A busca deve retornar resultados relevantes em um tempo de resposta rápido (a definir).                                                                                                                               |    ✅     |
|                                                      | Não Funcional | RNF004 | O sistema deve apresentar os resultados de forma clara e organizada.                                                                                                                                                  |    ✅     |
| **Construção da arquitetura e fluxo dos dados** | Funcional     | RF007  | O sistema deve definir uma arquitetura modular que permita a integração de diferentes componentes (serviço de classificação, interface do usuário).                                                                 |    ✅     |
|                                                      | Funcional     | RF008  | O sistema deve definir o fluxo de dados desde a entrada do usuário até a apresentação dos resultados da classificação.                                                                                                 |    ✅     |
|                                                      | Não Funcional | RNF005 | A arquitetura deve ser escalável para suportar um número crescente de usuários e dados.                                                                                                                                |    ✅     |
|                                                      | Não Funcional | RNF006 | A arquitetura deve garantir a segurança dos dados e do sistema.                                                                                                                                                       |    ✅     |
| **Definição do prompt para o agente** | Funcional     | RF009  | O sistema deve permitir a definição e o ajuste do prompt que será utilizado pelo agente de classificação.                                                                                                             |    ☐     |
|                                                      | Funcional     | RF010  | O sistema deve permitir o teste do prompt com diferentes exemplos para avaliar sua eficácia.                                                                                                                             |    ☐     |
|                                                      | Não Funcional | RNF007 | O prompt definido deve ser capaz de gerar classificações precisas e relevantes.                                                                                                                                      |    ☐     |
| **Desenvolvimento do serviço de classificação** | Funcional     | RF011  | O sistema deve implementar um serviço capaz de receber um texto (descrição do procedimento) e retornar o código CBHPM correspondente.                                                                                   |    ✅     |
|                                                      | Funcional     | RF012  | O serviço de classificação deve utilizar o prompt definido para realizar a classificação.                                                                                                                               |    ✅     |
|                                                      | Não Funcional | RNF008 | O serviço de classificação deve ter alta disponibilidade.                                                                                                                                                              |    ⏳     |
|                                                      | Não Funcional | RNF009 | O serviço de classificação deve apresentar baixa latência na resposta.                                                                                                                                                |    ⏳     |
| **Testes e validação do serviço de classificação** | Funcional     | RF013  | O sistema deve permitir a criação e execução de testes unitários para o serviço de classificação.                                                                                                     |    ⏳     |
|                                                      | Funcional     | RF014  | O sistema deve gerar relatórios de testes, indicando a cobertura e os resultados.                                                                                                                                    |    ⏳     |
|                                                      | Não Funcional | RNF010 | O serviço de classificação deve atingir um nível de precisão aceitável (a definir) nos testes.                                                                                                                            |    ⏳     |
| **Implementação de uma interface amigável para usuários finais** | Funcional     | RF015  | O sistema deve apresentar uma interface web intuitiva para os usuários interagirem.                                                                                                                            |    ✅     |
|                                                      | Funcional     | RF016  | A interface deve permitir que os usuários insiram descrições de procedimentos médicos.                                                                                                                                |    ✅     |
|                                                      | Funcional     | RF017  | A interface deve exibir os resultados da classificação de forma clara e organizada.                                                                                                                                   |    ✅     |
|                                                      | Não Funcional | RNF011 | A interface deve ser responsiva e funcionar em diferentes dispositivos (desktops, tablets, smartphones).                                                                                                                   |    ✅     |
|                                                      | Não Funcional | RNF012 | A interface deve ser acessível, seguindo as diretrizes de acessibilidade web (WCAG).                                                                                                                                 |    ⏳     |
| **Validação da integração da interface do usuário com o serviço de classificação** | Funcional     | RF018  | O sistema deve garantir a comunicação correta entre a interface do usuário e o serviço de classificação.                                                                                       |    ✅     |
|                                                      | Funcional     | RF019  | O sistema deve exibir na interface os resultados retornados pelo serviço de classificação.                                                                                                                               |    ☐     |
|                                                      | Não Funcional | RNF013 | A integração entre a interface e o serviço de classificação deve ser estável e confiável.                                                                                                                               |    ☐     |
|                                                      | Não Funcional | RNF014 | O tempo de resposta da integração entre a interface e o serviço de classificação deve ser aceitável para o usuário.                                                                                                    |    ☐     |
