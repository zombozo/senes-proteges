from datetime import date
from django.test import Client, SimpleTestCase, TestCase
from asilo.models import expediente
from asilo.views import contactoCreateView
from fundacion.models import solicitudCita
from usuarios.models import datosPersonales, empleado, empleadoEspecialidad, usuario


class LoginViewTestCase(TestCase):
    def setUp(self) -> None:
        _usuario = usuario.objects.create_superuser(email='gerson.olivares543@gmail.com', password="qeep.1212")
        _usuario.is_active=True
        _usuario.is_superuser=True 
        _usuario.save()
        return super().setUp()
    def test_LoginView(self):
        response = self.client.login(email='gerson.olivares543@gmail.com', password='qeep.1212')
        self.assertEquals(response, True)
        
class CreateClienteTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = usuario.objects.create_superuser(
            email="gerson.olivares543@gmail.com",
            password="qeep.1212"
        )
        self.client.force_login(self.admin_user)

    def test_CreateDatosPersonales(self):
        # datos_personales = datosPersonales.objects.create(primer_nombre="gerson olivares", primer_apellido="olivares", fecha_nacimiento='1993-12-12', dni='2398744551705')
        response = self.client.post('/datos-personales/', {'primer_nombre':'gerson olivares', 'primer_apellido':'olivares', 'fecha_nacimiento':'1993-12-12', 'dni':'2398744551705'}, follow=True)
        url_esperada = '/contacto/'
        url_redir, status_code = response.redirect_chain[-1]
        url_redir= url_redir.split('/')
        url_esperada +=url_redir[2]+"/" 
        self.assertRedirects(
            response, url_esperada, 
            status_code=302, 
            target_status_code=200,
            fetch_redirect_response=True
            )
        self.assertEqual(response.status_code, 200)
        self.test_CreateContacto(url=url_esperada)
        self.test_verify_exist_expediente(url_redir[2])
        
    def test_CreateContacto(self, url=None):
        if url != None:
            response = self.client.post(
                url, 
                {'nombre':'paola', 'numero_telefono':'36023912', 'correo_electronico':'esposa'},
                follow=True
                )
            # self.assertRedirects(response=response, expected_url='/expediente/', status_code=200, target_status_code=200, fetch_redirect_response=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.resolver_match.func.__name__, contactoCreateView.as_view().__name__)

    def test_verify_exist_expediente(self, id=None):
        if id != None:
            exped = expediente.objects.get(id_expediente=id)
            self.assertEqual(exped.codigo_expediente, "sp-1")



class solicitudCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = usuario.objects.create_superuser(
            email="gerson.olivares543@gmail.com",
            password="qeep.1212"
        )
        self.client.force_login(self.admin_user)
        fecha = date.fromisoformat('1993-12-12')
        
        _usuario = usuario.objects.create_user(
            email='paola.kamps94@gmail.com',
            password='qeep.1212'
        )
        especialidad = empleadoEspecialidad.objects.create(nombre='enfermeria', actividades="atencion a los pacientes")
        datosPer = datosPersonales.objects.create(
            primer_nombre='paola campos', 
            primer_apellido='campos',
            fecha_nacimiento = fecha,
            dni='2398755441705'
            )   
        _empleado = empleado.objects.create(
            id_datos_personales=datosPer,
            id_empleado_especialidad = especialidad,
            empresa="2",
            usuario=_usuario
            )
        _datosPersonales = datosPersonales.objects.create(
            primer_nombre='paola', 
            primer_apellido='porras',
            fecha_nacimiento = fecha,
            dni='2398755441706'
            )   
        exp = expediente.get_expediente(_datosPersonales)
        
    def test_verify_expediente(self):
        _expediente = expediente.objects.get(id_expediente=1)
        self.assertEquals(_expediente.codigo_expediente, 'sp-1')
        
        
    def test_get_viewCreateSolicitud(self):
        pass
        
        
    def test_createSolicitud(self):

        response = self.client.post(
            '/crear-solicitud/1/', {
                'id_expediente': 1,
                'id_enfermero': 1,
                'descripcion':'paciente grave'
            },
            follow=True
        )
        if response.exc_info != None:
            print("encontrado trace de error")
            print(response.ex_info)
        if response.redirect_chain:
            print(f"redirect a {response.redirect_chain}")
        else:
            print(f"contenido de la respuesta {response.content}")
        self.assertEquals(response.status_code, 200)
        _solicitudCita = solicitudCita.objects.all()
        self.assertEquals(len(_solicitudCita),  1)