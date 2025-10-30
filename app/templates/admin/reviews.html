@extends('layout.admin')

@section('content')
<div class="container admin-section">
    <h2 class="mb-4">Customer Reviews 🐾</h2>

    @if (session('success'))
        <div class="alert alert-success">
            {{ session('success') }}
        </div>
    @endif

    @if (session('error'))
        <div class="alert alert-danger">
            {{ session('error') }}
        </div>
    @endif

    @if ($reviews->isEmpty())
        <p>No reviews available.</p>
    @else
        <div class="table-responsive">
            <table class="table table-striped table-hover table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Product</th>
                        <th>User</th>
                        <th>Rating</th>
                        <th>Comment</th>
                        <th>Date</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach ($reviews as $review)
                        <tr>
                            <td>{{ $loop->iteration }}</td>
                            <td>{{ $review->product_name }}</td>
                            <td>{{ $review->user_name }}</td>
                            <td>{{ str_repeat('⭐', $review->rating) }}</td>
                            <td>{{ $review->comment }}</td>
                            <td>{{ date('M d, Y', strtotime($review->created_at)) }}</td>
                            <td>
                                <form action="{{ route('admin.reviews.delete', $review->id) }}" method="POST" onsubmit="return confirm('Are you sure you want to delete this review?');">
                                    @csrf
                                    <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                                </form>
                            </td>
                        </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    @endif
</div>

<style>
    /* Custom styles for the table */
    .table th, .table td {
        vertical-align: middle; /* Center-align content vertically */
        padding: 12px; /* Add padding for better spacing */
        text-align: left; /* Align text to the left */
    }

    /* Define column widths */
    .table th:nth-child(1), .table td:nth-child(1) { /* # */
        width: 5%;
    }
    .table th:nth-child(2), .table td:nth-child(2) { /* Product */
        width: 20%;
    }
    .table th:nth-child(3), .table td:nth-child(3) { /* User */
        width: 15%;
    }
    .table th:nth-child(4), .table td:nth-child(4) { /* Rating */
        width: 15%;
    }
    .table th:nth-child(5), .table td:nth-child(5) { /* Comment */
        width: 25%;
    }
    .table th:nth-child(6), .table td:nth-child(6) { /* Date */
        width: 10%;
    }
    .table th:nth-child(7), .table td:nth-child(7) { /* Action */
        width: 10%;
        text-align: center; /* Center the Delete button */
    }

    /* Ensure comments wrap if they're too long */
    .table td:nth-child(5) {
        word-wrap: break-word;
        white-space: normal;
    }

    /* Style the Delete button */
    .btn-sm {
        padding: 5px 10px;
        font-size: 0.875rem;
    }

    /* Add some spacing to the table */
    .table {
        background-color: #fff; /* White background for the table */
        border-radius: 8px; /* Rounded corners */
        overflow: hidden; /* Ensure rounded corners are visible */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
</style>
@endsection
