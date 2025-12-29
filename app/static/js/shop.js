function openLoginModal() {
    if (document.querySelector('.login-modal')) {
        return;
    }

    const htmlContent = `
        <div class="login-modal">
            <h1>Zaloguj</h1>
            <form id="login-form">
                <label for="username">Login:</label>
                <input type="text" id="username" name="username" required><br>

                <label for="password">Hasło:</label>
                <input type="password" id="password" name="password" required><br>
                <button>Zaloguj</button>
            </form>
        </div>
    `

    let loginModal = new Modal();
    const main = document.querySelector('main');
    main.appendChild(loginModal.modalElement);
    loginModal.open(htmlContent);

    const form = document.querySelector('#login-form');
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch("/v1/auth/login", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(user => {
                alert('Zalogowano pomyślnie');
                window.location.reload();
            })
            .catch(error => {
                alert('Problem z zalogowaniem');
                console.error(error);
            });
    })
}

function openRegisterModal() {
    if (document.querySelector('.register-modal')) {
        return;
    }

    const htmlContent = `
        <div class="register-modal">
            <h1>Zarejestruj</h1>
            <form id="register-form">
                <label for="username">Login:</label>
                <input type="text" id="username" name="username" required><br>

                <label for="password">Hasło:</label>
                <input type="password" id="password" name="password" required><br>
                <button>Zarejestruj</button>
            </form>
        </div>
    `

    let registerModal = new Modal();
    const main = document.querySelector('main');
    main.appendChild(registerModal.modalElement);
    registerModal.open(htmlContent);

    const form = document.querySelector('#register-form');
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch("/v1/auth/register", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(user => {
                alert('Użytkownik zarejestrowany pomyślnie');
                window.location.reload();
            })
            .catch(error => {
                alert('Wystąpił błąd podczas rejestracji');
                console.error(error);
            });
    })
}

function openCartModal() {
    if (document.querySelector('.cart-modal')) {
        return;
    }

    const cart = getCart();
    let itemsHtml = "";

    cart.forEach(item => {
    itemsHtml += `
        <li>
        ${item.product_name} - ${item.quantity}szt.
        </li>
    `;
    });

    const htmlContent = `
        <div class="cart-modal">
            <h1>Koszyk</h1>
            <ul>
                ${itemsHtml}
            </ul>
            <a href="/shop/user/orders"><button>Zamów</button></a>
            <button id="clear-cart-btn" onclick="clearCart()">Wyczyść koszyk</button>
        </div>
    `

    let cartModal = new Modal();
    const main = document.querySelector('main');
    main.appendChild(cartModal.modalElement);
    cartModal.open(htmlContent);

}

document.addEventListener("DOMContentLoaded", () => {
    const cartBtn = document.getElementById("cart-btn");
    const loginBtn = document.getElementById("login-btn");
    const registerBtn = document.getElementById("register-btn");
    if (cartBtn) cartBtn.addEventListener("click", openCartModal);
    if (loginBtn) loginBtn.addEventListener("click", openLoginModal);
    if (registerBtn) registerBtn.addEventListener("click", openRegisterModal);
});