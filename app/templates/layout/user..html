<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Wagging Wonders</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f6f6f6;
        }

        .navbar {
            background-color: #6B705C;
        }

        .navbar-nav .nav-link {
            color: white !important;
            font-weight: 500;
        }

        .logo-text {
            color: white;
            font-weight: 600;
            font-size: 1.2rem;
        }

        .nav-link i {
            margin-right: 5px;
        }

        .nav-item .category-link {
            background-color: #5A604D;
            border: 2px solid transparent;
            border-radius: 8px;
            padding: 8px 16px;
            transition: border-color 0.3s ease;
        }

        .nav-item .category-link:hover {
            background-color: #CB997E;
        }

        .nav-item .category-link.active {
            background-color: #CB997E;
        }

        .card.active {
            border: 3px solid #CB997E;
            box-shadow: 0 0 10px rgba(90, 144, 210, 0.3);
        }

        .offcanvas-end {
            width: 50% !important;
        }

        .offcanvas-header {
            background-color: #6B705C;
            color: white;
        }

        .offcanvas-body {
            background-color: #f6f6f6;
        }

        .cart-item {
            border-bottom: 1px solid #ddd;
            padding: 10px 0;
        }

        .cart-item img {
            max-height: 80px;
            object-fit: contain;
        }

        .cart-total {
            font-size: 1.2rem;
            color: #CB997E;
            font-weight: 500;
        }

        /* Custom Styles for Cart Sidebar and Items */
        .card {
            margin-bottom: 1rem;
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 10px;
        }

        .card-body {
            padding: 10px;
        }

        .card .btn-outline-secondary {
            border-radius: 0.375rem;
            padding: 5px 10px;
        }

        .card .btn-danger {
            background-color: #D9534F;
            color: white;
            font-size: 12px;
            border-radius: 0.375rem;
        }

        .card .btn-danger:hover {
            background-color: #C9302C;
        }

        .input-group {
            max-width: 160px;
        }

        .input-group .form-control {
            border-radius: 0.375rem;
            font-size: 14px;
            text-align: center;
        }

        .input-group .btn {
            background-color: #6B705C;
            /* Site's theme color */
            color: white;
            font-size: 14px;
            border-radius: 0.375rem;
            padding: 5px 10px;
        }

        .input-group .btn:hover {
            background-color: #CB997E;
            /* Lighter theme color */
        }

        .cart-item {
            margin-bottom: 15px;
        }

        /* Styling for Sidebar Buttons */
        #remove-selected {
            background-color: #f5f5f5;
            border: 2px solid #6B705C;
            color: #6B705C;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 0.375rem;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            width: 100%;
            margin-top: 10px;
            display: none;
        }

        #buy-selected {
            background-color: #6B705C;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 0.375rem;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            width: 100%;
            margin-top: 10px;
            display: none;
        }

        /* Hover effect for Remove and Buy buttons */
        #remove-selected:hover {
            background-color: #5A604D;
            color: white;
            box-shadow: 0 4px 8px rgba(107, 112, 92, 0.3);
        }

        #buy-selected:hover {
            background-color: #CB997E;
            box-shadow: 0 4px 8px rgba(107, 112, 92, 0.3);
        }

        /* Proper spacing between the two buttons */
        .offcanvas-footer {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            /* Gap between buttons */
            justify-content: center;
        }

        /* Add some space between buttons in the footer */
        .offcanvas-footer button {
            flex: 1;
        }
    </style>
</head>

