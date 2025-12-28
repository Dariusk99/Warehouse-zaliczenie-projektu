function getCart() {
    const match = document.cookie.match(new RegExp('(^| )cart=([^;]+)'));
    return match ? JSON.parse(decodeURIComponent(match[2])) : [];
}

function saveCart(cart) {
    document.cookie =
        'cart=' + encodeURIComponent(JSON.stringify(cart)) +
        '; path=/; max-age=604800';
}

function addToCart(product) {
    let cart = getCart();

    const existing = cart.find(p => p.product_id === product.id);

    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({
            product_id: product.id,
            product_name: product.name,
            quantity: 1
        });
    }

    saveCart(cart);
    return cart;
}

function removeFromCart(productId) {
    let cart = getCart().filter(p => p.product.id !== productId);
    saveCart(cart);
    return cart;
}

function clearCart() {
    saveCart([]);
}
