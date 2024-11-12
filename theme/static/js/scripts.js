// scripts.js

let orderSummary = {};

function increment(chaiId) {
    const quantityInput = document.getElementById(`quantity-${chaiId}`);
    let quantity = parseInt(quantityInput.value);
    quantityInput.value = ++quantity;
}

function decrement(chaiId) {
    const quantityInput = document.getElementById(`quantity-${chaiId}`);
    let quantity = parseInt(quantityInput.value);
    if (quantity > 1) {
        quantityInput.value = --quantity;
    }
}

function addToOrder(chaiName, chaiId) {
    const quantity = parseInt(document.getElementById(`quantity-${chaiId}`).value);

    if (orderSummary[chaiId]) {
        orderSummary[chaiId].quantity += quantity;
    } else {
        orderSummary[chaiId] = { name: chaiName, quantity: quantity };
    }

    alert(`Added ${chaiName} (x${quantity}) to order!`);
}

function showOrderSummary() {
    let summaryContent = '';
    for (const [id, item] of Object.entries(orderSummary)) {
        summaryContent += `<p>${item.name} - Quantity: ${item.quantity}</p>`;
    }

    document.getElementById('order-summary-content').innerHTML = summaryContent;
    document.getElementById('order-summary-modal').style.display = 'block';
}

function closeOrderSummary() {
    document.getElementById('order-summary-modal').style.display = 'none';
}