<body>

    <nav class="navbar navbar-expand-lg px-4">
        <div class="me-auto">
            <ul class="navbar-nav d-flex flex-row gap-3">
                <li class="nav-item">
                    <a class="nav-link category-link {{ request()->is('user/products/cat') ? 'active' : '' }}"
                        href="/user/products/cat">Cat Essentials</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link category-link {{ request()->is('user/products/dog') ? 'active' : '' }}"
                        href="/user/products/dog">Dog Essentials</a>
                </li>
            </ul>
        </div>
        <a class="navbar-brand mx-auto d-flex align-items-center" href="/">
            <span class="logo-text">Wagging Wonders</span>
        </a>
        <div class="ms-auto">
            <ul class="navbar-nav d-flex flex-row gap-3">
                @if (session('user_id') && session('role') === 'user')
                    <li class="nav-item">
                        <a href="#" class="nav-link" data-bs-toggle="offcanvas" data-bs-target="#cartSidebar"
                            aria-controls="cartSidebar">
                            🛒 Cart <span id="cart-count" class="badge bg-danger">
                                {{ session('user_id') ? DB::table('carts')->where('user_id', session('user_id'))->sum('quantity') : 0 }}
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="profileDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            {{ session('name') }}
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="profileDropdown">
                            <li><a class="dropdown-item" href="#" data-bs-toggle="offcanvas"
                                    data-bs-target="#ordersSidebar">My Orders</a></li>
                            <li><a class="dropdown-item" href="#" data-bs-toggle="offcanvas"
                                    data-bs-target="#historySidebar">My History</a></li>
                            <li><a class="dropdown-item" href="#" data-bs-toggle="offcanvas"
                                    data-bs-target="#reviewsSidebar">My Reviews</a></li>
                        </ul>
                    </li>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/logout">
                            <i class="bi bi-box-arrow-right"></i> Logout
                        </a>
                    </li>
                @else
                    <li class="nav-item">
                        <a class="nav-link" href="/login">
                            <i class="bi bi-box-arrow-in-right"></i> Login
                        </a>
                    </li>
                @endif
            </ul>
        </div>
    </nav>

    <!-- Cart Sidebar (Offcanvas) -->
    <div class="offcanvas offcanvas-end" tabindex="-1" id="cartSidebar" aria-labelledby="cartSidebarLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="cartSidebarLabel">Your Cart</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                aria-label="Close"></button>
        </div>
        <div class="offcanvas-body" id="cart-items">
            <!-- Cart items will be dynamically loaded here -->
        </div>
        <div class="offcanvas-footer">
            <!-- Buttons for selected items -->
            <button class="btn" id="remove-selected">Remove Selected</button>
            <button class="btn" id="buy-selected">Buy Selected</button>
        </div>
    </div>


    <!-- Order Confirmation Modal -->
<div class="modal fade" id="orderModal" tabindex="-1" aria-labelledby="orderModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered">
        <div class="modal-content" style="border-radius: 1rem; background-color: #f6f6f6;">
            <div class="modal-header" style="background-color: #6B705C; color: white; border-top-left-radius: 1rem; border-top-right-radius: 1rem;">
                <h5 class="modal-title" id="orderModalLabel">🧾 Order Confirmation</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <h5 class="mb-3" style="color: #5A604D; font-weight: bold;">Items to be purchased:</h5>
                <div id="order-details" style="background: white; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <!-- Order items will be dynamically filled here -->
                </div>
                <hr>
                <div class="d-flex justify-content-between align-items-center">
                    <p class="mb-0" style="font-size: 1.25rem; color: #333;"><strong>Total Amount:</strong></p>
                    <p class="mb-0" style="font-size: 1.5rem; color: #CB997E;"><strong>₱<span id="total-price">0</span></strong></p>
                </div>
                <p class="mt-2" style="color: #6B705C;"><strong>Payment Method:</strong> Cash on Delivery</p>
            </div>
            <div class="modal-footer" style="background-color: #FCFCFC; border-bottom-left-radius: 1rem; border-bottom-right-radius: 1rem;">
                <button type="button" class="btn btn-outline-secondary px-4 py-2" data-bs-dismiss="modal" style="border-radius: 0.5rem;">Cancel</button>
                <button type="button" class="btn px-4 py-2" id="confirmOrder" style="background-color: #CB997E; color: white; border-radius: 0.5rem;">Place Order</button>
            </div>
        </div>
    </div>
</div>



    <div class="offcanvas offcanvas-end" tabindex="-1" id="ordersSidebar" aria-labelledby="ordersSidebarLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="ordersSidebarLabel">My Orders</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <!-- Order details will be loaded here dynamically -->
            <div id="my-orders">
                <!-- Ongoing and completed orders -->
            </div>
        </div>
    </div>

    <!-- History Sidebar -->
    <div class="offcanvas offcanvas-end" tabindex="-1" id="historySidebar" aria-labelledby="historySidebarLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="historySidebarLabel">My History</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <div id="my-history">
                <!-- Completed orders will be loaded here dynamically -->
            </div>
        </div>
    </div>

    <!-- Reviews Sidebar -->
    <div class="offcanvas offcanvas-end" tabindex="-1" id="reviewsSidebar" aria-labelledby="reviewsSidebarLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="reviewsSidebarLabel">My Reviews</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <div id="my-reviews">
                <!-- Reviews will be loaded here dynamically -->
            </div>
        </div>
    </div>





    <main class="py-4">
        @yield('content')
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    @yield('scripts')

