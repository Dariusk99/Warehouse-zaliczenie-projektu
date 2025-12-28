document.addEventListener('DOMContentLoaded', function () {
    const cart = getCart();
    let itemsHtml = "";

    cart.forEach(item => {
        itemsHtml += `
        <li>
        ${item.product_name} - ${item.quantity}szt.
        </li>
    `;
    });

    const orderList = document.querySelector('#order-list');
    orderList.innerHTML = itemsHtml;
});


function order() {
    const form = document.querySelector("#user-personal-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        const cart = getCart();
        data.products = cart;

        data.products = data.products.map(({ product_id, quantity }) => ({
            product_id,
            quantity
        }));

        fetch('/v1/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(product => {
                alert('Zamówienie złożone');
                clearCart();
                window.location.reload();
            })
            .catch(error => {
                alert('Wystąpił błąd podczas zamawiania');
                console.error(error);
            });
    });
}

document.getElementById("order-btn").addEventListener("click", order);