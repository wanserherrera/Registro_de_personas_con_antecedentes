
from decimal import Decimal
import email
from email.policy import default
from pickletools import decimalnl_long
from django.shortcuts import render, redirect
from django.http import HttpResponse
from xml.dom.minidom import Document
from Aplicacion1.models import *
from django.template import RequestContext
from django.contrib import messages	
from django.db.models import Q
import datetime,socket
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import *
from .utils import render_to_pdf

delete_state="3"
exist_state="1"


def signup(request):
    return render(request, 'paginas/auth/signup.html')

def signin(request):
	flag = 0
	if request.user.is_authenticated:
		return redirect('inicio')
    
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		try:
			user = User.objects.get(username=username)
		except:
			flag = 1
			messages.error(request, 'El usuario o contraseña no existe')
            
		user = authenticate(request, username=username, password=password)

		if flag != 1:
			if user is not None:
				login(request, user)
				try:
					return redirect(request.GET.get('next'))
				except:
					return redirect('inicio')

			else:
				messages.error(request, 'El usuario o contraseña no existe')
	
	return render(request, 'paginas/auth/signin.html')
    #return render(request, 'paginas/auth/signin.html')

@login_required(login_url='signin')
def logoutUser(request):
    logout(request)
    return redirect('signin')

# Create your views here.


@login_required(login_url='signin')
def inicio(request):
	return render(request, 'paginas/index.html')


@login_required(login_url='signin')
def registerTipoDocumento(request):
	return render(request,'paginas/type_doc/add.html')

@login_required(login_url='signin')
def listTipoDocumento(request):
    TiposdeDocumento=Tipodocumento.objects.filter(activo="1")

    return render(request, "paginas/type_doc/list.html", {"tiposDocumento": TiposdeDocumento})

@login_required(login_url='signin')
def createTipoDocumento(request):
	
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	TiposdeDocumento = Tipodocumento.objects.create(
		documento=documento,
		descripcion=descripcion,
		activo= "1",
		estado="1",
		obs=obs,
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,

		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Documento guardado correctamente")
	return redirect("/documentType/",  RequestContext(request))

@login_required(login_url='signin')
def deleteTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	Tiposdocumento.activo="0"
	Tiposdocumento.estado="3"
	Tiposdocumento.save()
	return redirect("/documentType/")

@login_required(login_url='signin')
def editTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id) 
	return render(request,'paginas/type_doc/add.html', {"tipoDocumento": Tiposdocumento})

@login_required(login_url='signin')
def modifyTipoDocumento(request, id):
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	Tiposdocumento.documento=documento
	Tiposdocumento.descripcion=descripcion
	Tiposdocumento.obs=obs
	Tiposdocumento.fechamodifica=datetime.datetime.now()
	Tiposdocumento.idusermodifica= request.user.id
	Tiposdocumento.save()

	Tiposdocumento.maqmodifica=socket.gethostbyname(socket.gethostname()),

	messages.success(request, "Documento editado correctamente")
	return redirect("/documentType/")


@login_required(login_url='signin')
def viewTipoDocumento(request, id):
	Tiposdocumento=Tipodocumento.objects.get(id=id)
	return render(request,'paginas/type_doc/view.html', {"tipoDocumento": Tiposdocumento})



#Tipo de documento ORI

@login_required(login_url='signin')
def registerTipoDocumentoORI(request):
	return render(request,'paginas/tipo_doc_ori/add.html')

@login_required(login_url='signin')
def listTipoDocumentoORI(request):
    TiposdeDocumentoORI=Tipodocori.objects.filter(activo="1")

    return render(request, "paginas/tipo_doc_ori/list.html", {"tiposDocumentoORI": TiposdeDocumentoORI})

