
console.log("caraga correcta del controlador2")
let talla = document.querySelectorAll(".tal");
let peso = document.querySelectorAll(".tal");
let arrow = document.querySelectorAll(".arrow");
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
let btnEliminacion = document.querySelectorAll(".btnEliminacion");
const data = document.querySelectorAll(".table-content");


(function(){

        
    for (var i = 0; i < arrow.length; i++) {
        arrow[i].addEventListener("click", (e)=>{
       let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
       arrowParent.classList.toggle("showMenu");
        });
      }
      sidebarBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("close");
      });

       /* Funtion to resize length of the data  */
       try{
        for (var i=0;i<data.length;i++) {
            if(!data[i].hasChildNodes()){
                continue;
            }      
            console.log(data[i].childNodes[0].nodeValue)
            //if (typeof data[i].children[0].nodeValue !== 'undefined'){
            var textValue = data[i].childNodes[0].nodeValue;
            if (textValue.length>20){
                data[i].childNodes[0].nodeValue = textValue.substr(0, 20)+"...";
            }else{
                data[i].childNodes[0].nodeValue = textValue;
            }
             
        }
       }catch (error) {
       }
   
    /* Function to show an alert to delets */
    

    btnEliminacion.forEach((btn)=>{
        
        btn.addEventListener("click", function(e){
            e.preventDefault();
            Swal.fire({
                title:"¿Confirma la eliminación del elemento?",
                text: "esta acción no se puede deshacer",
                showCancelButton:true,
                icon: "warning",
                confirmButtonText: "Sí, eliminar",
                cancelButtonText: "No, cancelar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm:()=>{
                    //console.log("Redirigiendo hacia: "+this.href)
                    location.href = this.href
                },
                allowOutsideClick:()=>false,
                allowEscapeKey:()=>false,

            })
        })
    })
}
)();





