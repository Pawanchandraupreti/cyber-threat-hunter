package system.authz

default allow = false

allow {
    input.method == "GET"
    input.path = ["v1", "alerts"]
    input.user.role == "analyst"
}
allow {
    input.method == "POST"
    input.path = ["v1", "respond"]
    input.user.role == "responder"
    valid_team(input.user.teams, input.payload.team)
}