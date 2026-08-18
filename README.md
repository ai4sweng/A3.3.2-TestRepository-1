# TravelHub

TravelHub is a simple API for managing travel bookings (flights and hotels),
destinations and users. Intended as a sample project with a classic layered
architecture:

```
api/         -> presentation layer (HTTP routes, input/output)
services/    -> business logic layer (use cases)
database/    -> data access layer (models + repositories)
schemas/     -> data validation and serialization (Pydantic-like)
core/        -> configuration, security and cross-cutting exceptions
utils/       -> generic helper functions, no business logic
scripts/     -> maintenance utilities outside the API flow
tests/       -> unit tests
```

## Architecture

This project follows a **layered architecture**:

`api -> services -> database`

- The `api` layer must not know database details.
- The `services` layer contains the business logic and orchestrates the repositories.
- The `database` layer implements the **Repository pattern**, isolating data access
  so that `services` does not depend on SQL or on a specific ORM.

## Installation

```bash
pip install -r requirements.txt
python main.py
```