</body>

</html>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Load Cart Items (already present)
        function loadCartItems() {
    $.ajax({
        url: '/cart/items',
        method: 'GET',
        success: function(response) {
            const cartItemsContainer = document.getElementById('cart-items');
            let total = 0;
            cartItemsContainer.innerHTML = ''; // 🧽 Clear existing

            if (response.length > 0) {
                response.forEach(item => {
                    total += item.price * item.quantity;
                    cartItemsContainer.innerHTML += `
                        <div class="card mb-3 shadow-sm border-0 rounded" style="max-width: 100%; background-color: #f9f9f9;" id="cart-item-${item.id}">
                            <div class="card-body d-flex justify-content-between">
                                <div class="d-flex flex-column">
                                    <p class="fw-bold mb-1">${item.name}</p>
                                    <p>₱${item.price} x
                                        <div class="input-group" style="max-width: 160px;">
                                            <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, 'decrease')">-</button>
                                            <input type="number" id="quantity-${item.id}" class="form-control text-center" value="${item.quantity}" min="1" onchange="updateQuantityManually(${item.id})">
                                            <button class="btn btn-outline-secondary" type="button" onclick="updateQuantity(${item.id}, 'increase')">+</button>
                                        </div>
                                    </p>
                                </div>
                                <div class="d-flex align-items-center">
                                    <input type="checkbox" id="select-item-${item.id}" class="select-item" data-id="${item.id}" onclick="toggleSelection()">
                                </div>
                            </div>
                        </div>
                    `;
                });
                cartItemsContainer.innerHTML += `<p class="fw-bold mt-3">Total: ₱${total}</p>`;
            } else {
                cartItemsContainer.innerHTML = `<p>Your cart is empty</p>`;
            }
        }
    });
}

        // Preload all sidebar data on page load
        loadCartItems();
        loadMyOrders();
        loadMyHistory();
        loadMyReviews();

        // Handle remove selected items
        document.getElementById('remove-selected').addEventListener('click', function() {
            const selectedItems = getSelectedItems();
            if (selectedItems.length > 0) {
                $.ajax({
                    url: '/cart/remove-selected',
                    method: 'POST',
                    data: {
                        _token: '{{ csrf_token() }}',
                        selected_items: selectedItems
                    },
                    success: function(response) {
                        alert('Selected items removed successfully');
                        location.reload(); // Reload cart items
                    },
                    error: function() {
                        alert('Failed to remove selected items');
                    }
                });
            } else {
                alert('Please select items to remove.');
            }
        });

        // Handle buy selected items - Show modal first
        document.getElementById('buy-selected').addEventListener('click', function() {
            const selectedItems = getSelectedItems();
            if (selectedItems.length > 0) {
                $.ajax({
                    url: '/cart/items',
                    method: 'GET',
                    success: function(response) {
                        let total = 0;
                        let orderDetailsHTML = '';
                        const itemsToBuy = response.filter(item => selectedItems.includes(item.id.toString()));

                        if (itemsToBuy.length === 0) {
                            alert('No items selected.');
                            return;
                        }

                        itemsToBuy.forEach(item => {
                            const subtotal = item.price * item.quantity;
                            total += subtotal;
                            orderDetailsHTML += `
                            <p>${item.name} - Quantity: ${item.quantity} - Subtotal: ₱${subtotal.toFixed(2)}</p>
                        `;
                        });

                        // Populate modal
                        document.getElementById('order-details').innerHTML = orderDetailsHTML;
                        document.getElementById('total-price').textContent = total.toFixed(2);

                        // Show modal
                        const orderModal = new bootstrap.Modal(document.getElementById('orderModal'));
                        orderModal.show();

                        // Handle order confirmation
                        document.getElementById('confirmOrder').onclick = function() {
                            confirmOrder(itemsToBuy.map(item => ({
                                product_id: item.product_id,
                                quantity: item.quantity
                            })), orderModal);
                        };
                    },
                    error: function() {
                        alert('Failed to fetch cart items.');
                    }
                });
            } else {
                alert('Please select items to buy.');
            }
        });
    });

    // Toggle visibility of buttons when items are selected/deselected
    function toggleSelection() {
        const selectedItems = getSelectedItems();
        const removeButton = document.getElementById('remove-selected');
        const buyButton = document.getElementById('buy-selected');

        if (selectedItems.length > 0) {
            removeButton.style.display = 'block';
            buyButton.style.display = 'block';
        } else {
            removeButton.style.display = 'none';
            buyButton.style.display = 'none';
        }
    }

    // Get selected items' IDs
    function getSelectedItems() {
        const selectedItems = [];
        document.querySelectorAll('.select-item:checked').forEach(item => {
            selectedItems.push(item.getAttribute('data-id'));
        });
        return selectedItems;
    }

    function updateQuantity(id, action) {
        const quantityElement = document.getElementById('quantity-' + id);
        let quantity = parseInt(quantityElement.value);

        if (action === 'increase') {
            quantity += 1;
        } else if (action === 'decrease') {
            quantity -= 1;
        }

        if (quantity < 1) {
            quantity = 1;
        }

        quantityElement.value = quantity;

        $.ajax({
            url: `/cart/update/${id}`,
            method: 'POST',
            data: {
                _token: '{{ csrf_token() }}',
                quantity: quantity
            },
            success: function(response) {
                alert('Cart updated successfully!');
                location.reload();
            },
            error: function(xhr) {
                alert('Failed to update the quantity');
            }
        });
    }

    function updateQuantityManually(id) {
        const quantityElement = document.getElementById('quantity-' + id);
        let quantity = parseInt(quantityElement.value);

        if (quantity < 1) {
            quantity = 1;
        }

        quantityElement.value = quantity;

        $.ajax({
            url: `/cart/update/${id}`,
            method: 'POST',
            data: {
                _token: '{{ csrf_token() }}',
                quantity: quantity
            },
            success: function(response) {
                alert('Cart updated successfully!');
                location.reload();
            },
            error: function(xhr) {
                alert('Failed to update the quantity');
            }
        });
    }

    function showOrderConfirmationModal(productId) {
    const quantity = document.getElementById('quantity' + productId).value;
    const totalElement = document.getElementById('total' + productId).textContent;
    const productName = document.querySelector(`#productModal${productId} .modal-title`).textContent;

    // Close the product modal first
    const productModalInstance = bootstrap.Modal.getInstance(document.getElementById('productModal' + productId));
    productModalInstance.hide();

    setTimeout(() => {
        // Populate order details
        const orderDetails = document.getElementById('order-details');
        orderDetails.innerHTML = `<p>${productName} - Quantity: ${quantity}</p>`;

        document.getElementById('total-price').textContent = totalElement.replace('₱', '');

        // Show the order confirmation modal
        const orderModal = new bootstrap.Modal(document.getElementById('orderModal'));
        orderModal.show();

        // Confirm button action
        document.getElementById('confirmOrder').onclick = function() {
            confirmOrder([{ product_id: productId, quantity: quantity }], orderModal);
        };
    }, 300); // Wait for product modal to close
}


    function confirmOrder(items, modal) {
        $.ajax({
            url: '/order/create',
            method: 'POST',
            data: {
                _token: '{{ csrf_token() }}',
                items: items
            },
            success: function(response) {
                modal.hide();
                let message = 'Order placed successfully! Please go to your profile to track your order.';
                if (response.message) {
                    message += '\n' + response.message;
                }
                alert(message);
                location.reload();
            },
            error: function(xhr) {
                alert('Failed to place order: ' + (xhr.responseJSON?.message || 'Unknown error'));
            }
        });
    }

    // Function to load My Orders
    function loadMyOrders() {
        $.ajax({
            url: '/orders/active',
            method: 'GET',
            success: function(response) {
                const ordersContainer = document.getElementById('my-orders');
                ordersContainer.innerHTML = '';
                if (response.length > 0) {
                    response.forEach(order => {
                        ordersContainer.innerHTML += `
                        <div class="card mb-3">
                            <div class="card-body">
                                <h6>Order #${order.id} - ${order.status}</h6>
                                <p>Total: ₱${order.total_price}</p>
                                <button class="btn btn-success btn-sm" onclick="markAsReceived(${order.id})">Mark as Received</button>
                            </div>
                        </div>
                    `;
                    });
                } else {
                    ordersContainer.innerHTML = '<p>No ongoing orders.</p>';
                }
            },
            error: function() {
                document.getElementById('my-orders').innerHTML = '<p class="text-danger">Failed to load orders.</p>';
            }
        });
    }

    // Function to mark order as received
    function markAsReceived(orderId) {
        $.ajax({
            url: `/orders/update/${orderId}`,
            method: 'POST',
            data: {
                _token: '{{ csrf_token() }}',
                status: 'received'
            },
            success: function(response) {
                alert('Order marked as received!');
                location.reload();
            },
            error: function(xhr) {
                alert('Failed to mark as received: ' + (xhr.responseJSON?.message || 'Unknown error'));
            }
        });
    }

    // Function to load My History
    function loadMyHistory() {
        $.ajax({
            url: '/orders/history',
            method: 'GET',
            success: function(response) {
                const historyContainer = document.getElementById('my-history');
                historyContainer.innerHTML = '';

                if (response.length > 0) {
                    response.forEach(order => {
                        let productsHTML = '';

                        order.products.forEach(product => {
                            let reviewButton = '';
                            if (order.status === 'received' || order.status === 'completed') {
                                const buttonText = product.review_exists ? 'View Review' : 'Review';
                                reviewButton = `
                                <button class="btn btn-primary review-btn" data-order-id="${order.id}" data-product-id="${product.product_id}">
                                    ${buttonText}
                                </button>
                            `;
                            }

                            productsHTML += `
                            <div>
                                <p>${product.name} - ₱${product.price}</p>
                                ${reviewButton}
                            </div>
                        `;
                        });

                        historyContainer.innerHTML += `
                        <div class="card mb-3">
                            <div class="card-body">
                                <h6>Order #${order.id} - ${order.status}</h6>
                                <p>Total: ₱${order.total_price}</p>
                                ${productsHTML}
                            </div>
                        </div>
                    `;
                    });

                    // Attach click event to the dynamically created review buttons
                    $('.review-btn').off('click').on('click', function() {
                        const productId = $(this).data('product-id');
                        const orderId = $(this).data('order-id');
                        const buttonText = $(this).text().trim();

                        if (buttonText === 'View Review') {
                            const offcanvas = new bootstrap.Offcanvas(document.getElementById('reviewsSidebar'));
                            offcanvas.show();
                        } else {
                            window.location.href = `/review/${productId}/${orderId}`;
                        }
                    });
                } else {
                    historyContainer.innerHTML = '<p>No completed or received orders.</p>';
                }
            },
            error: function() {
                document.getElementById('my-history').innerHTML = '<p class="text-danger">Failed to load history.</p>';
            }
        });
    }

    // Function to load My Reviews
    function loadMyReviews() {
        $.ajax({
            url: '/user/reviews',
            method: 'GET',
            success: function(response) {
                const reviewsContainer = document.getElementById('my-reviews');
                reviewsContainer.innerHTML = '';

                if (response.length > 0) {
                    response.forEach(review => {
                        reviewsContainer.innerHTML += `
                        <div class="card mb-3">
                            <div class="card-body">
                                <h6>${review.product_name}</h6>
                                <p>Rating: ${'⭐'.repeat(review.rating)}</p>
                                <p>${review.comment}</p>
                                <small class="text-muted">${new Date(review.created_at).toLocaleDateString()}</small>
                            </div>
                        </div>
                    `;
                    });
                } else {
                    reviewsContainer.innerHTML = '<p>No reviews yet.</p>';
                }
            },
            error: function() {
                document.getElementById('my-reviews').innerHTML = '<p class="text-danger">Failed to load reviews.</p>';
            }
        });
    }

    // Update click event listeners to simply show the sidebar (data is already loaded)
    document.querySelector('[data-bs-target="#ordersSidebar"]').addEventListener('click', function() {
        // Optionally, you can call loadMyOrders() again to refresh the data
        // loadMyOrders();
    });

    document.querySelector('[data-bs-target="#historySidebar"]').addEventListener('click', function() {
        // Optionally, you can call loadMyHistory() again to refresh the data
        // loadMyHistory();
    });

    document.querySelector('[data-bs-target="#reviewsSidebar"]').addEventListener('click', function() {
        // Optionally, you can call loadMyReviews() again to refresh the data
        // loadMyReviews();
    });
</script>
