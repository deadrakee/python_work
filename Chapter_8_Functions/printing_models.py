def start_3d_print(requested_models, completed_models):
    """Simulate printing of requested lis of objects"""
    while requested_models:
        current_model = requested_models.pop()
        print(f"Printing {current_model}..")
        completed_models.append(current_model)


def print_completed(completed_models):
    """Show all completed models"""
    print()
    for completed_model in completed_models:
        print(f"{completed_model} is done")


request_jobs = ['batman logo', 'd12', 'container']
finished_jobs = []

start_3d_print(request_jobs, finished_jobs)
print_completed(finished_jobs)