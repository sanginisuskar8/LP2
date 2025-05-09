def schedule_jobs():
    # Take user input for profits, jobs, and deadlines
    n = int(input("Enter the number of jobs: "))
    
    profit = []
    jobs = []
    deadline = []

    for i in range(n):
        job = input(f"Enter name of job {i+1}: ")
        jobs.append(job)
        p = int(input(f"Enter profit for job {job}: "))
        profit.append(p)
        d = int(input(f"Enter deadline for job {job}: "))
        deadline.append(d)
    
    # Combine profit, jobs, and deadlines into one list and sort by profit in descending order
    profitNJobs = list(zip(profit, jobs, deadline))
    profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)
    
    # Slot array to track which slots are filled
    slot = [0] * (n + 1)  # Slot array with n+1 slots (1-based index)
    ans = ['null'] * (n + 1)  # Answer array to store the scheduled jobs (1-based index)
    
    total_profit = 0  # To accumulate the total profit

    # Schedule the jobs
    for i in range(n):
        job = profitNJobs[i]
        # Try to find the latest available slot before or on the deadline
        for j in range(job[2], 0, -1):  # Check slots from deadline down to 1
            if slot[j] == 0:  # Slot is available
                ans[j] = job[1]  # Assign job to this slot
                total_profit += job[0]  # Add profit
                slot[j] = 1  # Mark this slot as filled
                break  # Break the loop as the job has been assigned
    
    print("Jobs scheduled buddy:", ans[1:])
    print("Total profit:", total_profit)

if __name__ == "__main__":
    schedule_jobs()
