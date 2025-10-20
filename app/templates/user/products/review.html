@extends('layout.user')

@section('content')
<div class="container py-5">
    <div class="card p-4 shadow-sm">
        <h3 class="mb-4 text-center">Review Product</h3>

        <h5 class="mb-3">{{ $product->name }}</h5>

        @if(session('error'))
            <div class="alert alert-danger">
                {{ session('error') }}
            </div>
        @endif

        @if(session('success'))
            <div class="alert alert-success">
                {{ session('success') }}
            </div>
        @endif

        <form method="POST" action="{{ route('review.submit') }}">
            @csrf

            <input type="hidden" name="product_id" value="{{ $product->id }}">
            <input type="hidden" name="order_id" value="{{ $order->id }}">

            <div class="mb-3">
                <label for="rating" class="form-label">Rating</label>
                <select name="rating" class="form-select" required>
                    <option value="">Select Rating</option>
                    @for ($i = 1; $i <= 5; $i++)
                        <option value="{{ $i }}">{{ $i }} Star{{ $i > 1 ? 's' : '' }}</option>
                    @endfor
                </select>
            </div>

            <div class="mb-3">
                <label for="comment" class="form-label">Your Review</label>
                <textarea name="comment" class="form-control" rows="4" placeholder="Write your experience..." required></textarea>
            </div>

            <div class="d-grid gap-2">
                <button type="submit" class="btn btn-success">Submit Review</button>
                <a href="/user" class="btn btn-secondary">Cancel</a>
            </div>
        </form>
    </div>
</div>
@endsection
