@extends('layout.admin')

@section('content')
<div class="container py-4">
    <h2 class="mb-4" style="color: #6B705C;">Product Management</h2>

    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif

    <div class="d-flex justify-content-between mb-3">
        <a href="/admin/products/create" class="btn btn-success" style="background-color: #6B705C; border: none;">
            + Add New Product
        </a>
    </div>

    {{-- DOG FOOD --}}
    <h4 class="mt-4 mb-3">🐶 Dog Food</h4>
    <div class="table-responsive mb-5">
        <table class="table table-bordered table-hover align-middle">
            <thead class="table-light text-center">
                <tr>
                    <th>Name</th>
                    <th>Image</th>
                    <th>Description</th>
                    <th>Price (₱)</th>
                    <th>Quantity</th>
                    <th style="width: 150px;">Actions</th>
                </tr>
            </thead>
            <tbody>
            @php
                $dogFoods = $products->where('category', 'Dog Food');
            @endphp

            @forelse($dogFoods as $product)
                <tr>
                    <td class="fw-semibold">{{ $product->name }}</td>
                    <td>
                        @if($product->image)
                            <img src="{{ asset('storage/' . $product->image) }}" width="60">
                        @else
                            <span class="text-muted">No image</span>
                        @endif
                    </td>

                    <td>{{ $product->description }}</td>
                    <td class="text-center">₱{{ number_format($product->price, 2) }}</td>
                    <td class="text-center">{{ $product->quantity }}</td>
                    <td class="text-center">
                        <a href="/admin/products/edit/{{ $product->id }}" class="btn btn-sm btn-warning mb-1">Edit</a>
                        <a href="/admin/products/delete/{{ $product->id }}"
                           class="btn btn-sm btn-danger mb-1"
                           onclick="return confirm('Are you sure you want to delete this product?')">
                            Delete
                        </a>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="5" class="text-center text-muted">No dog food products yet.</td>
                </tr>
            @endforelse
            </tbody>
        </table>
    </div>

    {{-- CAT FOOD --}}
    <h4 class="mb-3">🐱 Cat Food</h4>
    <div class="table-responsive">
        <table class="table table-bordered table-hover align-middle">
            <thead class="table-light text-center">
                <tr>
                    <th>Name</th>
                    <th>Image</th>
                    <th>Description</th>
                    <th>Price (₱)</th>
                    <th>Quantity</th>
                    <th style="width: 150px;">Actions</th>
                </tr>
            </thead>
            <tbody>
            @php
                $catFoods = $products->where('category', 'Cat Food');
            @endphp

            @forelse($catFoods as $product)
                <tr>
                    <td class="fw-semibold">{{ $product->name }}</td>
                    <td>
                        @if($product->image)
                            <img src="{{ asset('storage/' . $product->image) }}" width="60">
                        @else
                            <span class="text-muted">No image</span>
                        @endif
                    </td>

                    <td>{{ $product->description }}</td>
                    <td class="text-center">₱{{ number_format($product->price, 2) }}</td>
                    <td class="text-center">{{ $product->quantity }}</td>
                    <td class="text-center">
                        <a href="/admin/products/edit/{{ $product->id }}" class="btn btn-sm btn-warning mb-1">Edit</a>
                        <a href="/admin/products/delete/{{ $product->id }}"
                           class="btn btn-sm btn-danger mb-1"
                           onclick="return confirm('Are you sure you want to delete this product?')">
                            Delete
                        </a>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="5" class="text-center text-muted">No cat food products yet.</td>
                </tr>
            @endforelse
            </tbody>
        </table>
    </div>
</div>
@endsection
