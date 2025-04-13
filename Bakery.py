import simpy
import random

# Mohammad Zafari
# mhdzafari80@gmail.com

busy_employees = 0  # NE(t) = busy_employees
customers_handled  = 0  # NC(t) = num_customers - customers_handled
# we can get NE(t) and NC(t) with report(t) in any time t


class BakeryShop:
    def __init__(self, env, num_employees):
        self.env = env
        self.employees = simpy.Resource(env, num_employees)

    def support_customer(self, customer_id):
        yield self.env.timeout(random.normalvariate(10, 2))
        
def customer(env, customer_id, bakery_shop):
    global busy_employees
    global customers_handled
    
    with bakery_shop.employees.request() as request:
        print( f'customer {customer_id} request at {env.now}')
        yield request
        busy_employees += 1
        print(f"start support customer {customer_id} at {env.now}")
        yield env.process(bakery_shop.support_customer(customer_id))
        busy_employees -= 1
        customers_handled += 1
        print(f"finish support customer {customer_id} at {env.now}")

def generate_customers(env, num_customers, bakery_shop):
    for i in range(1, num_customers + 1):
        env.process(customer(env, i ,bakery_shop))
        yield env.timeout(random.expovariate(1.5))

# print NC(t) and NE(t) every 1 second from t = 0 
def report(env, n_customers, bakery_shop):
    global busy_employees
    global customers_handled
    
    while customers_handled != n_customers:
        customers_in_queue = len(bakery_shop.employees.queue) 
        print(f"NC({env.now}) = {customers_in_queue} \t NE({env.now}): {busy_employees}")
        yield env.timeout(1)


if __name__ == '__main__':
    random.seed(0)
    num_customers=15
    num_employees=2
    env = simpy.Environment()
    bakery_shop = BakeryShop(env, num_employees)
    env.process(generate_customers(env, num_customers, bakery_shop))
    env.process(report(env, num_customers, bakery_shop))
    env.run()