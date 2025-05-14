from pyknow import *

class Sintomas(Fact):
    """Representa todos los síntomas (booleanos) usados por el sistema experto."""
    dificultad_respirar = Field(bool, mandatory=False)
    dolor_pecho = Field(bool, mandatory=False)
    dolor_brazo_izquierdo = Field(bool, mandatory=False)
    dolor_esfuerzo = Field(bool, mandatory=False)
    tos_persistente = Field(bool, mandatory=False)
    tos = Field(bool, mandatory=False)
    tos_seca = Field(bool, mandatory=False)
    tos_flema = Field(bool, mandatory=False)
    tos_sangre = Field(bool, mandatory=False)
    fiebre = Field(bool, mandatory=False)
    escalofrios = Field(bool, mandatory=False)
    fiebre_prolongada = Field(bool, mandatory=False)
    sudor_escalofrios = Field(bool, mandatory=False)
    fatiga = Field(bool, mandatory=False)
    mareo_debilidad = Field(bool, mandatory=False)
    palpitaciones_irregulares = Field(bool, mandatory=False)
    latidos_irregulares = Field(bool, mandatory=False)
    presion_alta = Field(bool, mandatory=False)
    sudoracion_nocturna = Field(bool, mandatory=False)
    sudoracion_excesiva = Field(bool, mandatory=False)
    temblores = Field(bool, mandatory=False)
    temblores_hambre = Field(bool, mandatory=False)
    ansiedad_estres = Field(bool, mandatory=False)
    estres = Field(bool, mandatory=False)
    dolor_cabeza = Field(bool, mandatory=False)
    nausea = Field(bool, mandatory=False)
    nausea_vomito = Field(bool, mandatory=False)
    sensibilidad_luz = Field(bool, mandatory=False)
    sensibilidad_luz_ruido = Field(bool, mandatory=False)
    rigidez_cuello = Field(bool, mandatory=False)
    convulsiones = Field(bool, mandatory=False)
    brotes_piel = Field(bool, mandatory=False)
    dolor_muscular = Field(bool, mandatory=False)
    dolor_muscular_intenso = Field(bool, mandatory=False)
    inflamacion = Field(bool, mandatory=False)
    dolor_abdominal = Field(bool, mandatory=False)
    dolor_abdominal_insoportable = Field(bool, mandatory=False)
    acidez_ardor = Field(bool, mandatory=False)
    ardor_boca_estomago = Field(bool, mandatory=False)
    lado_derecho_abdomen = Field(bool, mandatory=False)
    dolor_bajo_abdomen = Field(bool, mandatory=False)
    fiebre_dolor_baja = Field(bool, mandatory=False)
    dolor_lumbar = Field(bool, mandatory=False)
    dolor_insoportable = Field(bool, mandatory=False)
    fiebre_ardor = Field(bool, mandatory=False)
    perdida_conciencia = Field(bool, mandatory=False)
    fue_repentino = Field(bool, mandatory=False)
    antes_dolor_pecho = Field(bool, mandatory=False)
    dolor_pecho_antes = Field(bool, mandatory=False)
    dolor_pecho_repite = Field(bool, mandatory=False)
    sudor_ansiedad_antes = Field(bool, mandatory=False)
    sudor_vision_confusion = Field(bool, mandatory=False)
    parte_baja_espalda = Field(bool, mandatory=False)
    orina_sangre = Field(bool, mandatory=False)
    vision_borrosa = Field(bool, mandatory=False)
    dificultad_hablar = Field(bool, mandatory=False)
    golpe_cabeza = Field(bool, mandatory=False)
    conmocion = Field(bool, mandatory=False)
    accidente_golpe = Field(bool, mandatory=False)
    herida_abierta = Field(bool, mandatory=False)
    sangrado_profun = Field(bool, mandatory=False)
    signos_infeccion = Field(bool, mandatory=False)
    hinchada_anormal = Field(bool, mandatory=False)
    estructura_osea_expuesta = Field(bool, mandatory=False)
    mover_extremidad = Field(bool, mandatory=False)

