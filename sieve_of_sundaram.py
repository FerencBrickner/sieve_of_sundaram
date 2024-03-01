def sieve_of_sundaram(*, limit: int) -> list[int]:
    """Computing the primes from 2 up to a specified
    limit using the Sieve of Sundaram."""
    assert type(limit) is int and limit > 1

    class ChosenNode:
        _ = "These nodes will remain in the state."

    class NotChosenNode:
        _ = "These nodes will be deleted."

    limit += 1
    limit //= 2
    current_state = limit * [ChosenNode]

    _ = "Determining chosen nodes."

    for i in range(1, limit):
        for j in range(i, limit):
            if i + j + 2 * i * j >= limit:
                _ = "Index is becoming too large."
                break
            current_state[i + j + 2 * i * j] = NotChosenNode
    current_state = enumerate(current_state)

    def is_chosen_node(x):
        return x[1] == ChosenNode

    current_state = filter(is_chosen_node, current_state)

    _ = "Converting chosen nodes to prime numbers."

    def convert_node_to_prime(x):
        return 2 * x[0] + 1

    current_state = map(convert_node_to_prime, current_state)
    current_state = list(current_state)
    current_state[0] = 2
    return current_state


print(sieve_of_sundaram(limit=500))
