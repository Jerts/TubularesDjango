from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from meta.models import Cargo, Equipos, Miembros, Carreras, Vueltas
from meta.serializers import CargoSerializer, EquiposSerializer, MiembrosSerializer, CarrerasSerializer, VueltasSerializer

# Vistas para CARGOS--------------------------------------------
@api_view(['GET','POST'])
def lista_cargo(request):

    if request.method == 'GET':
        cargos = Cargo.objects.all()
        serializador = CargoSerializer(cargos, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = CargoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def lista_cargo_detail(request, pk):

    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = CargoSerializer(cargo)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = CargoSerializer(cargo, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# VISTAS PARA EQUIPOS--------------------------------------------
@api_view(['GET','POST'])
def lista_equipos(request):

    if request.method == 'GET':
        equipo = Equipos.objects.all()
        serializador = CargoSerializer(equipo, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = EquiposSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def lista_equipos_detail(request, pk):


    try:
        equipo = Equipos.objects.get(pk=pk)
    except Equipos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = EquiposSerializer(equipo)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = EquiposSerializer(equipo, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# VISTAS PARA MIEMBROS--------------------------------------------
@api_view(['GET','POST'])
def lista_miembros(request):

    if request.method == 'GET':
        miembro = Miembros.objects.all()
        serializador = MiembrosSerializer(miembro, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = MiembrosSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def lista_miembros_detail(request, pk):

    try:
        miembro = Miembros.objects.get(pk=pk)
    except Miembros.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = MiembrosSerializer(miembro)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = MiembrosSerializer(miembro, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        miembro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# VISTAS PARA CARRERAS--------------------------------------------
@api_view(['GET','POST'])
def lista_carreras(request):

    if request.method == 'GET':
        carrera = Carreras.objects.all()
        serializador = CarrerasSerializer(carrera, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = CarrerasSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def lista_carreras_detail(request, pk):

    try:
        carrera = Carreras.objects.get(pk=pk)
    except Carreras.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = CarrerasSerializer(carrera)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = CarrerasSerializer(carrera, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        carrera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# VISTAS PARA VUELTAS--------------------------------------------
@api_view(['GET','POST'])
def lista_vueltas(request):

    if request.method == 'GET':
        vuelta = Vueltas.objects.all()
        serializador = VueltasSerializer(vuelta, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        carrera_activa = Carreras.objects.get(estatus='activa').id
        
        #vuelta = Vueltas(equipo_id = request.data['equipo'], carrera_id= carrera_activa, vuelta=request.data['vuelta'],tiempo_total=request.data['tiempo_total'],tiempo_vuelta=request.data['tiempo_vuelta'])
        
        #print(request.data['vuelta'])
        params = {
            'equipo': request.data['equipo'],
            'carrera': carrera_activa,
            'tiempo_total': request.data['tiempo_total'],
            'tiempo_vuelta': request.data['tiempo_vuelta'],
            'vuelta': request.data['vuelta']
        }
        serializador = VueltasSerializer(data=params)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def lista_vueltas_detail(request, pk):

    try:
        vuelta = Vueltas.objects.get(pk=pk)
    except Vueltas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = VueltasSerializer(vuelta)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = VueltasSerializer(vuelta, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vuelta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def lista_posiciones(request,teams):
    numTeams=teams*2
    try:

        carrera_activa = Carreras.objects.get(estatus='activa')
        #posiciones = Vueltas.objects.all()
        
        vueltasOrdenadas = Vueltas.objects.filter(carrera_id=carrera_activa.id).order_by('-vuelta','tiempo_total')
        
        
        
        pilotosCorriendo=[]
        vueltasPosicionadas=[]
        equiposCorriendo=[]
        tmpVuelta=[]
        tmpTotal=[]
        listEquiposCorriendo=[]

        

        for index, vuelta in enumerate(vueltasOrdenadas):
            
            nombreCorredor=Miembros.objects.get(cargo_id=5,equipo_id=vuelta.equipo).nombre
            
            if nombreCorredor in pilotosCorriendo:
                pass
            else:
                pilotosCorriendo.append(nombreCorredor)
                vueltasPosicionadas.append(vuelta.vuelta)
                equiposCorriendo.append(vuelta.equipo.nombre)
                tmpTotal.append(vuelta.tiempo_total)
                tmpVuelta.append(vuelta.tiempo_vuelta) 
                listEquiposCorriendo.append(vuelta.equipo)#este esta por si acaso, no es usado
            
            numTeams=numTeams-1
            if numTeams==0:
                break
        auxlen = len(equiposCorriendo)
        posiciones=1
        json=""
        while auxlen>0:
            indice = posiciones-1

            posicion= posiciones
            nombre= pilotosCorriendo[indice]
            vuelta=vueltasPosicionadas[indice]
            equipo=equiposCorriendo[indice]
            tiempo_vuelta=tmpVuelta[indice]
            tiempo_total=tmpTotal[indice]
            jsonAux='{ "posicion" : "%s", "nombre":"%s", "vuelta":"%s", "equipo":"%s", "tiempo_vuelta":"%s", "tiempo_total":"%s" }, '%(posicion,nombre,vuelta,equipo,tiempo_vuelta,tiempo_total)
            json=json+jsonAux

            auxlen=auxlen-1
            posiciones=posiciones+1
            
        json = "["+json+"]"
        #posiciones = Vueltas.objects.get(pk=1)
        #corredores = posiciones.equipo
        """Poner siempre el many cuando se requiera responder con
        un arreglo """
        serializador = VueltasSerializer(vueltasOrdenadas, many=True)
        #serializador2 = EquiposSerializer(corredores)
    except Carreras.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        #serializador = CarrerasSerializer(carrera_activa)
        #return Response(serializador.data)
        #return Response(equiposCorriendo[0])
        #return Response(pilotosCorriendo)
        print(json)
        return Response(json)

