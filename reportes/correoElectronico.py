
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings



class correo:
    def __init__(self) -> None:
        self.html_content = get_template('asilo/NuevaSolicitudMedica.html')
        self.text_content = get_template('email.txt')
        self.contexto = None
        self.from_email = None # destinatario
        self.subject = None # motivo
        self.to = None # para
        
        
    def set_contenidoCorreo(self, destinatario, subject, contexto, to):
        self.from_email = destinatario
        self.subject = subject
        self.to = to
        self.contexto = contexto
        
        
    def enviar(self, contexto):
        texto_plano = self.text_content.render(contexto)
        html_content = self.html_content.render(contexto)
        mensaje = EmailMultiAlternatives(self.subject, texto_plano, self.from_email,self.to)
        mensaje.attach_alternative(html_content, "text/html")
        print("envio ficticio de correo")
        # mensaje.send()
    
    