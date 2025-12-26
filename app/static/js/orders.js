function loadOrders() {
    const tbody = document.querySelector("#items tbody");
    tbody.innerHTML = "";

    fetch("/v1/orders/")
        .then(response => response.json())
        .then(orders => {
            orders.forEach(o => {
                const row = document.createElement("tr");
                row.dataset.id = o.id;

                row.innerHTML = `
                    <td>${o.customer}</td>
                    <td>${o.address}</td>
                `;

                row.addEventListener("click", () => {
                    showDetails(o.id);
                });

                tbody.appendChild(row);
            });
        })
        .catch(err => {
            console.error("Błąd pobierania danych:", err);
            tbody.innerHTML = "<tr><td colspan='2'>Błąd ładowania danych</td></tr>";
        });
}

function showDetails(orderId) {
    fetch(`/v1/orders/${orderId}`)
        .then(response => response.json())
        .then(order => {
            const detailsPanel = document.getElementById("details");
            
            detailsPanel.querySelector("h2").textContent = `Zamówienie: ${order.customer}, ${order.address} #${order.id}`;

            const tbody = detailsPanel.querySelector("tbody");
            tbody.innerHTML = "";

            order.items.forEach(item => {
                const row = document.createElement("tr");

                if (item.available_quantity < item.quantity) {
                    row.style.backgroundColor = "red";
                    row.style.color = "white";
                }

                row.innerHTML = `
                    <td>${item.product_name}</td>
                    <td>${item.quantity}</td>
                    <td>${item.available_quantity}</td>
                `;

                tbody.appendChild(row);
            });
            detailsPanel.style.display = "block"; 
        })
        .catch(err => {
            console.error("Błąd pobierania szczegółów:", err);
            const tbody = document.querySelector("#details tbody");
            tbody.innerHTML = "<tr><td colspan='2'>Błąd ładowania szczegółów</td></tr>";
        });
}

document.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('#items tbody');

    table.addEventListener('click', (e) => {
        let tr = e.target.closest('tr');
        if (!tr) return;

        table.querySelectorAll('tr').forEach(row => row.classList.remove('selected'));

        tr.classList.add('selected');
    });
});


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
    window.currentItem = null;
    loadOrders();
});
