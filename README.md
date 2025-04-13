# Candy-store-simulation-by-Simpy
# Assumptions
The waiting line in a store is endless: Every time a customer enters the store, regardless of how long the line is, they join the line and wait until they receive the desired service.
The customer who enters the line earlier receives the desired service earlier.
There are 2 employees, and the average time to serve a customer is the same for both employees.
If one employee is free, the customer goes to that employee. If both employees are free, one of them serves the customer.
# Simulation model components
**NC(t):** Number of customers waiting to receive the desired service at time t.
**NE(t):** Number of employees busy at time t.
**Sources**: Customers and employees.
**Events:** Customer arrival, employee service completion.
**Activities:** The time between the arrival of one customer and the next., service time by an employee.
**Latency:** The time a customer waits to access a service.

1. Our model has 2 employees, modeled as “resources”. The customer and employee activities are simple: a customer requests a unit from the resource, if a resource is available, the customer receives the requested service (the requested unit cannot fulfill other customers’ orders while fulfilling another customer’s order). If the employee is not available, the customer joins the waiting line to receive the requested service in his turn.
2. When each customer receives the desired service and the resource unit (employee) is freed, the employee can serve the next person in the queue.
3. We assume that the service time follows a normal distribution with a mean of 10 and a standard deviation of 2. Furthermore, our customers enter the store at random times.
4. The candy store has certain high-priority customers who should be served as soon as they enter the store. The model is reconstructed using this assumption.(**Bakery_priority.py**) 
