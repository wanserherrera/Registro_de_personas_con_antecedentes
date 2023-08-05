(function () {
  'use strict'
  console.log("validaciones obtenidas")  
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()



//validacoin de decimales
//https://es.stackoverflow.com/questions/257977/como-validar-un-input-solo-puedan-entrar-decimales#:~:text=Se%20debe%20iniciar%20con%20d%C3%ADgitos,finalizar%20con%20d%C3%ADgitos%20(%20%24%20).