class DiagnosticoMedico(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultado = "Sin diagnóstico"
        
    #
    # 1) RUTAS BASADAS EN "Dificultad para respirar"
    #
    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=True))
    def preinfarto(self):
        self.resultado = "Pre-infarto"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=False,
                   dolor_esfuerzo=True))
    def insuficiencia_cardiaca_esfuerzo(self):
        self.resultado = "Insuficiencia cardíaca"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=False,
                   dolor_esfuerzo=False,
                   tos_persistente=True,
                   fiebre=False))
    def bronquitis(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=False,
                   dolor_esfuerzo=False,
                   tos_persistente=True,
                   fiebre=True))
    def neumonia(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=False,
                   dolor_esfuerzo=False,
                   tos_persistente=False,
                   latidos_irregulares=False))
    def asma(self):
        self.resultado = "Asma"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=True,
                   dolor_brazo_izquierdo=False,
                   dolor_esfuerzo=False,
                   tos_persistente=False,
                   latidos_irregulares=True))
    def arritmia(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=True,
                   hinchazon_extremidades=True,
                   sudoracion_nocturna=True,
                   tos_persistente=False))
    def neumonia_v2(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=True,
                   hinchazon_extremidades=True,
                   sudoracion_nocturna=True,
                   tos_persistente=True))
    def tuberculosis(self):
        self.resultado = "Tuberculosis"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=True,
                   hinchazon_extremidades=True,
                   sudoracion_nocturna=False,
                   ansiedad_estres=False))
    def asma_v2(self):
        self.resultado = "Asma"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=True,
                   hinchazon_extremidades=True,
                   sudoracion_nocturna=False,
                   ansiedad_estres=True))
    def ataque_panico(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=True,
                   tos_seca=True))
    def asma_v3(self):
        self.resultado = "Asma"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=True,
                   tos_seca=False,
                   tos_flema=True,
                   fiebre=False))
    def bronquitis_v2(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=True,
                   tos_seca=False,
                   tos_flema=True,
                   fiebre=True))
    def neumonia_v3(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=True,
                   tos_seca=False,
                   tos_flema=False,
                   tos_sangre=True))
    def tuberculosis_v2(self):
        self.resultado = "Tuberculosis"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=True,
                   tos_seca=False,
                   tos_flema=False,
                   tos_sangre=False))
    def insuficiencia_cardiaca_v2(self):
        self.resultado = "Insuficiencia cardíaca"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=False,
                   mareo_debilidad=True,
                   presion_alta=True))
    def hipertension(self):
        self.resultado = "Hipertensión arterial"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=False,
                   mareo_debilidad=True,
                   presion_alta=False,
                   palpitaciones_irregulares=True))
    def arritmia_v2(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=False,
                   mareo_debilidad=True,
                   presion_alta=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=True,
                   temblores=False))
    def ataque_panico_v2(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(dificultad_respirar=True,
                   dolor_pecho=False,
                   fatiga=False,
                   tos=False,
                   mareo_debilidad=True,
                   presion_alta=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=False))
    def bajon_azucar(self):
        self.resultado = "Bajón de azúcar"

    #
    # 2) RUTAS BASADAS EN "Fiebre"
    #
    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=True,
                   dificultad_respirar=True,
                   dolor_pecho=True,
                   escalofrios=True))
    def neumonia_f1(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=True,
                   dificultad_respirar=True,
                   dolor_pecho=True,
                   escalofrios=False))
    def bronquitis_f1(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=True,
                   dificultad_respirar=True,
                   dolor_pecho=False))
    def asma_f1(self):
        self.resultado = "Asma"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=True,
                   flema_amarilla_verde=True,
                   fiebre_prolongada=True))
    def neumonia_f2(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=True,
                   flema_amarilla_verde=True,
                   fiebre_prolongada=False))
    def bronquitis_f2(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=True,
                   flema_amarilla_verde=False))
    def gripe_influenza_f(self):
        self.resultado = "Gripe o Influenza"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=False,
                   tos_sangre=True,
                   perdida_peso=True))
    def tuberculosis_f1(self):
        self.resultado = "Tuberculosis"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=False,
                   tos_sangre=True,
                   perdida_peso=False,
                   escalofrios=True))
    def neumonia_f3(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=False,
                   tos_sangre=True,
                   perdida_peso=False,
                   escalofrios=False,
                   dolor_toser=True))
    def infeccion_pulmonar_f(self):
        self.resultado = "Infección pulmonar severa"

    @Rule(Sintomas(fiebre=True,
                   tos=True, tos_seca=False,
                   tos_flema=False,
                   tos_sangre=True,
                   perdida_peso=False,
                   escalofrios=False,
                   dolor_toser=False))
    def bronquitis_f3(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=True,
                   nausea=True,
                   sensibilidad_luz=True))
    def migraña_f(self):
        self.resultado = "Migraña"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=True,
                   nausea=True,
                   sensibilidad_luz=False,
                   rigidez_cuello=True))
    def meningitis_f1(self):
        self.resultado = "Meningitis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=True,
                   nausea=False,
                   brotes_piel=True))
    def dengue_f1(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=True,
                   nausea=False,
                   brotes_piel=False,
                   convulsiones=True))
    def meningitis_f2(self):
        self.resultado = "Meningitis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_bajo_abdomen=True))
    def infeccion_urinaria_f(self):
        self.resultado = "Infección urinaria"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_bajo_abdomen=False))
    def influenza_f2(self):
        self.resultado = "Influenza"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=True,
                   brotes_piel=True,
                   inflamacion=True))
    def dengue_f2(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=True,
                   brotes_piel=True,
                   inflamacion=False))
    def alergia_f(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=True,
                   brotes_piel=False,
                   dificultad_respirar=True))
    def bronquitis_f4(self):
        self.resultado = "Bronquitis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=True,
                   brotes_piel=False,
                   dificultad_respirar=False,
                   ardor_boca_estomago=True))
    def gastritis_f(self):
        self.resultado = "Gastritis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=True,
                   brotes_piel=False,
                   dificultad_respirar=False,
                   ardor_boca_estomago=False))
    def influenza_f3(self):
        self.resultado = "Influenza"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=True,
                   tos_persistente=True,
                   tos_sangre=True))
    def tuberculosis_f2(self):
        self.resultado = "Tuberculosis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=True,
                   tos_persistente=True,
                   tos_sangre=False))
    def neumonia_f4(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=True,
                   tos_persistente=False,
                   sudor_escalofrios=True))
    def neumonia_f5(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=True,
                   tos_persistente=False,
                   sudor_escalofrios=False))
    def influenza_f4(self):
        self.resultado = "Influenza"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=True,
                   tos_sangre=True))
    def tuberculosis_f3(self):
        self.resultado = "Tuberculosis"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=True,
                   tos_sangre=False))
    def neumonia_f6(self):
        self.resultado = "Neumonía"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=False,
                   dolor_muscular_intenso=True,
                   brotes_piel=True,
                   inflamacion=True))
    def dengue_f3(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=False,
                   dolor_muscular_intenso=True,
                   brotes_piel=True,
                   inflamacion=False))
    def alergia_f2(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=False,
                   dolor_muscular_intenso=False,
                   dificultad_respirar=True,
                   hinchazon_extremidades=True))
    def insuficiencia_cardiaca_f(self):
        self.resultado = "Insuficiencia cardíaca"

    @Rule(Sintomas(fiebre=True,
                   tos=False,
                   dolor_cabeza=False,
                   dolor_muscular=False,
                   sudoracion_excesiva=False,
                   fatiga=True,
                   tos_persistente=False,
                   dolor_muscular_intenso=False,
                   dificultad_respirar=False,
                   hinchazon_extremidades=False))
    def influenza_f5(self):
        self.resultado = "Influenza"

    #
    # 3) RUTAS BASADAS EN "Dolor de pecho"
    #
    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=True,
                   dolor_brazo_izquierdo=True))
    def preinfarto_dp(self):
        self.resultado = "Pre-infarto"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=True,
                   dolor_brazo_izquierdo=False,
                   palpitaciones_irregulares=True))
    def arritmia_dp(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=True,
                   dolor_brazo_izquierdo=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=True))
    def panico_dp(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=True,
                   dolor_brazo_izquierdo=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=False,
                   temblores=False))
    def hipertension_dp(self):
        self.resultado = "Hipertensión arterial"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=False,
                   nausea=True,
                   dolor_pecho_insoportable=True))
    def preinfarto_dp2(self):
        self.resultado = "Pre-infarto"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=False,
                   nausea=True,
                   dolor_pecho_insoportable=False,
                   reflujo=True))
    def gastritis_dp(self):
        self.resultado = "Gastritis"

    @Rule(Sintomas(dolor_pecho=True,
                   mareo_debilidad=False,
                   nausea=True,
                   dolor_pecho_insoportable=False,
                   reflujo=False))
    def hipertension_dp2(self):
        self.resultado = "Hipertensión arterial"

    #
    # 4) RUTAS BASADAS EN "Dolor abdominal"
    #
    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=True,
                   acidez_ardor=True))
    def gastritis_da(self):
        self.resultado = "Gastritis"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=True,
                   acidez_ardor=False,
                   lado_derecho_abdomen=True))
    def apendicitis_da(self):
        self.resultado = "Apendicitis"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=True,
                   acidez_ardor=False,
                   lado_derecho_abdomen=False,
                   fiebre_dolor_baja=False))
    def colicos_renales_da(self):
        self.resultado = "Cólicos renales"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=True,
                   acidez_ardor=False,
                   lado_derecho_abdomen=False,
                   fiebre_dolor_baja=True))
    def infeccion_urinaria_da(self):
        self.resultado = "Infección urinaria"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=False,
                   dolor_lumbar=True,
                   dolor_insoportable=True))
    def colicos_renales_da2(self):
        self.resultado = "Cólicos renales"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=False,
                   dolor_lumbar=True,
                   dolor_insoportable=False,
                   fiebre_ardor=False))
    def evaluacion_da(self):
        self.resultado = "Necesita evaluación (no enfermedad clara)"

    @Rule(Sintomas(dolor_abdominal=True,
                   nausea=False,
                   dolor_lumbar=True,
                   dolor_insoportable=False,
                   fiebre_ardor=True))
    def infeccion_urinaria_da2(self):
        self.resultado = "Infección urinaria"

    #
    # 5) RUTAS BASADAS EN "Mareo o debilidad"
    #
    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=True,
                   dolor_insoportable=True))
    def preinfarto_md(self):
        self.resultado = "Pre-infarto"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=True,
                   dolor_insoportable=False,
                   palpitaciones_irregulares=True))
    def arritmia_md(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=True,
                   dolor_insoportable=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=True))
    def panico_md(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=True,
                   dolor_insoportable=False,
                   palpitaciones_irregulares=False,
                   sudoracion_excesiva=False,
                   temblores=False))
    def hipertension_md(self):
        self.resultado = "Hipertensión arterial"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=False,
                   perdida_conciencia=True,
                   fue_repentino=True))
    def arritmia_md2(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=False,
                   perdida_conciencia=True,
                   fue_repentino=False,
                   antes_dolor_pecho=True))
    def preinfarto_md2(self):
        self.resultado = "Pre-infarto"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=False,
                   perdida_conciencia=True,
                   fue_repentino=False,
                   antes_dolor_pecho=False,
                   estres=True))
    def panico_md2(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=False,
                   perdida_conciencia=True,
                   fue_repentino=False,
                   antes_dolor_pecho=False,
                   estres=False,
                   sudoracion_excesiva=False))
    def hipertension_md2(self):
        self.resultado = "Hipertensión arterial"

    @Rule(Sintomas(mareo_debilidad=True,
                   dolor_pecho=False,
                   perdida_conciencia=False,
                   sudoracion_excesiva=False))
    def hipertension_md3(self):
        self.resultado = "Hipertensión arterial"

    #
    # 6) RUTAS BASADAS EN "Náuseas o vómito"
    #
    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=True,
                   dolor_abdominal_insoportable=True))
    def apendicitis_nv(self):
        self.resultado = "Apendicitis"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=True,
                   dolor_abdominal_insoportable=False,
                   acidez_ardor=True))
    def gastritis_nv(self):
        self.resultado = "Gastritis"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=True,
                   dolor_abdominal_insoportable=False,
                   acidez_ardor=False,
                   orina_sangre=True,
                   parte_baja_espalda=False))
    def infeccion_urinaria_nv(self):
        self.resultado = "Infección urinaria"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=True,
                   dolor_abdominal_insoportable=False,
                   acidez_ardor=False,
                   orina_sangre=True,
                   parte_baja_espalda=True))
    def colicos_renales_nv(self):
        self.resultado = "Cólico renal"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=True,
                   dolor_abdominal_insoportable=False,
                   acidez_ardor=False,
                   orina_sangre=False))
    def digestivo_nv(self):
        self.resultado = "Problema digestivo / requiere exámenes"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=True))
    def migraña_nv(self):
        self.resultado = "Migraña"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=True))
    def meningitis_nv(self):
        self.resultado = "Meningitis"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=True))
    def conmocion_nv(self):
        self.resultado = "Conmoción cerebral / vigilancia 24h"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=True,
                   dificultad_hablar=False))
    def hipertension_nv(self):
        self.resultado = "Hipertensión arterial"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=True,
                   dificultad_hablar=True))
    def ictus_nv(self):
        self.resultado = "Accidente cerebrovascular"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=False,
                   mareo_debilidad=True,
                   sudoracion_temblores=True))
    def bajon_azucar_nv(self):
        self.resultado = "Bajón de azúcar"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=False,
                   mareo_debilidad=True,
                   sudoracion_temblores=False,
                   sol_calor=True))
    def golpe_calor_nv(self):
        self.resultado = "Golpe de calor"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=False,
                   mareo_debilidad=True,
                   sudoracion_temblores=False,
                   sol_calor=False,
                   sustancia_toxica=False))
    def migraña_nv2(self):
        self.resultado = "Migraña"

    @Rule(Sintomas(nausea_vomito=True,
                   dolor_abdominal=False,
                   dolor_cabeza=True,
                   sensibilidad_luz_ruido=False,
                   fiebre_rigidez_cuello=False,
                   golpe_cabeza=False,
                   vision_borrosa=False,
                   mareo_debilidad=True,
                   sudoracion_temblores=False,
                   sol_calor=False,
                   sustancia_toxica=True))
    def intoxicacion_nv(self):
        self.resultado = "Intoxicación"

    #
    # 7) RUTAS BASADAS EN "Pérdida de conciencia"
    #
    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=True))
    def arritmia_pc(self):
        self.resultado = "Arritmia cardíaca"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=True,
                   dolor_pecho_repite=False))
    def insuf_cardiaca_pc(self):
        self.resultado = "Insuficiencia cardíaca"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=True,
                   dolor_pecho_repite=True))
    def infarto_pc(self):
        self.resultado = "Infarto miocárdico"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=False,
                   sudor_ansiedad_antes=True))
    def panico_pc(self):
        self.resultado = "Ataque de pánico"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=False,
                   sudor_ansiedad_antes=False,
                   sudor_vision_confusion=True,
                   temblores_hambre=True))
    def bajon_azucar_pc(self):
        self.resultado = "Bajón de azúcar"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=False,
                   sudor_ansiedad_antes=False,
                   sudor_vision_confusion=True,
                   temblores_hambre=False,
                   sustancia_exceso=False))
    def insuf_cardiaca_pc2(self):
        self.resultado = "Insuficiencia cardíaca"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=False,
                   sudor_ansiedad_antes=False,
                   sudor_vision_confusion=True,
                   temblores_hambre=False,
                   sustancia_exceso=True))
    def intoxicacion_pc(self):
        self.resultado = "Intoxicación"

    @Rule(Sintomas(perdida_conciencia=True,
                   mareo_debilidad=True,
                   latidos_irregulares=False,
                   dolor_pecho_antes=False,
                   sudor_ansiedad_antes=False,
                   sudor_vision_confusion=False))
    def ictus_pc(self):
        self.resultado = "Accidente cerebrovascular"

    #
    # 8) RUTAS BASADAS EN "Brote en la piel"
    #
    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=True))
    def dengue_bp(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=False))
    def evolucion_bp(self):
        self.resultado = "Revisar evolución por 24h"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=True))
    def alergia_bp(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False,
                   inflamacion=True))
    def alergia_bp2(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False,
                   inflamacion=False))
    def evaluar_bp(self):
        self.resultado = "Evaluar otras decisiones con estos síntomas"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=True))
    def dengue_bp2(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=False))
    def evolucion_bp2(self):
        self.resultado = "Revisar evolución por 24h"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=True))
    def alergia_bp3(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False))
    def evaluar_bp2(self):
        self.resultado = "Evaluar otras decisiones con estos síntomas"

    #
    # 8) RUTAS BASADAS EN "Brote en la piel"
    #
    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=True))
    def dengue_bp(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=False))
    def evolucion_bp(self):
        self.resultado = "Revisar evolución por 24h"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=True))
    def alergia_bp(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False,
                   inflamacion=True))
    def alergia_bp2(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False,
                   inflamacion=False))
    def evaluar_bp(self):
        self.resultado = "Evaluar otras decisiones con estos síntomas"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=True))
    def dengue_bp2(self):
        self.resultado = "Dengue"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=False))
    def evolucion_bp2(self):
        self.resultado = "Revisar evolución por 24h"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=True,
                   tocado_sustancia=True))
    def alergia_bp3(self):
        self.resultado = "Alergia"

    @Rule(Sintomas(brote_piel=True,
                   dolor_muscular=False,
                   nausea=True,
                   fiebre_reciente=False,
                   alergico_sustancia=False))
    def evaluar_bp2(self):
        self.resultado = "Evaluar otras decisiones con estos síntomas"