@login_required(login_url='signin')
def createTipoDocumentoORI(request):
	
	documento = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs = request.POST.get('Obs',False)
	grupo = request.POST.get('Grupo',False)
	TiposdeDocumentoORI = Tipodocori.objects.create(
		documento=documento,
		descripcion=descripcion,
		grupo = grupo,
		activo= "1",
		estado="1",
		obs=obs,
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Documento guardado correctamente")
	return redirect("/documentTypeORI/",  RequestContext(request))

@login_required(login_url='signin')
def deleteTipoDocumentoORI(request, id):
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	TiposdocumentoORI.activo="0"
	TiposdocumentoORI.estado="3"
	TiposdocumentoORI.save()
	return redirect("/documentTypeORI/")

@login_required(login_url='signin')
def editTipoDocumentoORI(request, id):
	TiposdocumentoORI= Tipodocori.objects.get(id=id) 
	return render(request,'paginas/tipo_doc_ori/add.html', {"tipoDocumentoORI": TiposdocumentoORI})

@login_required(login_url='signin')
def modifyTipoDocumentoORI(request, id):
	documentoORI = request.POST.get('Documento',False)
	descripcion =request.POST.get('Descripcion',False)
	obs =request.POST.get('Obs',False)
	grupo = request.POST.get('Grupo',False)
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	TiposdocumentoORI.documento=documentoORI
	TiposdocumentoORI.descripcion=descripcion
	TiposdocumentoORI.grupo=grupo
	TiposdocumentoORI.obs=obs
	TiposdocumentoORI.fechamodifica=datetime.datetime.now()
	TiposdocumentoORI.idusermodifica= request.user.id
	TiposdocumentoORI.maqmodifica=socket.gethostbyname(socket.gethostname())

	TiposdocumentoORI.save()
	return redirect("/documentTypeORI/")


@login_required(login_url='signin')
def viewTipoDocumentoORI(request, id):
	TiposdocumentoORI=Tipodocori.objects.get(id=id)
	return render(request,'paginas/tipo_doc_ori/view.html', {"tipoDocumentoORI": TiposdocumentoORI})





#Maestro Areas ORI

@login_required(login_url='signin')
def registerMAreasORI(request):
	return render(request,'paginas/m_areas_ori/add.html')

@login_required(login_url='signin')
def listMAreasORI(request):
    MAreasori=Mareasori.objects.filter(activo="1")

    return render(request, "paginas/m_areas_ori/list.html", {"MAreasori":  MAreasori})

@login_required(login_url='signin')
def createMAreasORI(request):
	
	MAreasori = Mareasori.objects.create(
		area=request.POST.get('area',False),
		grupo =request.POST.get('grupo',False),
		tipo=request.POST.get('tipo',False),
		encargado=request.POST.get('encargado',False),
		email=request.POST.get('email',False),
		nexo=request.POST.get('nexo',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Area guardada correctamente")
	return redirect("/mAreasORI/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMAreasORI(request, id):
	MAreasori=Mareasori.objects.get(id=id)
	MAreasori.activo="0"
	MAreasori.estado="3"
	MAreasori.save()
	return redirect("/mAreasORI/")

@login_required(login_url='signin')
def editMAreasORI(request, id):
	MAreasori= Mareasori.objects.get(id=id) 
	return render(request,'paginas/m_areas_ori/add.html', {"MAreaORI": MAreasori})

@login_required(login_url='signin')
def modifyMAreasORI(request, id):
	
	MAreasori=Mareasori.objects.get(id=id)
	MAreasori.area=request.POST.get('area',False)
	MAreasori.grupo =request.POST.get('grupo',False)
	MAreasori.tipo=request.POST.get('tipo',False)
	MAreasori.encargado=request.POST.get('encargado',False)
	MAreasori.email=request.POST.get('email',False)
	MAreasori.nexo=request.POST.get('nexo',False)
	MAreasori.obs=request.POST.get('obs',False)
	MAreasori.fechamodifica=datetime.datetime.now()
	MAreasori.idusermodifica= request.user.id
	MAreasori.maqmodifica=socket.gethostbyname(socket.gethostname())

	MAreasori.save()
	messages.success(request, "Documento editado correctamente")
	return redirect("/mAreasORI/")


@login_required(login_url='signin')
def viewMAreasORI(request, id):
	MAreasori=Mareasori.objects.get(id=id)
	return render(request,'paginas/m_areas_ori/view.html', {"MAreaORI": MAreasori})







#Maestro Factor

@login_required(login_url='signin')
def registerMFactor(request):
	return render(request,'paginas/m_factor/add.html')

@login_required(login_url='signin')
def listMFactor(request):
    MFactor=Mfactor.objects.filter(activo="1")

    return render(request, "paginas/m_factor/list.html", {"MFactors":  MFactor})

@login_required(login_url='signin')
def createMFactor(request):
	
	MFactor = Mfactor.objects.create(
		idasunto=request.POST.get('idasunto',False),
		asunto=request.POST.get('asunto',False),
		idfactor=request.POST.get('idfactor',False),
		factor=request.POST.get('factor',False),
		idsubfactor=request.POST.get('idsubfactor',False),
		subfactor=request.POST.get('subfactor',False),
		historial =request.POST.get('historial',False),
		grupo =request.POST.get('grupo',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Factor guardado correctamente")
	return redirect("/mFactor/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMFactor(request, id):
	MFactor=Mfactor.objects.get(id=id)
	MFactor.activo="0"
	MFactor.estado="3"
	MFactor.save()
	return redirect("/mFactor/")

@login_required(login_url='signin')
def editMFactor(request, id):
	MFactor= Mfactor.objects.get(id=id) 
	return render(request,'paginas/m_factor/add.html', {"MFactor": MFactor})

@login_required(login_url='signin')
def modifyMFactor(request, id):
	
	MFactor=Mfactor.objects.get(id=id)
	MFactor.idasunto=request.POST.get('idasunto',False)
	MFactor.asunto=request.POST.get('asunto',False)
	MFactor.idfactor=request.POST.get('idfactor',False)
	MFactor.factor=request.POST.get('factor',False)
	MFactor.idsubfactor=request.POST.get('idsubfactor',False)
	MFactor.subfactor=request.POST.get('subfactor',False)
	MFactor.historial =request.POST.get('historial',False)
	MFactor.grupo =request.POST.get('grupo',False)
	MFactor.obs=request.POST.get('obs',False)
	MFactor.fechamodifica=datetime.datetime.now()
	MFactor.idusermodifica= request.user.id
	MFactor.maqmodifica=socket.gethostbyname(socket.gethostname())
	MFactor.save()
	messages.success(request, "Factore editado correctamente")
	return redirect("/mFactor/")


@login_required(login_url='signin')
def viewMFactor(request, id):
	MFactor=Mfactor.objects.get(id=id)
	return render(request,'paginas/m_factor/view.html', {"MFactor": MFactor})





#Maestro User Rol

@login_required(login_url='signin')
def registerMUserRol(request):
	return render(request,'paginas/m_user_rol/add.html')

@login_required(login_url='signin')
def listMUserRol(request):
    MUserRol=Muserrol.objects.filter(activo="1")

    return render(request, "paginas/m_user_rol/list.html", {"MUsersRols":  MUserRol})

@login_required(login_url='signin')
def createMUserRol(request):
	
	MUserRol = Muserrol.objects.create(
		
		rol =request.POST.get('rol',False),
		descripcion =request.POST.get('descripcion',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),


		)
	messages.success(request, "Nuevo rol guardado correctamente")

	return redirect("/mUserRol/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMUserRol(request, id):
	MUserRol=Muserrol.objects.get(id=id)
	MUserRol.activo="0"
	MUserRol.estado="3"
	MUserRol.save()
	return redirect("/mUserRol/")

@login_required(login_url='signin')
def editMUserRol(request, id):
	MUserRol= Muserrol.objects.get(id=id) 
	return render(request,'paginas/m_user_rol/add.html', {"MUserRol": MUserRol})

@login_required(login_url='signin')
def modifyMUserRol(request, id):
	
	MUserRol=Muserrol.objects.get(id=id)
	MUserRol.rol =request.POST.get('rol',False)
	MUserRol.descripcion =request.POST.get('descripcion',False)
	MUserRol.obs=request.POST.get('obs',False)
	MUserRol.fechamodifica=datetime.datetime.now()
	MUserRol.idusermodifica= request.user.id
	MUserRol.maqmodifica=socket.gethostbyname(socket.gethostname())
	MUserRol.save()
	messages.success(request, "Rol de usuario editado correctamente")
	return redirect("/mUserRol/")


@login_required(login_url='signin')
def viewMUserRol(request, id):
	MUserRol=Muserrol.objects.get(id=id)
	return render(request,'paginas/m_user_rol/view.html', {"MUserRol": MUserRol})





#Maestro User

@login_required(login_url='signin')
def registerMUser(request):
	return render(request,'paginas/m_user/add.html',{"Roles": Muserrol.objects.filter(activo="1")})

@login_required(login_url='signin')
def listMUser(request):
    MUser=Muser.objects.filter(activo="1")
    return render(request, "paginas/m_user/list.html", {"MUsers":  MUser})

@login_required(login_url='signin')
def createMUser(request):
	
	MUser = Muser.objects.create(
		
		cip =request.POST.get('cip',False),
		codigo =request.POST.get('codigo',False),
		apepaterno =request.POST.get('apepaterno',False),
		apematerno =request.POST.get('apematerno',False),
		nombres =request.POST.get('nombres',False),
		email =request.POST.get('email',False),
		idrol = Muserrol.objects.get(id=request.POST.get('idrol',False)),
		motivobaja =request.POST.get('motivobaja',False),
		obs=request.POST.get('obs',False),
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),
		)
	messages.success(request, "Nuevo usuario guardado correctamente")
	return redirect("/mUser/",  RequestContext(request))

@login_required(login_url='signin')
def deleteMUser(request, id):
	MUser=Muser.objects.get(id=id)
	MUser.activo="0"
	MUser.estado="3"
	MUser.save()
	return redirect("/mUser/")

@login_required(login_url='signin')
def editMUser(request, id):
	MUser= Muser.objects.get(id=id) 
	return render(request,'paginas/m_user/add.html', {"MUser": MUser,"Roles": Muserrol.objects.filter(activo="1")})

@login_required(login_url='signin')
def modifyMUser(request, id):
	
	MUser=Muser.objects.get(id=id)
	MUser.cip =request.POST.get('cip',False)
	MUser.codigo =request.POST.get('codigo',False)
	MUser.apepaterno =request.POST.get('apepaterno',False)
	MUser.apematerno =request.POST.get('apematerno',False)
	MUser.nombres =request.POST.get('nombres',False)
	MUser.email =request.POST.get('email',False)
	MUser.idrol = Muserrol.objects.get(id=request.POST.get('idrol',False))
	MUser.motivobaja =request.POST.get('motivobaja',False)

	MUser.obs=request.POST.get('obs',False)
	MUser.fechamodifica=datetime.datetime.now()
	MUser.idusermodifica= request.user.id
	MUser.maqmodifica=socket.gethostbyname(socket.gethostname())
	MUser.save()
	messages.success(request, "Usuario editado correctamente")
	return redirect("/mUser/")


@login_required(login_url='signin')
def viewMUser(request, id):
	MUser=Muser.objects.get(id=id)
	return render(request,'paginas/m_user/view.html', {"MUser": MUser})





#Maestro IPersona

@login_required(login_url='signin')
def registerIPersona(request):
	departamentos = Mubigeo.objects.all().values('iddepartamento',
                                                 'departamento').distinct()
	return render(request,'paginas/i_persona/add.html', 
	{"Tipopersona":Tipopersona.objects.filter(activo="1"),
	"Mprocedencia":Mprocedencia.objects.filter(activo="1"),
	"Mpais":Mpais.objects.filter(activo="1"),
	"Tipodocumento":Tipodocumento.objects.filter(activo="1"),
	"Mubigeo":Mubigeo.objects.filter(activo="1"),
	"Mestadocivil":Mestadocivil.objects.filter(activo="1"),
	"Mgenero": Mgenero.objects.filter(activo="1"),
	"Mgradoinstruccion":Mgradoinstruccion.objects.filter(activo="1"),
	"Mfactor":Mfactor.objects.filter(activo="1"),
	"Tiporaza":Tiporaza.objects.filter(activo="1"),
	"Tipocontextura":Tipocontextura.objects.filter(activo="1"),
	"d": departamentos
	})

@login_required(login_url='signin')
def listIPersona(request):
	IPersona=Ipersona.objects.filter(activo="1")
	tipopersona=Tipopersona.objects.all().filter(activo="1")
	return render(request, "paginas/i_persona/list.html", {"IPersonas":  IPersona, "tipopersona": tipopersona})

@login_required(login_url='signin')
def createIPersona(request):

	IPersona = Ipersona.objects.create(
		idtipopersona = Tipopersona.objects.get(id=request.POST.get('idtipopersona',False)) ,
		idprocedencia =  Mprocedencia.objects.get(id=request.POST.get('idprocedencia',False)) ,
		idpais =  Mpais.objects.get(id=request.POST.get('idpais',False)),
		idtipodocumento =  Tipodocumento.objects.get(id=request.POST.get('idtipodocumento',False)),
		nrodoc=request.POST.get('nrodoc',False),
		otrodocumento=request.POST.get('otrodocumento',False) , 
		apepaterno=request.POST.get('apepaterno',False) ,
		apematerno=request.POST.get('apematerno',False) ,
		nombres=request.POST.get('nombres',False) ,
		fechanacimiento=request.POST.get('fechanacimiento',False) if request.POST.get('fechanacimiento',False) else None ,
		natural=request.POST.get('natural',False) ,
		idestadocivil =  Mestadocivil.objects.get(id=request.POST.get('idestadocivil',False)),
		idgenero =  Mgenero.objects.get(id=request.POST.get('idgenero',False)) ,
		idubigeo =  Mubigeo.objects.get(iddepartamento = request.POST.get('departamentos', False), idprovincia=request.POST.get('provincias', False),iddistrito=request.POST.get('ciudades', False) ) ,
		domicilio=request.POST.get('domicilio',False),
		telefono=request.POST.get('telefono',False),
		ocupacion=request.POST.get('ocupacion',False) ,
		religion=request.POST.get('religion',False) ,
		idgradoinstruccion =  Mgradoinstruccion.objects.get(id=request.POST.get('idgradoinstruccion',False)) ,
		profesion=request.POST.get('profesion',False) ,
		centroestudios=request.POST.get('centroestudios',False) ,
		email=request.POST.get('email',False),
		redessociales=request.POST.get('redessociales',False),
		idfactor =  Mfactor.objects.get(id=request.POST.get('idfactor',False)) ,
		tipoorganizacion=request.POST.get('tipoorganizacion',False),
		modalidaddelito=request.POST.get('modalidaddelito',False) ,
		alias=request.POST.get('alias',False) ,
		talla=request.POST.get('talla') if request.POST.get('talla') else None,
		peso=request.POST.get('peso')  if request.POST.get('peso') else None,
		idraza =  Tiporaza.objects.get(id=request.POST.get('idraza',False)),
		idcontextura = Tipocontextura.objects.get(id=request.POST.get('idcontextura',False)),
		caminada=request.POST.get('caminada',False) ,
		cicatrices=request.POST.get('cicatrices',False) ,
		tatuajes=request.POST.get('tatuajes',False) ,
		habitos=request.POST.get('habitos',False) ,
		vicios=request.POST.get('vicios',False) ,
		defectos=request.POST.get('defectos',False) ,
		tipo=request.POST.get('tipo') if request.POST.get('tipo') else None ,
		obs=request.POST.get('obs', '') ,
		archivo=request.POST.get('archivo',False) ,
		activo= "1",
		estado="1",
		fechacrea= datetime.datetime.now(),
		fechamodifica=datetime.datetime.now(),
		idusercrea= request.user.id,
		idusermodifica= request.user.id,
		maqcrea=socket.gethostbyname(socket.gethostname()),
		maqmodifica=socket.gethostbyname(socket.gethostname()),
		foto=request.FILES.get('avatar') if request.FILES.get('avatar') else None,
		


		)
	#print(foto)
	messages.success(request, "Nueva persona guardada correctamente")

	return redirect("/iPersona/",  RequestContext(request))

def generarpdf(request):
	tipopersona = request.POST['tipopersona']
	personas = Ipersona.objects.all().filter(idtipopersona__id=tipopersona,activo="1")
	data = {'personas': personas}
	pdf = render_to_pdf('paginas/i_persona/documentpdf.html', data)
	return HttpResponse(pdf, content_type='application/pdf')
	


@login_required(login_url='signin')
def deleteIPersona(request, id):
	IPersona=Ipersona.objects.get(id=id)
	IPersona.activo="0"
	IPersona.estado="3"
	IPersona.save()
	return redirect("/iPersona/")

@login_required(login_url='signin')
def editIPersona(request, id):
	IPersona= Ipersona.objects.get(id=id) 
	departamentos = Mubigeo.objects.all().values('iddepartamento',
                                                 'departamento').distinct()
	provincias = Mubigeo.objects.all().filter(
        iddepartamento=IPersona.idubigeo.iddepartamento).values('idprovincia',
                                              'provincia').distinct()
	
	ciudades = Mubigeo.objects.all().filter(iddepartamento=IPersona.idubigeo.iddepartamento,
                                            idprovincia=IPersona.idubigeo.idprovincia)

	return render(request,'paginas/i_persona/add.html', {"IPersona": IPersona,
	"Tipopersona":Tipopersona.objects.filter(activo="1"),
	"Mprocedencia":Mprocedencia.objects.filter(activo="1"),
	"Mpais":Mpais.objects.filter(activo="1"),
	"Tipodocumento":Tipodocumento.objects.filter(activo="1"),
	"Mubigeo": IPersona.idubigeo,
	"Mestadocivil":Mestadocivil.objects.filter(activo="1"),
	"Mgenero": Mgenero.objects.filter(activo="1"),
	"Mgradoinstruccion":Mgradoinstruccion.objects.filter(activo="1"),
	"Mfactor":Mfactor.objects.filter(activo="1"),
	"Tiporaza":Tiporaza.objects.filter(activo="1"),
	"Tipocontextura":Tipocontextura.objects.filter(activo="1"),
	"d":departamentos,
	"p":provincias,
	"c": ciudades
	})

@login_required(login_url='signin')
def modifyIPersona(request, id):
	
	IPersona=Ipersona.objects.get(id=id)
	IPersona.idtipopersona = Tipopersona.objects.get(id=request.POST.get('idtipopersona',False))
	IPersona.idprocedencia =  Mprocedencia.objects.get(id=request.POST.get('idprocedencia',False))
	IPersona.idpais =  Mpais.objects.get(id=request.POST.get('idpais',False))
	IPersona.idtipodocumento =  Tipodocumento.objects.get(id=request.POST.get('idtipodocumento',False))
	IPersona.nrodoc=request.POST.get('nrodoc',False)
	IPersona.otrodocumento=request.POST.get('otrodocumento',False)
	IPersona.apepaterno=request.POST.get('apepaterno',False)
	IPersona.apematerno=request.POST.get('apematerno',False)
	IPersona.nombres=request.POST.get('nombres',False)
	
	IPersona.fechanacimiento=request.POST.get('fechanacimiento',False) if request.POST.get('fechanacimiento',False) else None 
	print('asdas',IPersona.fechanacimiento,'1asda')
	IPersona.natural=request.POST.get('natural',False)
	IPersona.idestadocivil =  Mestadocivil.objects.get(id=request.POST.get('idestadocivil',False))
	IPersona.idgenero =  Mgenero.objects.get(id=request.POST.get('idgenero',False))
	IPersona.idubigeo =  Mubigeo.objects.get(iddepartamento = request.POST.get('departamentos'), idprovincia=request.POST.get('provincias'),iddistrito=request.POST.get('ciudades') )
	IPersona.domicilio=request.POST.get('domicilio',False)
	IPersona.telefono=request.POST.get('telefono',False)
	IPersona.ocupacion=request.POST.get('ocupacion',False)
	IPersona.religion=request.POST.get('religion',False)
	IPersona.idgradoinstruccion =  Mgradoinstruccion.objects.get(id=request.POST.get('idgradoinstruccion',False))
	IPersona.profesion=request.POST.get('profesion',False)
	IPersona.centroestudios=request.POST.get('centroestudios',False)
	IPersona.email=request.POST.get('email',False)
	IPersona.redessociales=request.POST.get('redessociales',False)
	IPersona.idfactor =  Mfactor.objects.get(id=request.POST.get('idfactor',False))
	IPersona.tipoorganizacion=request.POST.get('tipoorganizacion',False)
	IPersona.modalidaddelito=request.POST.get('modalidaddelito',False)
	IPersona.alias=request.POST.get('alias',False)
	IPersona.talla=request.POST.get('talla',False) if request.POST.get('talla') else None
	IPersona.peso=request.POST.get('peso',False) if request.POST.get('peso') else None
	IPersona.idraza =  Tiporaza.objects.get(id=request.POST.get('idraza',False))
	IPersona.idcontextura = Tipocontextura.objects.get(id=request.POST.get('idcontextura',False))
	IPersona.caminada=request.POST.get('caminada',False)
	IPersona.cicatrices=request.POST.get('cicatrices',False)
	IPersona.tatuajes=request.POST.get('tatuajes',False)
	IPersona.habitos=request.POST.get('habitos',False)
	IPersona.vicios=request.POST.get('vicios',False)
	IPersona.defectos=request.POST.get('defectos',False)
	IPersona.tipo=request.POST.get('tipo',False) if request.POST.get('tipo') else None 
	IPersona.obs=request.POST.get('obs',False)
	IPersona.archivo=request.POST.get('archivo',False)
	IPersona.fechamodifica=datetime.datetime.now()
	IPersona.idusermodifica= request.user.id
	IPersona.maqmodifica=socket.gethostbyname(socket.gethostname())

	if request.POST.get('avatar',False) != '':

		#IPersona.foto=request.POST.get('avatar',False)
		IPersona.foto=request.FILES.get('avatar',False)


	IPersona.save()
	return redirect("/iPersona/")


@login_required(login_url='signin')
def viewIPersona(request, id):
	IPersona=Ipersona.objects.get(id=id)
	return render(request,'paginas/i_persona/view.html', {"IPersona": IPersona})

@login_required(login_url='signin')
def load_province(request):
    iddepartamento = request.GET.get('departamentoid')
    provincias = Mubigeo.objects.all().filter(
        iddepartamento=iddepartamento).values('idprovincia',
                                              'provincia').distinct()
    return render(request, 'paginas/i_persona/provinceSelect.html', {'provincias': provincias})


@login_required(login_url='signin')
def load_cities(request):
    iddepartamento = request.GET.get('departamentoid')
    idprovincia = request.GET.get('provinciaid')
    ciudades = Mubigeo.objects.all().filter(iddepartamento=iddepartamento,
                                            idprovincia=idprovincia)
    return render(request, 'paginas/i_persona/ciudadSelect.html', {'ciudad': ciudades})

def searchIPersona(request):
	IPersona= Ipersona.objects.filter(activo="9")
	comodin = request.POST.get('comodin') 
	dni= request.POST.get('dni') 
	apepaterno= request.POST.get('apepaterno') 
	apematerno= request.POST.get('apematerno') 
	nombres= request.POST.get('nombres') 
	print(comodin)
	if request.POST.get('comodin'):
		IPersona= Ipersona.objects.filter(Q(activo = "1"), Q(nrodoc = comodin)| Q(nombres = comodin)| 
		Q(apepaterno = comodin)| Q(apematerno = comodin)|  Q(natural = comodin)| Q(domicilio = comodin)|
		Q(telefono = comodin)| Q(ocupacion = comodin)|  Q(religion = comodin)| Q(profesion = comodin)|
		Q(centroestudios = comodin)| Q(email = comodin)|  Q(redessociales = comodin)| Q(tipoorganizacion = comodin)|
		Q(modalidaddelito = comodin)| Q(alias = comodin)|  Q(caminada = comodin)| Q(cicatrices = comodin)|
		Q(habitos = comodin)| Q(vicios = comodin)|  Q(defectos = comodin)| Q(obs = comodin)| Q(archivo = comodin))

	else:
		if request.POST.get('dni'):
			IPersona= IPersona.union(Ipersona.objects.filter(activo="1",nrodoc = dni))
		if request.POST.get('apepaterno'):
			IPersona= IPersona.union(Ipersona.objects.filter(activo="1",apepaterno = apepaterno))
		if request.POST.get('apematerno'):
			IPersona= IPersona.union(Ipersona.objects.filter(activo="1",apematerno = apematerno))
		if request.POST.get('nombres'):
			IPersona= IPersona.union(Ipersona.objects.filter(activo="1",nombres = nombres))
		

	return render(request, "paginas/i_persona/list.html", {"IPersonas":  IPersona,"comodin":  comodin,"dni":  dni,
	"apepaterno":  apepaterno, "apematerno":  apematerno, "nombres":  nombres})
   
#---- ANTECEDENTES PENALES ----#
@login_required(login_url='signin')
def createRPenales(request, pk):
	form = RPenalesForm()
	if request.method == 'POST':
		form = RPenalesForm(request.POST, request.FILES)
		print('x')
		if form.is_valid():
			form = form.save(commit = False)
			persona= Ipersona.objects.get(id=pk)
			form.idpersona = persona
			form.nrodoc = persona.nrodoc
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/rPenales/"+pk)
	context={'form':form, 'pk':pk}
	return render(request, 'paginas/r_penales/add.html', context)

@login_required(login_url='signin')
def updateRPenales(request, pk):
	penales = Rpenales.objects.get(id=pk)
	form = RPenalesForm(instance=penales)
	if request.method == 'POST':
		form = RPenalesForm(request.POST, request.FILES , instance=penales)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/rPenales/"+str(form.idpersona.id))
	context={'form':form}
	return render(request, 'paginas/r_penales/add.html', context)

@login_required(login_url='signin')
def listRPenales(request,pk):
	RPenales = Rpenales.objects.all().filter(idpersona=pk, activo="1")
	context = {'RPenales':RPenales, 'pk':pk}
	return render(request, 'paginas/r_penales/list.html', context)

def getRPenalesData(request):
	idRPenal = request.GET.get('id')
	RPenales = Rpenales.objects.filter(id=idRPenal, activo="1")
	context = {'registro': RPenales}
	return render(request, "paginas/r_penales/showdataRPenales.html", context)

@login_required(login_url='signin')
def deleteRPenales(request, pk):
	penales=Rpenales.objects.get(id=pk)
	penales.activo="0"
	penales.estado="3"
	penales.save()
	return redirect("/rPenales/"+str(penales.idpersona.id))

@login_required(login_url='signin')
def viewRPenales(request, pk):
	penales=Rpenales.objects.get(id=pk)
	context = {'penales':penales}
	return render(request,'paginas/r_penales/view.html', context)

@login_required(login_url='signin')
def listAllRPenales(request):
	RPenales = Rpenales.objects.all().filter(activo="1")
	context = {'RPenales':RPenales}
	return render(request, 'paginas/r_penales/listall.html', context)

#---- RELACIONES FAMILIARES ----#

@login_required(login_url='signin')
def createRFamiliares(request, pk):
	if request.method == 'POST':
		form = RFamiliaresForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			persona= Ipersona.objects.get(id=pk)
			form.idpersona = persona
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/rFamiliares/"+pk)
	else:
		form = RFamiliaresForm()
		#Mprocedencia = Mprocedencia.objects.filter(active=1)
		parentescos = Mparentesco.objects.filter(estado=1)
		context={'form':form, 'pk':pk, 'parentescos':parentescos}
		
		return render(request, 'paginas/r_familiares/add.html', context)



def getRFamiliaresData(request):
	idRFamiliar = request.GET.get('id')
	RFamiliares = Rfamiliares.objects.filter(id=idRFamiliar, activo="1")
	context = {'registro': RFamiliares}
	return render(request, "paginas/r_familiares/showdataRFamiliares.html", context)

@login_required(login_url='signin')
def updateRFamiliares(request, pk):
	penales = Rfamiliares.objects.get(id=pk)
	form = RFamiliaresForm(instance=penales)
	if request.method == 'POST':
		form = RFamiliaresForm(request.POST, request.FILES , instance=penales)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/rFamiliares/"+str(form.idpersona.id))
	parentescos = Mparentesco.objects.filter(estado=1)
	context={'form':form,'parentescos':parentescos}
	return render(request, 'paginas/r_familiares/add.html', context)

@login_required(login_url='signin')
def listRFamiliares(request,pk):
	RPenales = Rfamiliares.objects.filter(idpersona=pk, activo="1")
	context = {'RPenales':RPenales, 'pk':pk}
	return render(request, 'paginas/r_familiares/list.html', context)

@login_required(login_url='signin')
def deleteRFamiliares(request, pk):
	penales=Rfamiliares.objects.get(id=pk)
	penales.activo="0"
	penales.estado="3"
	penales.save()
	return redirect("/rFamiliares/"+str(penales.idpersona.id))

@login_required(login_url='signin')
def viewRFamiliares(request, pk):
	penales=Rfamiliares.objects.get(id=pk)
	context = {'penales':penales}
	return render(request,'paginas/r_familiares/view.html', context)

@login_required(login_url='signin')
def listAllRFamiliares(request):
	familiares = Rfamiliares.objects.filter(activo="1")
	context = {'familiares':familiares}
	return render(request, 'paginas/r_familiares/listall.html', context)

#------------PRUEBAS----------------
@login_required(login_url='signin')
def viewTest(request, pk, pk2):
	persona = Ipersona.objects.get(id=pk)
	penales= Rpenales.objects.filter(idpersona=pk, activo="1")
	penalesi= Rpenales.objects.get(id=pk2, activo="1")
	context = {'penales':penales, 'persona':persona, 'penalesi':penalesi, 'pk':pk}
	return render(request,'paginas/r_penales/test.html', context)
#------------PRUEBAS----------------

#---- ANTECEDENTES FUERZAS ARMADAS ----#

@login_required(login_url='signin')
def createIFFAA(request, pk):
	if request.method == 'POST':
		form = IFFAAForm(request.POST, request.FILES)
		
		if form.is_valid():
			form = form.save(commit = False)
			
			persona= Ipersona.objects.get(id=pk)
			form.idpersona = persona
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/iFFAA/"+pk)
	else:
		form = IFFAAForm()
		tffaa = Tipoffaa.objects.filter(activo="1")
		context={'form':form, 'pk':pk, 'tffaa':tffaa}
		
		return render(request, 'paginas/i_ffaa/add.html', context)

@login_required(login_url='signin')
def updateIFFAA(request, pk):
	ffaa = Iffaa.objects.get(id=pk)
	form = IFFAAForm(instance=ffaa)
	if request.method == 'POST':
		form = IFFAAForm(request.POST, request.FILES , instance=ffaa)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/iFFAA/"+str(form.idpersona.id))
	tffaa = Tipoffaa.objects.filter(activo="1")
	context={'form':form, 'tffaa':tffaa}
	return render(request, 'paginas/i_ffaa/add.html', context)

@login_required(login_url='signin')
def listIFFAA(request,pk):
	ffaa = Iffaa.objects.filter(idpersona=pk, activo="1")
	context = {'ffaa':ffaa, 'pk':pk}
	return render(request, 'paginas/i_ffaa/list.html', context)

@login_required(login_url='signin')
def deleteIFFAA(request, pk):
	ffaa=Iffaa.objects.get(id=pk)
	ffaa.activo="0"
	ffaa.estado="3"
	ffaa.save()
	return redirect("/iFFAA/"+str(ffaa.idpersona.id))

@login_required(login_url='signin')
def viewIFFAA(request, pk):
	ffaa=Iffaa.objects.get(id=pk)
	context = {'ffaa':ffaa}
	return render(request,'paginas/i_ffaa/view.html', context)

@login_required(login_url='signin')
def getRIFFAA(request):
	idRIFFAA = request.GET.get('id')
	RFIFFAA = Iffaa.objects.filter(id=idRIFFAA, activo="1")
	context = {'registro': RFIFFAA}
	return render(request, "paginas/i_ffaa/showdataIFFAA.html", context)

@login_required(login_url='signin')
def listAllIFFAA(request):
	ffaa = Iffaa.objects.filter(activo="1")
	context = {'ffaa':ffaa}
	return render(request, 'paginas/i_ffaa/listall.html', context)

#---- SITUACIÓN POLICIAL ----#

@login_required(login_url='signin')
def createMsitpolicial(request):
	if request.method == 'POST':
		form = MsitpolicialForm(request.POST, request.FILES)
		
		if form.is_valid():
			form = form.save(commit = False)
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/Msitpolicial/")
	else:
		form = MsitpolicialForm()
		sitPolicial = Msitpolicial.objects.filter(activo="1")
		context={'form':form, 'sitPolicial':sitPolicial}
		
		return render(request, 'paginas/m_sit_policial/add.html', context)

@login_required(login_url='signin')
def updateMsitpolicial(request, pk):
	sitPolicial = Msitpolicial.objects.get(id=pk)
	form = MsitpolicialForm(instance=sitPolicial)
	if request.method == 'POST':
		form = MsitpolicialForm(request.POST, request.FILES , instance=sitPolicial)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/Msitpolicial/")
	context={'form':form}
	return render(request, 'paginas/m_sit_policial/add.html', context)

@login_required(login_url='signin')
def listMsitpolicial(request):
	sitPolicial = Msitpolicial.objects.filter(activo="1")
	context = {'sitPolicial':sitPolicial}
	return render(request, 'paginas/m_sit_policial/list.html', context)

@login_required(login_url='signin')
def deleteMsitpolicial(request, pk):
	sitPolicial=Msitpolicial.objects.get(id=pk)
	sitPolicial.activo="0"
	sitPolicial.estado="3"
	sitPolicial.save()
	return redirect("/Msitpolicial/")

@login_required(login_url='signin')
def viewMsitpolicial(request, pk):
	sitPolicial=Msitpolicial.objects.get(id=pk)
	context = {'sitPolicial':sitPolicial}
	return render(request,'paginas/m_sit_policial/view.html', context)



#---- ANTECEDENTES POLICIALES ----#

@login_required(login_url='signin')
def createIpolicia(request, pk):
	if request.method == 'POST':
		form = IpoliciaForm(request.POST, request.FILES)
		
		if form.is_valid():
			form = form.save(commit = False)
			persona= Ipersona.objects.get(id=pk)
			form.idpersona = persona
			form.nrodoc = persona.nrodoc
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/Ipolicia/"+pk)
	else:
		form = IpoliciaForm()
		igrado = Mgrado.objects.filter(activo="1")
		isitpolicial = Msitpolicial.objects.filter(activo="1")
		iunidad = Munidadespnp.objects.filter(activo="1")
		context={'form':form, 'pk':pk, 'igrado': igrado, 'isitpolicial':isitpolicial,'iunidad':iunidad }
		
		return render(request, 'paginas/i_policia/add.html', context)

@login_required(login_url='signin')
def updateIpolicia(request, pk):
	policia = Ipolicia.objects.get(id=pk)
	form = IpoliciaForm(instance=policia)
	if request.method == 'POST':
		form = IpoliciaForm(request.POST, request.FILES , instance=policia)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/Ipolicia/"+str(form.idpersona.id))
	context={'form':form, 'policia':policia}
	return render(request, 'paginas/i_policia/add.html', context)

@login_required(login_url='signin')
def listIpolicia(request,pk):
	policia = Ipolicia.objects.filter(idpersona=pk, activo="1")
	context = {'policia':policia, 'pk':pk}
	return render(request, 'paginas/i_policia/list.html', context)

@login_required(login_url='signin')
def deleteIpolicia(request, pk):
	policia=Ipolicia.objects.get(id=pk)
	policia.activo="0"
	policia.estado="3"
	policia.save()
	return redirect("/Ipolicia/"+str(policia.idpersona.id))

@login_required(login_url='signin')
def viewIpolicia(request, pk):
	policia=Ipolicia.objects.get(id=pk)
	context = {'policia':policia}
	return render(request,'paginas/i_policia/view.html', context)

@login_required(login_url='signin')
def getRIPNP(request):
	idRIPNP = request.GET.get('id')
	rIPNP = Ipolicia.objects.filter(id=idRIPNP, activo="1")
	context = {'registro': rIPNP}
	return render(request, "paginas/i_policia/showdataIPNP.html", context)

@login_required(login_url='signin')
def listAllIpolicia(request):
	policia = Ipolicia.objects.filter( activo="1")
	context = {'policia':policia}
	return render(request, 'paginas/i_policia/listall.html', context)

#---- FILIACION POLITICA ----#

@login_required(login_url='signin')
def createRfiliacionpolitica(request, pk):
	if request.method == 'POST':
		form = RfiliacionpoliticaForm(request.POST, request.FILES)
		
		if form.is_valid():
			form = form.save(commit = False)
			persona= Ipersona.objects.get(id=pk)
			form.idpersona = persona
			form.nrodoc = persona.nrodoc
			form.idusercrea = request.user.id
			form.idusermodifica = request.user.id
			form.activo = 1
			form.estado = 1
			form.maqcrea = socket.gethostbyname(socket.gethostname())
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			form.save()
			return redirect("/Rfiliacionpolitica/"+pk)
	else:
		form = RfiliacionpoliticaForm()
		tipoorgpolitica = Tipoorgpolitica.objects.filter(activo="1")
		context={'form':form, 'pk':pk, 'tipoorgpolitica':tipoorgpolitica}
		
		return render(request, 'paginas/r_filiacion/add.html', context)

@login_required(login_url='signin')
def updateRfiliacionpolitica(request, pk):
	filiacionpolitica = Rfiliacionpolitica.objects.get(id=pk)
	form = RfiliacionpoliticaForm(instance=filiacionpolitica)
	if request.method == 'POST':
		form = RfiliacionpoliticaForm(request.POST, request.FILES , instance=filiacionpolitica)
		if form.is_valid():
			form = form.save(commit = False)
			form.idusermodifica = request.user.id
			form.maqmodifica = socket.gethostbyname(socket.gethostname())
			print('y')
			form.save()
			return redirect("/Rfiliacionpolitica/"+str(form.idpersona.id))
	tipoorgpolitica = Tipoorgpolitica.objects.filter(activo="1")
	context={'form':form, 'filiacionpolitica':filiacionpolitica, 'tipoorgpolitica':tipoorgpolitica}
	return render(request, 'paginas/r_filiacion/add.html', context)

@login_required(login_url='signin')
def getFiliacion(request):
	idFiliacion = request.GET.get('id')
	rFiliacion = Rfiliacionpolitica.objects.filter(id=idFiliacion, activo="1")
	context = {'registro': rFiliacion}
	return render(request, "paginas/r_filiacion/showdataFiliacion.html", context)



@login_required(login_url='signin')
def listRfiliacionpolitica(request,pk):
	filiacionpolitica = Rfiliacionpolitica.objects.filter(idpersona=pk, activo="1")
	context = {'filiacionpolitica':filiacionpolitica, 'pk':pk}
	return render(request, 'paginas/r_filiacion/list.html', context)

@login_required(login_url='signin')
def deleteRfiliacionpolitica(request, pk):
	policia=Rfiliacionpolitica.objects.get(id=pk)
	policia.activo="0"
	policia.estado="3"
	policia.save()
	return redirect("/Rfiliacionpolitica/"+str(policia.idpersona.id))

@login_required(login_url='signin')
def viewRfiliacionpolitica(request, pk):
	filiacionpolitica=Rfiliacionpolitica.objects.get(id=pk)
	context = {'filiacionpolitica':filiacionpolitica}
	return render(request,'paginas/r_filiacion/view.html', context)

@login_required(login_url='signin')
def listAllRfiliacionpolitica(request):
	filiacionpolitica = Rfiliacionpolitica.objects.filter(activo="1")
	context = {'filiacionpolitica':filiacionpolitica}
	return render(request, 'paginas/r_filiacion/listall.html', context)