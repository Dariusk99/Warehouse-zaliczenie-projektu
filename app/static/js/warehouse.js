function loadItems() {
    const tbody = document.querySelector("#items tbody");
    tbody.innerHTML = "";

    fetch("/v1/products/")
        .then(response => response.json())
        .then(products => {
            products.forEach(p => {
                const row = document.createElement("tr");

                row.dataset.id = p.id;

                row.innerHTML = `
                    <td>${p.index}</td>
                    <td>${p.name}</td>
                    <td>${p.product_type}</td>
                    <td>${p.quantity}</td>
                    <td>${p.category || ""}</td>
                    <td>${p.location || ""}</td>
                `;

                row.addEventListener("click", () => {
                    showDetails(p.id);
                });

                tbody.appendChild(row);
            });
        })
        .catch(err => {
            console.error("Błąd pobierania danych:", err);
            tbody.innerHTML = "<tr><td colspan='4'>Błąd ładowania danych</td></tr>";
        });
}

function showDetails(productId) {
    fetch(`/v1/products/${productId}`)
        .then(response => response.json())
        .then(product => {
            const htmlContent = `
                <h3>Szczegóły produktu #${product.id}</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Właściwość</th>
                            <th>Wartość</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>Index</td><td>${product.index}</td></tr>
                        <tr><td>Nazwa</td><td>${product.name}</td></tr>
                        <tr><td>Ilość</td><td><input id="edit-quantity" type="number" value=${product.quantity}></td></tr>
                        <tr><td>Lokalizacja</td><td>${product.location}</td></tr>
                        <tr><td>Kategoria</td><td>${product.category}</td></tr>
                        <tr><td>Typ</td><td>${product.product_type}</td></tr>
                    </tbody>
                </table>
                <button id="edit-btn">Edytuj</button>
            `;

            let productModal = new Modal();
            const rightSection = document.querySelector('.right-section');
            rightSection.appendChild(productModal.modalElement);

            productModal.open(htmlContent);

            const editBtn = productModal.modalElement.querySelector("#edit-btn");
            editBtn.addEventListener("click", () => {
                const newQuantity = productModal.modalElement.querySelector("#edit-quantity").value;
                updateProductQuantity(product.id, newQuantity);
            });
        })
        .catch(err => {
            console.error("Błąd pobierania szczegółów:", err);
            const errorHtml = `
                <h3>Błąd ładowania danych produktu</h3>
                <p>Wystąpił problem podczas ładowania szczegółów produktu. Spróbuj ponownie później.</p>
            `;
            let errorModal = new Modal();
            const rightSection = document.querySelector('.right-section');
            rightSection.appendChild(errorModal.modalElement);
            errorModal.open(errorHtml);
        });
}

function updateProductQuantity(productId, newQuantity) {
    fetch(`/v1/products/${productId}/${newQuantity}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(response => response.json())
    .then(updatedProduct => {
        alert("Ilość została zaktualizowana!");
        window.location.reload();
    })
    .catch(err => {
        console.error("Błąd aktualizacji:", err);
        alert("Nie udało się zaktualizować produktu.");
    });
}

function filterTable() {
    const table = document.getElementById("items");
    const trs = table.querySelectorAll("tbody tr");
    const inputs = table.querySelectorAll("thead input.search");

    trs.forEach(tr => {
        let show = true;
        inputs.forEach(input => {
            const colIndex = input.dataset.column;
            const value = input.value.toLowerCase();
            const cellText = tr.cells[colIndex].textContent.toLowerCase();
            if (!cellText.includes(value)) {
                show = false;
            }
        });
        tr.style.display = show ? "" : "none";
    });
}

document.querySelectorAll("#items thead input.search").forEach(input => {
    input.addEventListener("input", filterTable);
});

window.addEventListener("DOMContentLoaded", () => {
    loadItems();
});
