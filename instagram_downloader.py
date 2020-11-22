import PySimpleGUI as sg
import instaloader
import webbrowser, os

def descargarDeInstagram(profile):
   L = instaloader.Instaloader()
   posts = instaloader.Profile.from_username(L.context, profile).get_posts()
   #L.download_profilepic(profile)
   for post in posts:
      L.download_post(post, profile)
   sg.Popup('Descarga completa')
   abrirDirectorio(profile)

def interfaz():
   layout = [[sg.Text('Ingresa el perfil de instagram:')],
             [sg.Input()],
             [sg.Button('Buscar', key='buscar')]
            ]
   eventx, valuesx = sg.Window('Descargar de Instagram', layout).Read()
   return eventx, valuesx

def abrirDirectorio(profileDir):
   cwd = os.getcwd()
   directorioDescargado = cwd + '/' + profileDir
   webbrowser.open(os.path.realpath(directorioDescargado))
   
#   sp1 = subprocess.Popen(path, stdout=subprocess.PIPE)


 
while True:
   event, values = interfaz()
   if event is None:
      break
   elif event == 'buscar':
      perfilInstagram = values[0]
      descargarDeInstagram(perfilInstagram)
