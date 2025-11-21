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
                    <td>${p.name}</td>
                    <td>${p.quantity}</td>
                    <td>${p.category || ""}</td>
                    <td>${p.location || ""}</td>
                `;

                tbody.appendChild(row);
            });
        })
        .catch(err => {
            console.error("Błąd pobierania danych:", err);
            tbody.innerHTML = "<tr><td colspan='4'>Błąd ładowania danych</td></tr>";
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
    window.currentItem = null;
    loadItems();
});
