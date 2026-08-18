"""
HTTP routes related to bookings.

This layer is only responsible for receiving the request, delegating
to the corresponding service, and shaping the response. It contains
no business logic.
"""

from api.dependencies import get_booking_service
from core.exceptions import TravelHubError
from database.session import get_db
from schemas.booking import BookingCreateRequest, BookingResponse

router = "bookings_router"  # placeholder: in a real project this would be APIRouter()


def create_booking_endpoint(request: BookingCreateRequest) -> BookingResponse:
    """POST /bookings — creates a new booking."""
    service = get_booking_service()
    try:
        booking = service.create_booking(
            user_id=request.user_id,
            destination_id=request.destination_id,
            check_in=request.check_in,
            check_out=request.check_out,
            passengers=request.passengers,
        )
    except TravelHubError as exc:
        return {"error": str(exc)}

    destination = get_db().destinations[booking.destination_id]
    return BookingResponse(
        id=booking.id,
        destination_city=destination.city,
        check_in=booking.check_in,
        check_out=booking.check_out,
        total_price=booking.total_price,
        status=booking.status.value,
    )


def list_user_bookings_endpoint(user_id: int) -> list[BookingResponse]:
    """GET /users/{user_id}/bookings — lists a user's bookings."""
    service = get_booking_service()
    bookings = service.get_user_bookings(user_id)
    db = get_db()
    return [
        BookingResponse(
            id=b.id,
            destination_city=db.destinations[b.destination_id].city,
            check_in=b.check_in,
            check_out=b.check_out,
            total_price=b.total_price,
            status=b.status.value,
        )
        for b in bookings
    ]


def cancel_booking_endpoint(booking_id: int) -> dict:
    """DELETE /bookings/{booking_id} — cancels a booking."""
    service = get_booking_service()
    try:
        booking = service.cancel_booking(booking_id)
        return {"id": booking.id, "status": booking.status.value}
    except TravelHubError as exc:
        return {"error": str(exc)}
