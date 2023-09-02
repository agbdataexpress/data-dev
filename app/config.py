class config():
    SECRET_KEY = 'secretkey'
    GOOGLE_CREDENTIALS_PATH = "/ruta/hacia/tu/archivo/credenciales.json"

class DevCofig(config):
    DEBUG = True
    
class ProdConfig():
    DEBUG = False
    
config = {
    'dev': DevCofig,
}