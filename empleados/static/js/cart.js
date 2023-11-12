// Encuentra el botón "Verificar" y el campo de entrada del código de cupón
var verificarBtn = document.getElementById('verificar-cupon');
var cuponCodigoInput = document.getElementById('cupon_codigo');
var updateBtns = document.getElementsByClassName('update-cart')

var descuentoAmount = document.getElementById('descuento-amount');
var totalAnterior = document.getElementById('total-anterior');
var descuentoInfo = document.getElementById('descuento-info');
var totalCarrito = document.getElementById('total-carrito');

console.log(descuentoAmount, totalAnterior, descuentoInfo, totalCarrito);

if (verificarBtn) {
    // Agrega un event listener al botón "Verificar"
    verificarBtn.addEventListener('click', function () {
        var cuponCodigo = cuponCodigoInput.value; // Obtiene el código de cupón ingresado
        console.log('Cupón ingresado en JavaScript:', cuponCodigo); // Registra el código de cupón

        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            verificarCupon(cuponCodigo); // Envía el código de cupón a la función verificarCupon
        }
    });
    cuponCodigoInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            var cuponCodigo = cuponCodigoInput.value;
            if (user === 'AnonymousUser') {
                console.log('Not logged in');
            } else {
                verificarCupon(cuponCodigo);
            }
        }
    });
}
function verificarCupon(cuponCodigo) {
    console.log('Verifying coupon...');

    var url = '/verificar_cupon/'; // Define la URL para verificar el cupón
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'cupon_codigo': cuponCodigo, // Envía el código de cupón
        })
    })

        .then((response) => {
            return response.json();
        })

        // ... (código anterior)

        .then((data) => {
            console.log('Coupon verification result:', data);
            if (data.valid) {
                function ocultarMensaje() {
                    descuentoInfo.style.display = 'none';
                }
                // Mostrar la información del descuento
                var descuentoAmount = document.getElementById('descuento-amount');
                var totalAnterior = document.getElementById('total-anterior');

                descuentoAmount.innerText = '-$' + data.descuento;
                totalAnterior.innerText = '$' + data.total_anterior;

                // Mostrar el elemento de información del descuento
                var descuentoInfo = document.getElementById('descuento-info');
                descuentoInfo.style.display = 'block';

                // Actualiza el total en el carrito (si es necesario)
                var totalCarrito = document.getElementById('total-carrito');
                totalCarrito.innerText = '$' + data.nuevo_total;

                verificarBtn.addEventListener('click', ocultarMensaje);
                cuponCodigoInput.addEventListener('keypress', function(event) {
                    if (event.key === 'Enter') {
                        ocultarMensaje();
                    }
                });
            } else {
                // Mostrar un mensaje de error si el cupón no es válido
                var mensajeInfo = document.getElementById('mensaje-info');
                mensajeInfo.style.display = 'block';
                var mensajeError = document.getElementById('mensaje-error');
                mensajeError.innerText = 'Cupón no válido: ' + data.error;

                setTimeout(function() {
                    mensajeInfo.style.display = 'none';
                }, 2500);
            }
        });


}

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        console.log('Entrando en updateUserOrder');
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User id logged in, sending data...')
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })

}


