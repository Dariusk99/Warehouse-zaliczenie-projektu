document.addEventListener('DOMContentLoaded', function() {
    const list = document.getElementById('product-list');
    const userLoggedIn = list.dataset.user === 'True';
  
    fetch('/v1/products')
      .then(response => response.json())
      .then(data => {
        data.forEach(item => {
          const li = document.createElement('li');
          li.textContent = item.name;
  
          if (userLoggedIn) {
            const btn = document.createElement('button');
            btn.textContent = 'Dodaj do koszyka';
            btn.addEventListener('click', () => {
              console.log(`Dodano ${item.name} do koszyka`);
            });
            li.appendChild(document.createTextNode(' '));
            li.appendChild(btn);
          }
  
          list.appendChild(li);
        });
      })
      .catch(error => console.error(error));
  });
  