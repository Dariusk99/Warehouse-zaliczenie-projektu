function openAddItemModal() {

    if (document.querySelector('#add-item-form')) {
        return;
    }

    const htmlContent = `
        <h3>Dodaj nowy przedmiot</h3>
        <form id="add-item-form">
            <table>
                <tr>
                    <td><label for="index">Index:</label></td>
                    <td><input type="text" id="index" name="index" minlength="3" required></td>
                </tr>
                <tr>
                    <td><label for="name">Nazwa:</label></td>
                    <td><input type="text" id="name" name="name" minlength="3" required></td>
                </tr>
                <tr>
                    <td><label for="type">Typ:</label></td>
                    <td>
                        <select id="type" name="product_type" required>
                            <option value="Element">Element</option>
                            <option value="Produkt gotowy">Produkt gotowy</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><label for="quantity">Ilość:</label></td>
                    <td><input type="number" id="quantity" name="quantity" min="0" required></td>
                </tr>
                <tr>
                    <td><label for="category">Kategoria:</label></td>
                    <td><input type="text" id="category" name="category" required></td>
                </tr>
                <tr>
                    <td><label for="location">Lokalizacja:</label></td>
                    <td><input type="text" id="location" name="location" required></td>
                </tr>
                <tr>
                    <td colspan="2" style="text-align:center;">
                        <button type="submit">Zapisz</button>
                    </td>
                </tr>
            </table>
        </form>
    `;

    let addItemModal = new Modal();
    const rightSection = document.querySelector('.right-section');
    rightSection.appendChild(addItemModal.modalElement);

    addItemModal.open(htmlContent);

    const form = addItemModal.modalElement.querySelector("#add-item-form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch('/v1/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(product => {
            alert('Przedmiot został dodany!');
            window.location.reload();
        })
        .catch(error => {
            alert('Wystąpił błąd podczas dodawania przedmiotu!');
            console.error(error);
        });
    });
}

document.getElementById("add-item-btn").addEventListener("click", openAddItemModal);