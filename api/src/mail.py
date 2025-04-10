import markdown
from weasyprint import HTML
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from io import BytesIO


class MarkdownConverter:
    """Classe responsável pela conversão de Markdown para outros formatos."""
    
    @staticmethod
    def md_to_html(texto_md):
        """Converte texto Markdown para HTML."""
        return markdown.markdown(texto_md, extensions=['extra', 'codehilite'])
    
    @staticmethod
    def add_html_style(html_content):
        """Adiciona estilos CSS ao conteúdo HTML."""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 2em;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #333;
                    margin-top: 1.5em;
                    margin-bottom: 0.5em;
                }}
                h1 {{
                    font-size: 2em;
                    border-bottom: 1px solid #ddd;
                    padding-bottom: 0.3em;
                }}
                h2 {{
                    font-size: 1.5em;
                    border-bottom: 1px solid #eee;
                    padding-bottom: 0.3em;
                }}
                code {{
                    background-color: #f6f8fa;
                    padding: 0.2em 0.4em;
                    border-radius: 3px;
                    font-family: monospace;
                }}
                pre {{
                    background-color: #f6f8fa;
                    padding: 1em;
                    border-radius: 3px;
                    overflow: auto;
                }}
                blockquote {{
                    border-left: 4px solid #ddd;
                    padding-left: 1em;
                    color: #666;
                    margin-left: 0;
                }}
                img {{
                    max-width: 100%;
                }}
                a {{
                    color: #0366d6;
                    text-decoration: none;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin-bottom: 1em;
                }}
                table, th, td {{
                    border: 1px solid #ddd;
                }}
                th, td {{
                    padding: 0.5em;
                    text-align: left;
                }}
                th {{
                    background-color: #f6f8fa;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
    
    @staticmethod
    def html_to_pdf_buffer(html_content):
        """Converte HTML em um buffer PDF em memória."""
        pdf_buffer = BytesIO()
        HTML(string=html_content).write_pdf(pdf_buffer)
        pdf_buffer.seek(0)  # Voltar ao início do buffer
        return pdf_buffer


class EmailSender:
    """Classe responsável pelo envio de emails."""
    
    def __init__(self, servidor_smtp="smtp.privateemail.com", porta_smtp=587):
        """Inicializa o serviço de email com configurações padrão."""
        self.servidor_smtp = servidor_smtp
        self.porta_smtp = porta_smtp
    
    def criar_mensagem(self, remetente, destinatario, assunto, corpo):
        """Cria a estrutura básica da mensagem de email."""
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo))
        return msg
    
    def anexar_pdf(self, mensagem, pdf_buffer, nome_arquivo):
        """Anexa um buffer PDF à mensagem de email."""
        pdf_attachment = MIMEApplication(pdf_buffer.read(), _subtype='pdf')
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')
        mensagem.attach(pdf_attachment)
        return mensagem
    
    def enviar(self, mensagem, email_remetente, senha_remetente):
        """Envia a mensagem de email usando as credenciais fornecidas."""
        try:
            with smtplib.SMTP(self.servidor_smtp, self.porta_smtp) as server:
                server.starttls()  # Ativar segurança
                server.login(email_remetente, senha_remetente)
                server.send_message(mensagem)
            return True
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
            return False


def converter_md_para_pdf_e_enviar_email(texto_md, email_destinatario, 
                                         assunto="Arquivo PDF convertido", 
                                         mensagem="Segue o arquivo PDF que foi convertido do Markdown.",
                                         nome_arquivo="documento.pdf",
                                         email_remetente=None, senha_remetente=None,
                                         servidor_smtp="smtp.privateemail.com", porta_smtp=587):
    """
    Converte texto Markdown para PDF e envia por email sem salvar em disco.
    
    Args:
        texto_md (str): Texto em formato Markdown para conversão.
        email_destinatario (str): Email do destinatário.
        assunto (str, opcional): Assunto do email.
        mensagem (str, opcional): Corpo do email.
        nome_arquivo (str, opcional): Nome do arquivo PDF anexado.
        email_remetente (str, opcional): Email do remetente.
        senha_remetente (str, opcional): Senha do email do remetente.
        servidor_smtp (str, opcional): Servidor SMTP para envio. Padrão: smtp.privateemail.com
        porta_smtp (int, opcional): Porta do servidor SMTP. Padrão: 587
    
    Returns:
        bool: True se o email foi enviado com sucesso, False caso contrário.
    """
    # Verificar se as credenciais foram fornecidas
    if email_remetente is None or senha_remetente is None:
        raise ValueError("Email e senha do remetente são obrigatórios.")
    
    try:
        # Instanciar conversor e serviço de email
        conversor = MarkdownConverter()
        email_service = EmailSender(servidor_smtp, porta_smtp)
        
        # Etapa 1: Converter Markdown para HTML com estilo
        html_basico = conversor.md_to_html(texto_md)
        html_completo = conversor.add_html_style(html_basico)
        
        # Etapa 2: Converter HTML para PDF em memória
        pdf_buffer = conversor.html_to_pdf_buffer(html_completo)
        
        # Etapa 3: Criar mensagem de email
        msg = email_service.criar_mensagem(
            remetente=email_remetente,
            destinatario=email_destinatario,
            assunto=assunto,
            corpo=mensagem
        )
        
        # Etapa 4: Anexar PDF à mensagem
        msg = email_service.anexar_pdf(msg, pdf_buffer, nome_arquivo)
        
        # Etapa 5: Enviar email
        resultado = email_service.enviar(msg, email_remetente, senha_remetente)
        
        if resultado:
            print(f"Email enviado com sucesso para {email_destinatario}")
        return resultado
        
    except Exception as e:
        print(f"Erro no processo: {e}")
        return False


# Exemplo de uso
if __name__ == "__main__":
    markdown_texto = """
    # Título de Exemplo
    
    Este é um exemplo de **Markdown** que será convertido para PDF.
    
    - Item 1
    - Item 2
    - Item 3
    
    > Uma citação de exemplo
    
    ```python
    def hello_world():
        print("Hello, World!")
    ```
    """

    converter_md_para_pdf_e_enviar_email(
        texto_md=markdown_texto,
        email_destinatario="contato@natanascimento.com",
        email_remetente="noreply@mytriply.io",
        senha_remetente="^KuQ2JWCR;E!*e#"
    )