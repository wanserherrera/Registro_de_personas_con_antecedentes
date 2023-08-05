from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from ProyectoPNP.settings import MEDIA_ROOT, MEDIA_URL
from . import views

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('documentType/form', views.registerTipoDocumento, name = "addDocuments"),
    path('documentType/', views.listTipoDocumento, name = "listDocuments"),
    path('documentType/create', views.createTipoDocumento, name = "addDocument"),
    path('documentType/delete/<id>', views.deleteTipoDocumento, name = "deletDocument"),
    path('documentType/edit/<id>', views.editTipoDocumento, name = "editDocument"),
    path('documentType/modify/<id>', views.modifyTipoDocumento, name = "modifyDocument"),
    path('documentType/view/<id>', views.viewTipoDocumento, name = "viewTypeDocument"),
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
    path('logout/', views.logoutUser, name="logout"),




    
    path('documentTypeORI/form', views.registerTipoDocumentoORI, name = "addDocumentsORI"),
    path('documentTypeORI/', views.listTipoDocumentoORI, name = "listDocumentsORI"),
    path('documentTypeORI/create', views.createTipoDocumentoORI, name = "addDocumentORI"),
    path('documentTypeORI/delete/<id>', views.deleteTipoDocumentoORI, name = "deletDocumentORI"),
    path('documentTypeORI/edit/<id>', views.editTipoDocumentoORI, name = "editDocumentORI"),
    path('documentTypeORI/modify/<id>', views.modifyTipoDocumentoORI, name = "modifyDocumentORI"),
    path('documentTypeORI/view/<id>', views.viewTipoDocumentoORI, name = "viewTypeDocumentORI"),



    path('mAreasORI/form', views.registerMAreasORI, name = "addMAreasORI"),
    path('mAreasORI/', views.listMAreasORI, name = "listMAreasORI"),
    path('mAreasORI/create', views.createMAreasORI, name = "addMFactor"),
    path('mAreasORI/delete/<id>', views.deleteMAreasORI, name = "deletMAreaORI"),
    path('mAreasORI/edit/<id>', views.editMAreasORI, name = "editMAreaORI"),
    path('mAreasORI/modify/<id>', views.modifyMAreasORI, name = "modifyMAreaORI"),
    path('mAreasORI/view/<id>', views.viewMAreasORI, name = "viewTypeMAreaORI"),


    
    path('mFactor/form', views.registerMFactor, name = "addMFactor"),
    path('mFactor/', views.listMFactor, name = "listMFactor"),
    path('mFactor/create', views.createMFactor, name = "addMFactor"),
    path('mFactor/delete/<id>', views.deleteMFactor, name = "deletMFactor"),
    path('mFactor/edit/<id>', views.editMFactor, name = "editMFactor"),
    path('mFactor/modify/<id>', views.modifyMFactor, name = "modifyMFactor"),
    path('mFactor/view/<id>', views.viewMFactor, name = "viewTypeMFactor"),




    path('mUserRol/form', views.registerMUserRol, name = "addmUserRol"),
    path('mUserRol/', views.listMUserRol, name = "listmUserRol"),
    path('mUserRol/create', views.createMUserRol, name = "addmUserRol"),
    path('mUserRol/delete/<id>', views.deleteMUserRol, name = "deletmUserRol"),
    path('mUserRol/edit/<id>', views.editMUserRol, name = "editmUserRol"),
    path('mUserRol/modify/<id>', views.modifyMUserRol, name = "modifymUserRol"),
    path('mUserRol/view/<id>', views.viewMUserRol, name = "viewTypemUserRol"),



    
    path('mUserRol/form', views.registerMUserRol, name = "addmUserRol"),
    path('mUserRol/', views.listMUserRol, name = "listmUserRol"),
    path('mUserRol/create', views.createMUserRol, name = "addmUserRol"),
    path('mUserRol/delete/<id>', views.deleteMUserRol, name = "deletmUserRol"),
    path('mUserRol/edit/<id>', views.editMUserRol, name = "editmUserRol"),
    path('mUserRol/modify/<id>', views.modifyMUserRol, name = "modifymUserRol"),
    path('mUserRol/view/<id>', views.viewMUserRol, name = "viewTypemUserRol"),


    path('mUser/form', views.registerMUser, name = "addmUser"),
    path('mUser/', views.listMUser, name = "listmUser"),
    path('mUser/create', views.createMUser, name = "addmUser"),
    path('mUser/delete/<id>', views.deleteMUser, name = "deletmUser"),
    path('mUser/edit/<id>', views.editMUser, name = "editmUser"),
    path('mUser/modify/<id>', views.modifyMUser, name = "modifymUser"),
    path('mUser/view/<id>', views.viewMUser, name = "viewTypemUser"),




    path('iPersona/form', views.registerIPersona, name = "addiPersona"),
    path('iPersona/', views.listIPersona, name = "listiPersona"),
    path('iPersona/create', views.createIPersona, name = "addiPersona"),
    path('iPersona/delete/<id>', views.deleteIPersona, name = "deletiPersona"),
    path('iPersona/edit/<id>', views.editIPersona, name = "editiPersona"),
    path('iPersona/modify/<id>', views.modifyIPersona, name = "modifyiPersona"),
    path('iPersona/view/<id>', views.viewIPersona, name = "viewTypeiPersona"),
    path('ajax_province/', views.load_province, name='ajax_province'),
    path('ajax_cities/', views.load_cities, name="ajax_cities"),
    path('iPersona/generarpdf/', views.generarpdf, name="generar_pdf"),
    path('iPersona/search', views.searchIPersona, name = "searchiPersona"),


    path('rPenales/<str:pk>/', views.listRPenales, name = "listRPenales"),
    path('rPenales/create/<str:pk>/', views.createRPenales, name = "createRPenales"),
    path('rPenales/edit/<str:pk>/', views.updateRPenales, name = "updateRPenales"),
    path('rPenales/delete/<str:pk>/', views.deleteRPenales, name = "deleteRPenales"),
    path('rPenales/view/<str:pk>/', views.viewRPenales, name = "viewRPenales"),
    path('registropenal_ajax/', views.getRPenalesData, name="registropenal_ajax"),
    path('rPenales/', views.listAllRPenales, name = "listAllRPenales"),

    path('rFamiliares/<str:pk>/', views.listRFamiliares, name = "listRFamiliares"),
    path('rFamiliares/create/<str:pk>/', views.createRFamiliares, name = "createRFamiliares"),
    path('rFamiliares/edit/<str:pk>/', views.updateRFamiliares, name = "updateRFamiliares"),
    path('rFamiliares/delete/<str:pk>/', views.deleteRFamiliares, name = "deleteRFamiliares"),
    path('rFamiliares/view/<str:pk>/', views.viewRFamiliares, name = "viewRFamiliares"),
    path('registrofamiliar_ajax/', views.getRFamiliaresData, name="registrofamiliar_ajax"),
    path('rFamiliares/', views.listAllRFamiliares, name = "listAllRFamiliares"),


    path('rPenales/<str:pk>/view/<str:pk2>/', views.viewTest, name = "viewTest"),

    path('iFFAA/<str:pk>/', views.listIFFAA, name = "listIFFAA"),
    path('iFFAA/create/<str:pk>/', views.createIFFAA, name = "createIFFAA"),
    path('iFFAA/edit/<str:pk>/', views.updateIFFAA, name = "updateIFFAA"),
    path('iFFAA/delete/<str:pk>/', views.deleteIFFAA, name = "deleteIFFAA"),
    path('iFFAA/view/<str:pk>/', views.viewIFFAA, name = "viewIFFAA"),
    path('registroiFFAA_ajax/', views.getRIFFAA, name="registroIFFAA_ajax"),
    path('iFFAA/', views.listAllIFFAA, name = "listAllIFFAA"),

    path('Msitpolicial/', views.listMsitpolicial, name = "listMsitpolicial"),
    path('Msitpolicial/create/', views.createMsitpolicial, name = "createMsitpolicial"),
    path('Msitpolicial/edit/<str:pk>/', views.updateMsitpolicial, name = "updateMsitpolicial"),
    path('Msitpolicial/delete/<str:pk>/', views.deleteMsitpolicial, name = "deleteMsitpolicial"),
    path('Msitpolicial/view/<str:pk>/', views.viewMsitpolicial, name = "viewMsitpolicial"),

    path('Ipolicia/<str:pk>/', views.listIpolicia, name = "listIpolicia"),
    path('Ipolicia/create/<str:pk>/', views.createIpolicia, name = "createIpolicia"),
    path('Ipolicia/edit/<str:pk>/', views.updateIpolicia, name = "updateIpolicia"),
    path('Ipolicia/delete/<str:pk>/', views.deleteIpolicia, name = "deleteIpolicia"),
    path('Ipolicia/view/<str:pk>/', views.viewIpolicia, name = "viewIpolicia"),
    path('registroiPNP_ajax/', views.getRIPNP, name="registroIPNP_ajax"),
    path('Ipolicia/', views.listAllIpolicia, name = "listAllIpolicia"),

    path('Rfiliacionpolitica/<str:pk>/', views.listRfiliacionpolitica, name = "listRfiliacionpolitica"),
    path('Rfiliacionpolitica/create/<str:pk>/', views.createRfiliacionpolitica, name = "createRfiliacionpolitica"),
    path('Rfiliacionpolitica/edit/<str:pk>/', views.updateRfiliacionpolitica, name = "updateRfiliacionpolitica"),
    path('Rfiliacionpolitica/delete/<str:pk>/', views.deleteRfiliacionpolitica, name = "deleteRfiliacionpolitica"),
    path('Rfiliacionpolitica/view/<str:pk>/', views.viewRfiliacionpolitica, name = "viewRfiliacionpolitica"),
    path('registroiFiliacion_ajax/', views.getFiliacion, name="registroFiliacion_ajax"),
    path('Rfiliacionpolitica/', views.listAllRfiliacionpolitica, name = "listAllRfiliacionpolitica"),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)      

