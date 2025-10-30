@extends('layout.admin')

@section('content')
<div class="container py-4">
    <h2 class="mb-4" style="color: #6B705C;">Edit Product</h2>

    <form action="{{ url('/admin/products/update/' . $product->id) }}" method="POST" enctype="multipart/form-data">

        @csrf

        <div class="mb-3">
            <label for="name" class="form-label">Product Name</label>
            <input type="text" name="name" class="form-control" value="{{ $product->name }}" required>
        </div>

        <div class="mb-3">
            <label class="form-label">Current Image:</label><br>
            @if($product->image)
                <img src="{{ asset('storage/' . $product->image) }}" width="100" class="mb-2">
            @else
                <p>No image uploaded</p>
            @endif
        </div>

        <div class="mb-3">
            <label for="image" class="form-label">Change Image</label>
            <input type="file" name="image" class="form-control">
        </div>


        <div class="mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea name="description" class="form-control" rows="3" required>{{ $product->description }}</textarea>
        </div>

        <div class="mb-3">
            <label for="price" class="form-label">Price (₱)</label>
            <input type="number" name="price" step="0.01" class="form-control" value="{{ $product->price }}" required>
        </div>

        <div class="mb-3">
            <label for="quantity" class="form-label">Quantity</label>
            <input type="number" name="quantity" class="form-control" value="{{ $product->quantity }}" required>
        </div>

        <div class="mb-3">
            <label for="category" class="form-label">Category</label>
            <select name="category" class="form-select" required>
                <option value="">Select Category</option>
                <option value="Dog Food" {{ $product->category === 'Dog Food' ? 'selected' : '' }}>Dog Food</option>
                <option value="Cat Food" {{ $product->category === 'Cat Food' ? 'selected' : '' }}>Cat Food</option>
            </select>
        </div>

        <button type="submit" class="btn btn-primary">Update Product</button>
        <a href="{{ url('/admin/products') }}" class="btn btn-secondary">Cancel</a>
    </form>
</div>
@endsection
