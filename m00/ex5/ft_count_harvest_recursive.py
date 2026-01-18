def ft_count_harvest_recursive():
    harvest_day = int(input("Days until harvest: "))
    def recursive_helper(current_day):
        if current_day < harvest_day:
            print(f"Day {current_day}")
            recursive_helper(current_day + 1)
        elif current_day == harvest_day:
            print(f"Day {current_day}")
            print("Harvest time!")
    recursive_helper(1)